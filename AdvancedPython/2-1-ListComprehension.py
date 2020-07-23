import timeit
from random import randint

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

#生成一个1到20学号的随机分数, 这也是一个没有条件语句的字典解析
dct = {key:randint(70,100) for key in range(1,21)}
print(dct)

#对整个字典, 进行条件为分数大于90的解析
high = {key:value for key,value in dct.items() if value>90}
print(high)

