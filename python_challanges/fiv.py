a=0
b=1
n=0
print(f'{a},{b},',end="")
while(n<=100):
    sum=a+b
    print(f'{sum},',end="")
    a=b
    b=sum
    n=n+1
    
