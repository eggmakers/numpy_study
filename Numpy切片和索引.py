import numpy as np

a = np.arange(10)
s = slice(2, 7, 2)
print(a[s])

b = a[2:7:2]
print(b)

a = np.arange(10)
b = a[5]
print(b)

a = np.arange(10)
print(a[2:])

print(a[2:5])

a = np.array([[1,2,3],[3,4,5],[4,5,6]])
print(a[1:])
print(a[..., 1])
print(a[1, ...])
print(a[..., 1:])