import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
mpl.rcParams['font.sans-serif']=[u'SimHei']
mpl.rcParams['axes.unicode_minus']=False
plt.xlim((0,1))
plt.ylim((0,1))

plt.xlabel('x')
plt.ylabel('y')

x = np.linspace(0.01,1,100)

plt.plot(x, pow((x+(1-x)*0.03),2), 'g--', linewidth=1, label="f(x)")

plt.text(10,20,'f(x)',size=13)

plt.legend(['f(x)'], loc='upper left')

plt.show()