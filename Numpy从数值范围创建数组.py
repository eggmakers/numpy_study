###numpy.arange
import numpy as np
x = np.arange(5)
print(x)
x = np.arange(5, dtype=float)#设置类型为浮点
print(x)

#设置起始值，终止值和步长
x = np.arange(10 ,20 , 2)
print(x)

#创建一个等差数列组成的数组
a = np.linspace(1, 10, 10)
print(a)

a = np.linspace(1, 1, 10)
print(a)

#不设立终止值
a = np.linspace(10, 20, 5, endpoint=False)
print(a)
#设立终止值
a = np.linspace(10, 20, 5, endpoint=True)
print(a)

#拓展
b = np.linspace(1, 10, 10).reshape([10, 1])
print(b)

###numpy.logspace创建一个等比数列
a = np.logspace(1.0, 2.0, num=10)
print(a)
#默认底数是10
a = np.logspace(0,9,10,base=2)
print (a)