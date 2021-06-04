m=int(input("enter the lower term"))
n=int(input("enter the upper term"))
k=n
for j in range(m,n+1):
    c=0;
    for i in range(2,j):
        if(j%i)==0:
            c=c+1
    if(c==0):
        if(k==n):
           k=j
           
        elif(k+2==j):
            
            print("twin number",k,",",j)
            k=j
        
            
        else:
            if(j%2!=0):
                k=j
        
            
