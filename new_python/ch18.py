s=input("enter the string=")
s1=""
c=0
l=[]
for i in s:
    if i not in s1:
        s1=s1+i
    else:
        l.append(s1)
        s1=s1+i
        
        
        v=s1.index(i)
        x=s1[:v+1]
        l.append(x)
        y=s1[v+1:]
        s1=y
        
l.append(s1)
k=len(l[0])
m=l[0]
for j in l:
    if(len(j)>k or len(j)==k):
        k=len(j)
        m=j
        
       
    
    

print(m,",",k)
        
        
        
