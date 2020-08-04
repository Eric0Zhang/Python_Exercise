# 上下文支持是指类似 with open() as f:这样的语句,
# 把一个普通的函数形成一个类似于函数的上下文结构,
# 然后f在上下文结束以后,自动关闭销毁
'''with open('test.txt', encoding = 'utf-8') as f:
    print(f.readline())
    # f.close #不需要close 程序块结束,自动close
print("test over.")
f.readline()#这里会报错'''

# 下面创建一个类, 实现自定义类对上下文管理的支持
from telnetlib import Telnet # 远程登录服务
from sys import stdin, stdout
from collections import deque

class TelnetClient(object):
    def __init__(self, addr, port=23):
        self.addr = addr
        self.port = port
        self.tn = Telnet(self.addr, self.port)
        self.history = deque()

    def start(self):
        #raise Exception('Test')
        # user
        t = self.tn.read_until(b'raspberrypi login: ')
        stdout.write(t.decode())
        user = stdin.readline()
        susr = user.encode()
        self.tn.write(susr)

        # password
        t = self.tn.read_until(b'Password: ')
        s = t.decode()
        if s.startswith(user[:-1]): s = s[len(user) + 1:]
        stdout.write(s)
        stdout.flush()
        self.tn.write(stdin.readline().encode())

        t = self.tn.read_until(b'$ ')
        stdout.write(t.decode())
        #stdout.flush()
        while True:
            uinput = stdin.readline()
            if uinput=='testend\n':
                break
            self.history.append(uinput)
            self.tn.write(uinput.encode())
            t = self.tn.read_until(b'$ ')
            s = t.decode()
            stdout.write(s[len(uinput) + 1:])
            #stdout.flush()

    def cleanup(self):
        pass

    # 实现了enter和exit方法,即可支持上下文管理with xx() as x:
    # 进入块调用enter
    # 退出块调用exit
    def __enter__(self):
        self.tn = Telnet(self.addr, self.port)
        self.history = deque()
        return self 

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('In __exit__')

        self.tn.close()
        self.tn = None
        with open(self.addr + '_history.txt', 'w') as f:
            f.writelines(self.history)
        return True

with TelnetClient('192.168.1.110') as client:
    client.start()


'''
client = TelnetClient('192.168.1.110') 
print ('\nstart...')
client.start()
print ('\ncleanup')
client.cleanup()'''

