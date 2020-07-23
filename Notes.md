
# Python学习笔记

---
### 1 Python语法技巧

#### 1.1 字典和集合的注意事项
字典和集合都用{}来赋值，然而字典属于序列类型，而集合是区别于序列的无序元素组合类型。
由于公用大括号作为标识符，<u>**空大括号**</u>只能用来初始化字典：
```
>>> aa = set()
>>> aa
set()
>>> dict = {} #空的大括号创建的是字典
>>> dict
{}
>>> type(aa)
<class 'set'>
>>> type(dict)
<class 'dict'>
```
这种优先给字典用的做法，很大程度上决定于，字典使用的频率更高，是一种更实用的组合数据类型。
#### 1.2 Python解释器清空内存变量
在使用解释器进行试验的时候，经常会遇到长时间试验，无用的变量太多的情况。
这时候可以使用`dir()`来查看内存中的变量，然后是用`del()`来清除对应的变量，不过这只是清除变量名，并没有清除变量的内存，使用垃圾回收可以同时释放内存和变量名：
```
import gc
gc.collect(val)
```
这种方法在变量比较多的时候，还是很麻烦，于是可以通过判断是否是系统变量，把多于的变量全部删除：
```
for name in dir():
    if not name.startswith('_'):
        del globals()[name]

for name in dir():
    if not name.startswith('_'):
        del locals()[name]
```
这里`locals`和`globals`返回的是局部变量列表和全局变量列表，用del删除即可，也可以用gc，如果你比较重视内存的话，实际上试验产生的内存占用通常不会太多。
另外如果你使用的是ipython解释器，还可以使用：reset命令来清除内存变量。reset如果不带参数调用，则通过删除用户定义的所有名称来重置命名空间。

### 2 Python高级编程
#### 2.1 列表解析 List Comprehension
列表解析的基本格式如下:
`[expr for iter_var in iterable if condition]`
expr是一个表达式, 其后是一个迭代表达式, 迭代表达式后面可选的, 可以加`if`条件语句.
```python
def listcycle():
    data = [2,4,7,1,-10,-4,-1,-8,-4,9]
    retlist = []
    for num in data:
        if num >= 0:
            retlist.append(num)
    return retlist


#data = [randint(-10,10) for _ in range(10)]
data = [2,4,7,1,-10,-4,-1,-8,-4,9]
#基本的按照循环来解析
cyc = listcycle()
#按照If的条件,解析列表中的所有元素
lc = [x for x in data if x>=0]

#计算循环函数的用时
print('循环耗时:%.3f' % timeit.timeit('listcycle()','from __main__ import listcycle'))

#计算列表解析的时间
print('列表解析耗时:%.3f' % timeit.timeit('[x for x in data if x>=0]','data = [2,4,7,1,-10,-4,-1,-8,-4,9]'))

```
可以得到循环的耗时为0.688s, 而列表解析方法的耗时为0.449s. 明显列表解析的效率更高.

同样对于字典也可以有列表解析,包括带条件的和不带条件的:
```python
#生成一个1到20学号的随机分数, 这也是一个没有条件语句的字典解析
dct = {key:randint(70,100) for key in range(1,21)}
print(dct)

#对整个字典, 进行条件为分数大于90的解析
high = {key:value for key,value in dct.items() if value>90}
print(high)
```
注意字典在迭代时,使用的是dct.items()方法.
