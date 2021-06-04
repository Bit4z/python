import numpy as np
arr=np.array([1,2,3,4],ndmin=7)
print("Number of diamensions:",arr)

print("<----------------------------------------------------------------------------->")
print("                         Array accessing elements")
arr=np.arange(10)
for i in range(10):
    print(arr[i])
    print("sum=",arr[i]+arr[i])
print("                       Access 2D array")
arr2=np.array([[1,2,3,4],[7,8,9,10]])
print(len(arr2))
print("2d array elements:")
for i in range(len(arr2)):
    for j in range(len(arr2[i])):
        print(arr2[i][j])
print("<------------------------------------------------------------------------------->")
print("                        Access 3D array elements")
arr3=np.array([[[12,13,14,17],[18,19,20,21]],[[22,23,24,27],[28,29,30,31]]])
print(arr3)
                   
                   
print(arr3[0,1,2])
print(arr3[0,2,1])
