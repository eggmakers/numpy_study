###numpy.empty用于创建一个指定形状，数据类型且未初始化的数组
import numpy as np
x = np.empty([3, 2], dtype=int)
print(x)
###numpy.zeros创建一个0填充数组
x = np.zeros(5)
print(x)#默认是浮点
y = np.zeros((5,), dtype=int)
print(y)#设置为整型
z = np.zeros((2, 2), dtype=[('x', 'i4'), ('y', 'i4')])
print(z)#自定义类型
###numpy.ones创建一个1填充数组
x = np.ones(5)
print(x)#默认为浮点数
x = np.ones([2, 2], dtype=int)
print(x)#自定义类型
###numpy.zero_like用于创建一个与给定数组相同形状的数组，元素全是0
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
zero_arr = np.zeros_like(arr)
print(zero_arr)
###numpy.ones_like用于创建一个与给定数组相同形状的数组，元素全是0
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
ones_arr = np.ones_like(arr)
print(ones_arr)