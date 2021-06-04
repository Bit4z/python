import numpy as np
a=np.arange(10)#predifine way
print(a)
b=np.array([10,20,30,40])
print(b)
l=[]
n=int(input("enter the number="))
for i in range(n):
    x=int(input("the number="))
    l.append(x)
print(l)
print(type(b))

#0D array
arr=np.array(42)
print("This is 0D array=",arr)
#1D array
arr1=np.array([12,13,14,17])
print("This is 1D Array=",arr1)

arr2=np.array([[1,2,3,4],[10,11,12,13]])
print("This is 2D Array=",arr2)
arr3=np.array([[[1,2,3,4],[7,8,9,10]],[[11,12,13,14],[17,18,19,20]]])

print("This is 3D Array=",arr3)
print("This is 0D",arr.ndim)
print("This is 1D",arr1.ndim)
print("This is 2D",arr2.ndim)
print("This is 3d",arr3.ndim)
