l=[[1,12,3,4],[7,8,19,10]]
k=0
for i in range(len(l)):
    for j in l[i]:
        if(j>k):
            k=j
print(k) 
        
