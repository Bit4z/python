n=int(input("enter the value"))
k=n-1
for i in range(n):
    for j in range(n):
        if(j<k):
            print(" ",end="")
        
        else:
            print("*",end="")
    k=k-1
    print("")
    
