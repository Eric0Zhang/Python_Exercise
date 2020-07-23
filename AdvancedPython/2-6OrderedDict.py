from collections import OrderedDict
from time import time
from random import randint

players = list('ABCEDFGH')

#普通的字典是按键的名称排序的,而OrderedDict是按照添加的顺序排序的
dct = OrderedDict()
start = time()
for i in range(8):
    input()
    p = players.pop(randint(0,7-i))
    end = time()
    print(i+1,p, end-start)
    dct[p] = (i+1, end-start) 

print()
print('-'*20)

for k in dct:
    print(k,dct[k])