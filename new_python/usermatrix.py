mat=[]
k=0
c=0
n=int(input("enter the raw="))
m=int(input("enter the collunm="))
for i in range(n):
    li=[]
    k=0
    for j in range(m):
       li.append(k)
       k=k+c
       
    mat.append(li)
    c=c+1
print(mat)
    
