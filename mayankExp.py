import numpy as np

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(len(arr))
for i in range(len(arr)):
    for j in range(len(arr[i])):
        print(arr[i,i:j])

            
    
#print(arr[1, 1:4])
