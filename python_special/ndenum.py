import numpy as np
arr=np.array([[1,2,3,4,7,8,9,10],[11,12,13,14,17,18,19,20]])
print(arr)
print("The enumeration list:")
for idx,x in np.ndenumerate(arr):
    print(idx,x)
