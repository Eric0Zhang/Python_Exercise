from math import pi

class Circle(object):
    def __init__(self, radius):
        self.radius = radius

    def getRadius(self):
        return self.radius #这里还可以对属性进行读取的预处理工作,比如取整,或者转换成字符串输出等

    def setRadius(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError('wrong type.' )
        self.radius = float(value)

    def getArea(self):
        return self.radius ** 2 * pi

    R = property(getRadius, setRadius)

c = Circle(3.2)
# 直接访问读写类的属性是有一定风险的,例如:
# c.radius = 'abc' #这里不小心将半径赋值为字符串了,但是Python允许直接赋值覆盖,没有类型检查
# 因此我们通常需要对属性用专门的方法进行管理,即get方法和set方法
# c.setRadius('abc') #这里set方法中进行了类型检测,避免了赋值错误
# 但是不管是调用方法,写法比较犯错,直接赋值更加直观,
# 我们可以使用property函数来为类创建半径的管理属性,可以将调用操作和赋值操作对应到get和set方法
print (c.R)
c.R = 'abcc' #这里会调用set方法进行类型检查
print (c.R)

