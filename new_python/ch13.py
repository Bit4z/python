lis=[]
n=int(input("enter the length"))
for i in range(0,(n-1)):
    k=int(input())
    lis.append(k)
    if(i==0):
        x=k
    elif(x>k):
        x=k
for i in range(0,(n-1)):
    if(k in lis):
        k=k+1
    else:
        print("missing number",k)
        break

