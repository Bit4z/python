from functools import reduce
sequences = [1,2,3,4,5]
product = reduce (lambda x, y: x*y, sequences)
print(product)

import functools  
  
# initializing list  
lis = [ 1 , 3, 5, 6, 2, ]  
  
# using reduce to compute maximum element from list  
print ("The maximum element of the list is : ",end="")  
print (functools.reduce(lambda a,b : a if a > b else b,lis)) 
