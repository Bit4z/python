
m=int(input("enter the value of  first interval="))
n=int(input("enter the value of last interval="))
for i in range(m,n+1):
    c=0
    for j in range(2,i):
        if(i%j==0):
            c=c+1
    if(c==0):
        print(i)
        #i=i+1
