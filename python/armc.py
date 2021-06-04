c n=int(input("enter the number"))
temp=n
sum=0
r=0
c=0
while(n>0):
    n=n//10
    c=c+1

n=temp
while(n>0):
    r=n%10
    sum=sum+(r**c)
    n=n//10
if(sum==temp):
    print("armstrong")
else:
    print("not armstrong")
    
    
    
    
            
