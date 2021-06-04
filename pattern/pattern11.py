m=int(input("enter the raw"))
for i in range(0,m):
    for i in range(0,m-i-1):
        print(end="")
    for j in range(0,i+1):
        print("*",end=" ")
    print()
        
