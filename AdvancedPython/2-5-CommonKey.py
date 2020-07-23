#sample是随机取样函数,可以从列表中随机获取几个元素
from random import randint, sample
from functools import reduce
#7为前锋,每轮有三到六个人进球
players = ['Messi','C Ronald','Suya','Neymar','Pogba','Grizz','Bell']
round1 = sample(players,randint(3,6))
round2 = sample(players,randint(3,6))
round3 = sample(players,randint(3,6))
#每轮进球的球员有概率仅1到4球
dictGoal1 = {key:randint(1,4) for key in round1 }
dictGoal2 = {key:randint(1,4) for key in round2 }
dictGoal3 = {key:randint(1,4) for key in round3 }

print('每轮进球情况如下:\n',dictGoal1,'\n',dictGoal2,'\n',dictGoal3,'\n')

#其中每轮都进球的球员有如下球员,Keys返回的是集合类型的键,利用集合的交操作可以得到公共键
#print('Following Players Goal every round:\n',dictGoal1.keys() & dictGoal2.keys() & dictGoal3.keys())
#如果轮数比较多,大量用交操作不方便,可以用map函数对每一轮进行取键值,然后用reduce函数对各轮球员进行交操作的迭代
bestplayer = reduce(lambda a,b: a&b, map(dict.keys,[dictGoal1,dictGoal2,dictGoal3]))
print('Following Players Goal every round:\n',bestplayer)