def func():
    print('First line!')
    yield 1#生成器迭代到此处返回1

    print('Second line!')
    yield 2#生成器迭代到此处返回2

    print('Third line!')
    yield 3#生成器迭代到此处返回3

# func函数包含三个yield语句, 它是一个生成器函数, 调用可创建生成对象g
g = func()
# 每次next对于生成器函数, 将一直执行到下一次yield位置
'''
# g包含迭代器接口__next__
# 第一次迭代
print(g.__next__()) #先调用内部的打印, 再打印本身的返回值
# 第二次迭代
print(g.__next__()) #先调用内部的打印, 再打印本身的返回值
# 第三次迭代
print(g.__next__()) #先调用内部的打印, 再打印本身的返回值
# 第四次迭代
print(g.__next__()) #迭代超出范围
'''
# g还有可迭代对象的接口__iter__
for x in g:
    print(x)

#g的可迭代对象接口返回的还是自身
print(g.__iter__() is g)