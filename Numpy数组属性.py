import numpy as np

### ndarray.ndim
a = np.arange(24)
print(a.ndim)#a只有一个维度
#现在调整其大小
b = a.reshape(2, 4, 3)
print(b.ndim)

###ndarray.shape
a = np.array([[1, 2, 3], [4, 5, 6]])
print(a.shape)
#调整数组大小
a = np.array([[1, 2, 3], [4, 5, 6]])
a.shape = (3, 2)
print(a)
a = np.array([[1, 2, 3], [4, 5, 6]])
b = a.reshape(3, 2)
print(b)
###ndarray.itemsize返回数组的每一个元素的大小
x = np.array([1, 2, 3, 4, 5], dtype=np.int8)
print(x.itemsize)
y = np.array([1, 2, 3, 4, 5], dtype=np.float64)
print(y.itemsize)
###ndarray.flags包含以下属性
# C_CONTIGUOUS (C) 数据是在一个单一的C风格的连续段中
# F_CONTIGUOUS (F) 数据是在一个单一的Fortran风格的连续段中
# OWNDATA (O)      数组拥有它所使用的内存或从另一个对象中借用它
# WRITEABLE (W)    数据区域可以被写入，将该值设置为 False，则数据为只读
# ALIGNED (A)      数据和所有元素都适当地对齐到硬件上
# UPDATEIFCOPY (U) 这个数组是其它数组的一个副本，当这个数组被释放时，原数组的内容将被更新
x = np.array([1, 2, 3, 4, 5])
print(x.flags)