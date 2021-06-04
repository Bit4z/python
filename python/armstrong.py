n=int(input("enter the number"))
t=n
sum=0
c=0
while(n>0):
    n=n//10
    c=c+1
n=t
while(n>0):
    r=n%10
    sum=sum+r**c
    n=int(n/10)
if(t==sum):
    print("armstrong")
else:
    print("not armstrong")
