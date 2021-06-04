a=int(input("enter the raw"))
b=int(input("enter the collunm"))
k=b
for i in range(a):
    for j in  range(b):
        print(k,end=" ")
        k=k-1
    print(end="\n")
    k=b
