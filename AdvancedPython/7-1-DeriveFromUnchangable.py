from typing import Iterable

# 元组是不可变类型,我们想创建一个新的元祖类,
# 该类可以滤除元祖中的非正整数元素, 
# 即这个类需要删除不可变元组中的数据,实现可变
class IntTuple(tuple):
    # __new__方法先于__init__执行时构造函数的前一步骤
    # 第一个参数cls命名不唯一,跟self一样都是自定义的变量名,
    # 但是必须是函数的第一个参数,cls是一个类对象
    # python中一切都是对象,数字是对象,类的实例化是对象,
    # 类本身也是对象,可以理解成就是类的定义被指向了cls
    # 在创建IntTuple的对象时,IntTuple类被传递给cls
    def __new__(cls, iterable):
        #通过生成器遍历元组的所有元素生成一个新的元组
        g = (x for x in iterable if isinstance(x,int) and x>0)
        # super函数获取第一个参数类的父类,
        # 然后将第二个参数对象转换为该父类对象,并返回
        # 这里比较特殊, cls是IntTuple的类对象,而不是实例对象
        # 但是一样可以返回父类的类对象
        # 然后调用父类对象的new方法,用g来创建init的self对象
        return super(IntTuple, cls).__new__(cls,g)
    
    # __init__方法是实例化一个对象必须的,self代表这个对象,
    # 后面跟随的参数是构造函数初始化的参数变量,
    # 这里是一个可迭代对象,对于本例调用时传入的是一个元组
    # 所以这个iterable也不是什么类型,只是个变量名
    def __init__(self, iterable):
        # 构造器调用父类构造其之前想要改变iterable的内容是没用的
        # 因为self已经创建好了,并且因为是不可变类型,因而不可直接修改
        # 而这个self实例是由__new__方法创建的
        # 父类即元祖类的init的方法在python3中,只接受隐式的实例,即self,
        # 括号中不能有其他东西,否则会报错:
        # object.__init__() takes exactly one argument (the instance to initialize) 
        print(self)#self在这里被new改造过了
        super(IntTuple, self).__init__()

# 传入一个可迭代对象 列表
t = IntTuple([1,-1,'abc',6,['x','y'],3])
print(t)