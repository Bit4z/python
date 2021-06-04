list=[]

swap=0
c=1
x=0
y=0
z=0
sum=0

n=int(input("enter the array size"))
k=int(input("swap number"))
for i in range(n):
    m=int(input())
    if(m%2!=0 and c<=k):
        if(swap==0):
            swap=m
            x=i
            
        else:
            swap=m
            result=list.pop(i-1)
            list.append(swap)
            list.append(result)
            continue
    list.append(m)
print(list)
for i in list:
    if(i%2!=0):
        sum=sum+i
        if(sum%2==0):
            sum=0
            z=z+1
        
    else:
        z=z+1
print("total sub array=",z)

    
            
            
            
