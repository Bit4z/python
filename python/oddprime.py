m=int(input("enter the lowe tem"))
n=int(input("enter the upper term"))
for j in range(m,n+1):
    c=0;
    for i in range(2,j):
        if(j%i)==0:
            c=c+1
            #break
    if(c==0):
        #i=i+1
        print(j)
        #j=j+1
            
