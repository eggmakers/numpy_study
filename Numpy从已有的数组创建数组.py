###numpy.asarray
import numpy as np

x = [1, 2, 3]
a = np.asarray(x)
print(a)#将列表转换为ndarray

x = (1, 2, 3)
a = np.asarray(x)
print(a)#将元组转换为ndarray

#设置了dtype参数
x = [1, 2, 3]
a = np.asarray(x, dtype=float)
print(a)

###numpy.frombuffer用于实现动态数组
s = b'Hello World'
a = np.frombuffer(s, dtype= 'S1')
print(a)

###numpy.fromiter从可迭代对象中建立 ndarray 对象，返回一维数组
list = range(5)
it = iter(list)

x = np.fromiter(it, dtype=float)
print(x)