m=int(input("enter the raw"))
for i in range(1,m+1):
    for j in range(i):
        print(i,end=" ")
    print("\n")
for i in range(m,0,-1):
    for j in range(1,i+1):
        print(i,end=" ")
    print("\n")
