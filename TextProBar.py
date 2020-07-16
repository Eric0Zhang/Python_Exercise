import time
from math import pi
from math import sin
from math import ceil
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