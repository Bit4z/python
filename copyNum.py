import numpy as np
a=np.array([1,2,3,4,7])
x=a.copy()
a[0]=10
print(a)

print(x)
y=a.view()
z=a.copy()
a[1]=20
print(a)
print(y)
print(z)
print(y.base)
print(z.base)
