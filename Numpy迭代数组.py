import numpy as np

a = np.arange(6).reshape(2, 3)
print(a)

for x in np.nditer(a):
    print(x, end=',')
print('\n')

# c顺序访问
for x in np.nditer(a.T):
    print(x, end=',')
print('\n')
for x in np.nditer(a.T.copy(order='C')):
    print (x, end=", " )

###控制遍历顺序
a = np.arange(0, 60, 5)
a = a.reshape(3, 4)
print('原始数组是：')
print(a)
print('\n')
b = a.T
print(b)
print('\n')
print('以C风格顺序排序：')
c = b.copy(order='C')
print(c)
for x in np.nditer(c):
    print(x, end=',')
print('\n')
print('以F风格顺序排序：')    
c = b.copy(order='F')
print(c)
for x in np.nditer(c):
    print(x, end=',')

###修改数组中元素的值
a = np.arange(0, 60, 5)
a = a.reshape(3, 4)
print('\n')
print('原始数组是：')
print(a)
print('\n')
for x in np.nditer(a, op_flags=['readwrite']):
    x[...] = 2 * x
print('修改后的数组是：')
print(a)

###使用外部循环
a = np.arange(0, 60, 5)
a = a.reshape(3, 4)
print('\n')
print('修改后的数组为：')
for x in np.nditer(a, flags=['external_loop'], order='F'):
    print(x, end=',')

###广播迭代
a = np.arange(0, 60, 5)
a = a.reshape(3, 4)
print('第一个数组为：')
print(a)
print('\n')
print('第二个数组为：')
b = np.array([1, 2, 3, 4], dtype=int)
print(b)
print('\n')
print('修改后的数组为：')
for x,y in np.nditer([a,b]):  
    print ("%d:%d"  %  (x,y), end=", " )