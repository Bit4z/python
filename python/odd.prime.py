l=[]
for j in range(0,100):
    c=0
    for i in range(2,j):
        if(j%i)==0:
            
            c=c+1
            
    
    if(c==0):
        l.append(j)
        #print(j)
print("The list of prime number")
print(l)
    
            
    
           
