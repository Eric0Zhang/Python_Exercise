import turtle as t

t.title('自动轨迹绘制')
t.setup(800,600,0,0)
t.pencolor('red')
t.pensize(5)
datalist = []
f = open("route.txt","rt")
line = f.readline()
line = line.replace('\n','')
while line!='':
    # map 是一个迭代器,用eval函数对第二个参数列表的每一项进行迭代
    # 产生的若干数值再转化成List,每个小列表作为元素添加到datalist中
    datalist.append(list(map(eval,line.split(','))))
    line = f.readline()
    line = line.replace('\n','')
f.close()

#自动绘制
for i in range(len(datalist)):
    t.pencolor(datalist[i][3],datalist[i][4],datalist[i][5])
    t.fd(datalist[i][0])
    if datalist[i][1]:
        t.right(datalist[i][2])
    else:
        t.left(datalist[i][2])

t.hideturtle()
t.done()