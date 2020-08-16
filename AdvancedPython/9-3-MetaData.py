# inner函数内嵌到outer中,形成闭包,inner捕获的outer变量有name num,他们会随闭包和inner的函数对象一起保存.
def outer():
    '''this is a closure'''
    name="python"
    num=10
    def inner():
        '''this is a local func'''
        print(name)
        print(num)
    return inner

# outer返回inner的函数对象,赋值给res        
res=outer()
res()
# 元数据__closure__包含了闭包的变量列表,类型为cell,可以通过cell_contents返回其内容
print('闭包中包含变量',res.__closure__[0].cell_contents,res.__closure__[1].cell_contents)
# 元数据__name__ 返回函数名称
print(res.__name__)
# 元数据__doc__ 返回说明文档
print(res.__doc__)
# 元数据__dict__ 返回对象的属性字典
print(res.__dict__)
# 元数据__module__ 返回所属模块
print(res.__module__)
