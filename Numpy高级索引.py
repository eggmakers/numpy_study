import numpy as np

x = np.array([[1, 2], [3, 4], [5, 6]])
y = x[[0, 1, 2], [0, 1, 0]]
print(y)

#获取4X3数组的四个角的元素
x = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]])
print(x)
rows = np.array([[0, 0], [3, 3]])
cols = np.array([[0, 2], [0, 2]])
y = x[rows, cols]
print(y)

#布尔索引
print(x[x > 5])

#过滤NaN
a = np.array([np.nan, 1, 2, np.nan, 3, 4, 5])
print(a[~np.isnan(a)])

#过滤非复数元素
a = np.array([1, 2+6j, 5, 3.5+5j])
print(a[np.iscomplex(a)])

#使用整数数组进行索引
x = np.arange(9)
print(x)
x2 = x[[0, 6]]
print(x2)

#二维数组
x = np.arange(32).reshape((8, 4))
print(x)
print(x[[4, 2, 1, 7]])#读取下标对应的行

#传入倒序索引数组
print(x[[-4, -2, -1, -7]])

#传入多个索引数组
x = np.arange(32).reshape((8, 4))
print(x[np.ix_([1, 5, 7, 2], [0, 3, 1, 2])])
