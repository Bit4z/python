import numpy as np
arr=np.array([[1,2,3],[7,8,9]])
#print(arr)
for x in arr:
    for y in x:
        print(y)
print("                 3D Array")
arr1=np.array([[[1,2,3],[7,8,9],[20,21,22]],[[10,11,12],[13,17,18],[23,27,28]]])
print(arr1)
print("Array shape=",arr1.shape)
print("traverse 3D Array for loop")
for x in arr1:
    for y in x:
        print(y)
        for z in y:
            print(z)
print("this is special techniq traverse 3D Array elements")
for x in np.nditer(arr1):
    print(x)
print("this is 2D traversing elements")
for x in np.nditer(arr):
    print(x)
