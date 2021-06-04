b=[]
a=input("enter the string=")
c=a
for i in c:
    
    cout=0
    for j in range(len(a)):
        if(i==a[j]):
            cout+=1
    if([i,cout]) not in b:
        b.append([i,cout])
print(b)        

            
