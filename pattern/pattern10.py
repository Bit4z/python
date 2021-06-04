m=int(input("enter the raw"))
for i in range(m,0,-1):
    for j in range(m):
        print(end="  ")
    for j in range(0,i):
        print("*",end=" ")
    print()
for i in range(m):
    for j in range(m):
        if(i>j):
            print(end=" ")
        else:
            print("*", end=" ")
    print()

    
        
