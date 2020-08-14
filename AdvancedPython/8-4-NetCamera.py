import os, cv2, struct, threading
from http.server import BaseHTTPRequestHandler
from socketserver import ThreadingTCPServer
from threading import Thread, RLock
from concurrent.futures import ThreadPoolExecutor

# streamer从摄像头采集数据 继承线程类Thread,它本身就是一个线程,名称叫做JpegStreamer
class JpegStreamer(Thread):
    def __init__(self, camera):
        # 调用父类的构造器,构造器将返回一个线程对象
        Thread.__init__(self)
        # opencv视频捕捉
        self.cap = cv2.VideoCapture(camera)
        # 可重入线程锁
        self.lock = RLock()
        # 视频分发的管道,保存为一个字典key是读取描述符,value是写入描述符
        self.pipes = {}

    # 注册管道
    def register(self):
        # 创建管道返回读取和写入的文件描述符
        pr, pw = os.pipe()
        # 保存管道时,上锁,防止管道没写完时,进入其他线程
        self.lock.acquire()
        self.pipes[pr] = pw
        self.lock.release()
        return pr
    # 注销管道
    def unregister(self, pr):
        # 管道没有close方法,应该是自动释放了,后面仔细看一下pipe相关的内容
        # pr.close()
        # self.pipes[pr].close()

        self.lock.acquire()
        self.pipes.pop(pr)
        self.lock.release()

    # opencv捕捉循环
    def capture(self):
        cap = self.cap
        while cap.isOpened():
            ret, frame = cap.read()
            if ret:
                # 对获取到的帧进行图片编码
                ret, data = cv2.imencode('.jpg', frame, (cv2.IMWRITE_JPEG_QUALITY, 40))
                # 转换成字符
                yield data.tostring()

    def send(self, frame):
        n = struct.pack('l', len(frame))
        self.lock.acquire()
        if len(self.pipes):
            lst = self.pipes.values()
            #_, pipes, _ = select([], lst, [], 1) # select只用用于套接字 不能用于管道
            for pipe in lst:
                os.write(pipe, n)
                os.write(pipe, frame)
        self.lock.release()

    def run(self):
        # capture定义在前面是个生成器,所以每个frame是yield返回的图片数据,
        # 生成器是个无限循环,所以这里迭代也是无限次,直到cap被关闭
        for frame in self.capture():
            self.send(frame)

# retriever生成streamer对象,并从中获取帧
class JpegRetriever(object):
    def __init__(self, streamer):
        self.streamer = streamer
        self.local = threading.local()

    # 从管道获取数据,形成生成器
    def retrieve(self):
        while True:
            ns = os.read(self.local.pipe, 8)
            n = struct.unpack('l', ns)[0]
            data = os.read(self.local.pipe, n)
            yield data

    # enter和exit方法实现上下文管理
    def __enter__(self):
        if hasattr(self.local, 'pipe'):
            raise RuntimeError()
        
        # 让每个retriever对象的独立线程中都对接上streamer的管道
        self.local.pipe = streamer.register()
        return self.retrieve()

    def __exit__(self, *args):
        self.streamer.unregister(self.local.pipe)
        del self.local.pipe
        return True

# http的request回调函数,每次有客户端请求,都会做出响应
class Handler(BaseHTTPRequestHandler):
    retriever = None

    # 静态方法 给handler指定retriever
    @staticmethod
    def setJpegRetriever(retriever):
        Handler.retriever = retriever

    # request中的GET指令响应
    def do_GET(self):
        if self.retriever is None:
            raise RuntimeError('no retriver')

        if self.path != '/':
            return

        self.send_response(200) 
        self.send_header("Content-type", 'multipart/x-mixed-replace;boundary=abcde')
        self.end_headers()

        # 上下文管理形式迭代retriever
        with self.retriever as frames:
            for frame in frames:
                self.send_frame(frame)
    
    # 把数据发送到web
    def send_frame(self, frame):
        # 注意这里python3 必须写二进制 不然报错
        self.wfile.write(b'--abcde\r\n')
        self.wfile.write(b'Content-Type: image/jpeg\r\n')
        self.wfile.write(b'Content-Length: %d\r\n\r\n' % len(frame))
        self.wfile.write(frame)

# 改写多线程TCP服务器类,改为线程池创建线程,
# 重写ThreadingTCPSever的构造器和proces_request方法
class PoolThreadingTCPServer(ThreadingTCPServer):
    # ThreadingTCPSever继承TCPSever(TCP服务器)和ThreadingMixIn(TCP访问的线程操作),并且没有本身的方法,所有方法调用这两个基类的
    # 重构TCPSever的构造函数,增加线程池深度参数,默认最多100个线程
    def __init__(self, server_address, RequestHandlerClass, bind_and_activate=True, max_thread=100):
        super().__init__(server_address, RequestHandlerClass, bind_and_activate)
        self.executor = ThreadPoolExecutor(max_thread)
    def process_request(self, request, client_address):
        """Start a new thread to process the request."""
        self.executor.submit(self.process_request_thread, request, client_address)
        # t = threading.Thread(target = self.process_request_thread,
        #                     args = (request, client_address))
        # t.daemon = self.daemon_threads
        # if not t.daemon and self.block_on_close:
        #     if self._threads is None:
        #         self._threads = []
        #     self._threads.append(t)
        # t.start()

if __name__ == '__main__':
    # streamer是一个独立的线程,将获取的视频流放入Pipe
    streamer = JpegStreamer(0)
    streamer.start()
    # retriever的每个实例都创建一个独立的线程,它们与streamer之间通过pipe进行通信,即通过pipe获取视频
    retriever = JpegRetriever(streamer)
    # handler在每个http的request时,都创建一个retriever,而retriever通过其实例的多线程实现并发
    Handler.setJpegRetriever(retriever)

    print('Start server...')
    # 这里的ThreadingTCPServer是一个并发的TCP服务器,多线程实现,因此Handler也会在每个不同线程中重入
    # PoolThreadingTCPSever重写了多线程创建部分,这里指定线程池最大深度是3,这样访问的数量超过三个就会阻塞,等待某个线程释放
    httpd = PoolThreadingTCPServer(('192.168.1.128', 9000), Handler, max_thread = 3)
    httpd.daemon_threads = True
    threading.Thread(target=httpd.serve_forever, name='httpd', daemon=True).start()
    #httpd.serve_forever()
    while True:
        cmd = input('>>>').strip()
        if cmd == 'quit':
            httpd.server_close()
            break
        print(threading.enumerate())
