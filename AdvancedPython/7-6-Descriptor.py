# 用描述符进行类型检查
# Python是动态语言,变量的类型可以随意改变,解释器并不检查
# 因此如果想要进行类型检查,不需自己实现,这里采用描述符来实现

# 类当中只要实现了get set delete当中的任意一个,概率就是描述符类
# 描述符类的get set delete方法的第二个参数是调用描述符的类的实例,
# 例如主函数中的s,第三个参数是调用描述符的类的类型,如主函数中的Person
class Attr(object):
    def __init__(self, name, type_):
        self.name = name
        self.type_ = type_

    def __get__(self, instance, cls):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, self.type_):
            raise TypeError('expected an %s' % self.type_)
        instance.__dict__[self.name] = value

    # 注意这里是delete,是描述符的删除方法,不是析构,析构是__del__
    def __delete__(self, instance):
        del instance.__dict__[self.name]
        #raise AttributeError("can't delete this attr")

# Person中本身没有通过__slots__或者__init__(dict)创建name等属性
# 而是通过调用描述符的构造函数,与描述符类进行了绑定
# 在对这些动态的属性进行增删改查等操作时,就会调用描述符的
# get set delete方法,于是可以在其中进行类型检查都中间操作
class Person(object):
    name    = Attr('name', str)
    age     = Attr('age', int) 
    height  = Attr('height', float)
    weight  = Attr('weight', float)

s = Person()
# 原本Person类是没有任何属性的,下面这些赋值操作,都会调用
# 描述符的set方法, 创建属性, 并进行类型检查
s.name = 'Bob'
s.age = 17
s.height = 1.82
s.weight = 52.5
del s.age
# 这里可以看到, 各个属性已经动态创建到Person类中了.
print(s.__dict__)
