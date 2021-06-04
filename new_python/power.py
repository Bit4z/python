n=int(input("enter the number="))
while(n>1):
    if(n%2==0):
        n=n/2;
    else:
        print("this is not a power of 2")
        break
if(n==1):
    print("this is a power of 2")
