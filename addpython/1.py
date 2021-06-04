m=int(input("enter the number"))
k=m;
for i in range (m):
    for j in range(i):
        print("*",end="")
        k=k-1;
    print("\n")
