list=[]
total=0
n=int(input("enter the number"))
z=int(n/2);
for i in range(0,n):
    k=int(input())
    list.append(k)
    
for i in range(0,len(list)):
    if(i<z):
        #x=len(list[i])
        x=list[i]
        
        while(x>9):
            x=int(x/10)
        total=(total*10)+x
        
    else:
        x=list[i]
        y=x%10
        total=(total*10)+y
        
        
if(total%11==0):
    print("OUI")
else:
    print("NON")
        
    
    
    
        
    
    
