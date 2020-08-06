# 比较符重载 和 装饰器简化重载过程
from functools import total_ordering #比较运算装饰器 通过小于和等于推断其他所有比较
from abc import ABCMeta, abstractmethod #虚方法 抽象方法装饰器
from math import pi

# 使用此装饰器以后,只要实现less than(lt)和equal(eq)就可以实现其他比较运算重载
# 其他重载包括:less equal(le) greater than(gt) greater equal(ge) not equal(ne)
@total_ordering 
class Shape(object):
    @abstractmethod #虚函数的装饰器
    def area(self):
        pass #虚函数没有具体实现,每个子类实现方式不同,即多态
    # obj是比较符后面的对象
    def __lt__(self, obj): 
        if not isinstance(obj,Shape):
            raise TypeError('obj is not Shape class!')
        print('in lt')
        return self.area()<obj.area()
    
    def __eq__(self, obj):
        print('in eq')
        return self.area() == obj.area()

class Rectangle(Shape):
    def __init__(self,w,h):
        self.w = w
        self.h = h
    def area(self):
        return self.w * self.h

class Circle(Shape):
    def __init__(self,r):
        self.r = r
    def area(self):
        return self.r ** 2 * pi

r1 = Rectangle(5,3)
r2 = Rectangle(4,4)
c1 = Circle(3)

# 比较时,调用超类的比较函数,比较函数调用虚函数(面积)进行比较,
# 虚函数由不同子类各自实现,即为多态
print(r1>r2)
# 这步通过装饰器检查了lt 和 eq两步,lt是false,装饰器推断出>为True, eq是false,
# 那么>=即True or False = True, 实际上在判断到>为True,解释器就跳过了对=的判断
print(c1>=r1)
print(r2>c1)