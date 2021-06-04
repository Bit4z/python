list1=[]
list=[]



n=int(input("enter the value of item"))
for i in range(n):
    k=int(input())
    list1.append(k)
#print(list1)
for i in range(n):
    y=list1[i]
    for j in range(i,i+2):
        
        if(y<list1[i]):
            y=list1[i]
            #x=y
    print(y)
print(list)
    
            
