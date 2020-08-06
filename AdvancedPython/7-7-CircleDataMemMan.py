# 正常的类对象解释器会记录它的引用计数, 可以通过sys.getrefcount得到
# 当引用计数变为零时,解释器自动调用类的析构函数,释放掉对象
# 但对于环形数据结构,比如图和树,他们存在一些例如子节点和父节点互相引用的情况,
# 这就需要用到weakref来对循环引用的情况进行处理

import weakref

class Data(object):
    def __init__(self, value, owner):
        # 如果这里不用weakref,那么就是
        # Node对象和Data的对象循环引用, 即node引用了self.data
        # Data中又通过owner引用了node,这时del node不能立即回收内存
        #self.owner = owner
 
        # 如果使用了weakref,解释器会立即释放这个循环引用,
        # 引用计数清零,然后析构回收内存
        # 弱引用的作用在于可以访问owner, 但是不增加它的引用计数
        # 这样就不存在循环引用了
        self.owner = weakref.ref(owner)
        self.value = value

    def __str__(self):
        # 注意对于弱引用,必须按照函数形式来调用
        return "%s's data, value is %s" % (self.owner(), self.value)

    def __del__(self):
        print('in Data.__del__') 

class Node(object):
    def __init__(self, value):
        self.data = Data(value, self)

    def __del__(self):
        print('in Node.__del__')

node = Node(100)
print(node.data) # 打印一个类的对象时, 如果有str方法,则被其拦截
del node
input('wait...')
