n=int(input("enter the value"))
a=[]
for i in range(n):
    num=int(input())
    a.append(num)
for i in range(n):
    sum=1
    for j in range(n):
        if(a[i]!=a[j]):
            sum=sum*a[j]
    print(sum)

