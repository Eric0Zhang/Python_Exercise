from threading import Thread
import turtle

def koch(size,n):
    if n==0:
        turtle.fd(size)
    else:
        for angle in [0,60,-120,60]:
            turtle.left(angle)
            koch(size/3,n-1)

def drawkoch():
    turtle.setup(600,600)
    turtle.penup()
    turtle.goto(-200,100)
    turtle.pendown()
    turtle.pensize(2)
    turtle.speed(100)
    koch(400,4)
    turtle.right(120)
    koch(400,4)
    turtle.right(120)
    koch(400,4)
    turtle.hideturtle()
    turtle.done()

import time
from math import pi
from math import sin
from math import ceil
def progress():
    scale = 50
    print("执行开始".center(scale,"-"))
    start = time.perf_counter()
    for i in range(scale+1):
        #x = i+(1-sin(i*pi*2+pi/2))/-8
        x = pow((i/scale+(1-i/scale)*0.03),2)
        a = '*'*round(x*50)
        b = '.'*(scale-ceil(x*50))
        c = (x*50/scale)*100
        dur = time.perf_counter() - start
        #退回行首 /r
        print("\r{:^3.0f}%[{}->{}]{:.3f}s".format(c,a,b,dur),end='')
        time.sleep(0.1)
    print("\n"+"执行结束".center(scale,"-"))

t = Thread(target=drawkoch)
t2 = Thread(target=progress)
t.start()
t2.start()

# 两个子线程如果没有执行完,会阻塞在这里
t.join()
t2.join()
print('main thread finished.')

