n=int(input("enter the value of n"))
i=2
c=0
while(i<n):
    if(n%i)==0:
        c=c+1
        i=i+1
    break
elif(c==0):
    print("prime")
else:
    print("not prime")
        
