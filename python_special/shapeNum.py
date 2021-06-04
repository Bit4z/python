import numpy as np
arr=np.array([1,2,3,4,7,8,9])
print(arr.shape)
arr1=np.array([[10,11,12,13,14],[17,18,19,20,21]])
arr2=arr1.copy()
print(arr1.shape)
arr3=np.array([1,2,3,4,7,8,9,10],ndmin=4)
print(arr3)
print(arr3.shape)
