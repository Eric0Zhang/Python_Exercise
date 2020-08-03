class Player(object):
    def __init__(self, uid, name, status=0, level=1):
        # 成员变量的定义必须直接放在构造函数中
        # 构造函数外定义的变量是类变量(静态变量),所有实例共享
        self.uid = uid
        self.name = name
        self.stat = status
        self.level = level
    
class Player2(object):
    # 通过重定义object类的__slot__方法节省内存
    # 提前声明所有属性,舍弃python类的__dict__动态添加属性的特性,__dict__默认占用1048字节,浪费空间
    __slots__ = ['uid','name','stat','level']
    def __init__(self, uid, name, status=0, level=1):
        self.uid = uid
        self.name = name
        self.stat = status
        self.level = level

p1 = Player('0001','Jim')
p2 = Player2('0002','Jim')
# dir返回对象的所有属性和方法
# 两个集合详见得到Player对象比Player2对象多出来的属性
print(dir(p1))
print(dir(p2))
print(set(dir(p1)) - set(dir(p2)))# 可以看到 默认的类是有__dict__属性的,占用1048字节,用于动态添加和删除自定义属性