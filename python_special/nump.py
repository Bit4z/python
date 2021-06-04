import numpy as np
print(np.__version__)
arr = np.array([1, 2, 3, 4, 5])

print(arr)

print(type(arr))
arr = np.array((1, 2, 3, 4, 5))

print(arr)
print(type(arr))
a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(arr)

print(arr.shape)
print(d.shape)

#arr=np.ndim(4)
print(arr)
print(
