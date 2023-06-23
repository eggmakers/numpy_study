import numpy as np

#reshape
a = np.arange(8)
print('原始数组')
print(a)
print('\n')

b = a.reshape(4, 2)
print('修改后的数组')
print(b)
print('\n')

#flat数组提取
a = np.arange(9).reshape(3, 3)
print("原始数组")
for row in a:
    print(row)
print('迭代后的数组')
for element in a.flat:
    print(element)

#flatten数据复制
a = np.arange(8).reshape(2, 4)
print("原数组")
print(a)
print('\n')
print("展开的数组")
print(a.flatten())
print('\n')
print("以F风格顺序展开的数组")
print(a.flatten(order='F'))
print('\n')

#ravel展开数组
a = np.arange(8).reshape(2, 4)
print("原数组：")
print(a)
print('\n')
print("调用ravel函数之后：")
print(a.ravel())
print('\n')
print('以 F 风格顺序调用 ravel 函数之后：')
print(a.ravel(order = 'F'))
print('\n')

#transpose用于对换数组的维度
a = np.arange(12).reshape(3, 4)
print("原数组：")
print(a)
print('\n')

print("转置")
print(np.transpose(a))
#相等与a.T

#rollaxis
a = np.arange(8).reshape(2, 2, 2)
print('原数组')
print(a)
print("获取其中的一个值")
print(np.where(a==6))
print(a[1, 1, 0])
print('\n')
#将轴2滚动到轴0
print('调用rollaxis函数')
b = np.rollaxis(a, 2, 0)
print(b)
print(np.where(b==6))
print('\n')
#将轴2滚动到轴1
print('调用rollaxis函数')
c = np.rollaxis(a, 2, 1)
print(c)
print(np.where(c==6))
print('\n')

# swapaxes用于交换数组的两个轴
a = np.arange(8).reshape(2, 2, 2)
print('原数组')
print(a)
print('\n')
print('调用swapaxes函数后的数组')
print(np.swapaxes(a, 2, 0))

#broadcast产生模仿广播的对象
x = np.array([[1], [2], [3]])
y = np.array([4, 5, 6])
#对y广播x
b = np.broadcast(x, y)
print('对y广播x：')
r, c = b.iters
print(next(r), next(c))
print(next(r), next(c))
print('\n')
print('广播对象的形状')
print(b.shape)
print('\n')
b = np.broadcast(x, y)
c = np.empty(b.shape)
print('手动使用 broadcast 将 x 与 y 相加：')
print(c.shape)
print('\n')
c.flat = [u + v for (u,v) in b]
print('调用flat函数')
print(c)
print('\n')
print('x + y的和')
print(x + y)

#broadcasat_to
a = np.arange(4).reshape(1, 4)
print('原数组：')
print(a)
print('\n')
print('调用broadcast_to函数之后')
print(np.broadcast_to(a, (4, 4)))

#expand_dims在指定位置插入新的轴来扩展数组形状
x = np.array(([1, 2], [3, 4]))
print('数组 x:')
print(x)
print('\n')
print('数组x和y的形状')
print(x.shape, y.shape)
print('\n')
y = np.expand_dims(x, axis=1)
print('在位置1插入轴之后的数组y:')
print(y)
print('\n')
print('x.ndim和y.ndim')
print(x.ndim, y.ndim)
print('\n')
print ('x.shape 和 y.shape：')
print (x.shape, y.shape)

#squeeze从给定数组的形状中删除一堆的条目
x = np.arange(9).reshape(1, 3, 3)
print('数组x:')
print(x)
print('\n')
y = np.squeeze(x)
print('数组y:')
print(y)
print('\n')
print('数组x和y的形状：')
print(x.shape, y.shape)

#concatenate用于沿指定轴连接相同形状的两个或多个数组
a = np.array([[1, 2], [3, 4]])
print('第一个数组：')
print(a)
print('\n')
b = np.array([[5, 6], [7, 8]])
print('第二个数组：')
print(b)
print('\n')
print('沿轴0连接两个数组')
print(np.concatenate((a, b)))
print('\n')
print('沿轴1连接两个数组')
print(np.concatenate((a, b), axis=1))

#stack用于沿新轴连接数组序列
a = np.array([[1, 2], [3, 4]])
print('第一个数组：')
print(a)
print('\n')
b = np.array([[5, 6], [7, 8]])
print('第二个数组：')
print(b)
print('\n')
print('沿轴0堆叠两个数组：')
print(np.stack((a, b), 0))
print('\n')
print('沿轴1堆叠两个数组：')
print(np.stack((a, b), 1))

#hstack通过水平堆叠来生成数组
a = np.array([[1, 2], [3, 4]])
print('第一个数组：')
print(a)
print('\n')
b = np.array([[5, 6], [7, 8]])
print(b)
print('\n')
print('水平堆叠：')
c = np.hstack((a,b))
print(c)
print('\n')

#vstack通过垂直堆叠来生成数组
print(b)
print('\n')
print('水平堆叠：')
c = np.vstack((a,b))
print(c)
print('\n')

#vstack通过垂直堆叠来生成数组


