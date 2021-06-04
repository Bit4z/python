import numpy as np
arr=np.array([1,2,3,4,7,8,9,10])
print(arr[1:4])
print(arr[-8:-2])
print(arr[1:5:2])#starting point,ending point,step point
print(arr[::2])#step pointing
print("<----------------------------------------------------------------------->")
print("                         2D Array Slicing")
arr1=np.array([[12,13,14,15],[17,18,19,20]])
print(arr1)
print("1,1:4=",arr1[1,1:4])
print("0:2,2=",arr1[0:2,2])
print("0:2,1:4=",arr1[0:2,1:4])
