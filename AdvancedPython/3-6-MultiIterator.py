from random import randint

# 列表解析创建分数
math = [randint(45,100) for _ in range(40)]
chinese = [randint(65,100) for _ in range(40)]
english = [randint(55,100) for _ in range(40)]

#总分列表
total = []
# 内置函数zip可以组合多个可迭代对象
# for的拆包可以提取组合对象的每个元素中的各项
for m,c,e in zip(math,chinese,english):
    total.append(m+c+e)

#打印所有人的总分
for x in total:
    print(x)