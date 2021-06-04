a=int(input("enter the raw"))
b=int(input("enter the collunm"))
k=1
for i in range(a):
    for j in  range(b,i):
        print("#",end=" ")
        k=k+1
    print(end="\n")    
