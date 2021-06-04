
l=[]
l1=[]
c=0
n=int(input("enter the number"))
for i in range(n):
    x=int(input())
    l.append(x)
    if(x>=0):
        l1.append(x)

       
for i in range(len(l1)):
    for j in range(len(l1)):
        if(i!=j):
            sum=l1[i]+l1[j]
            a=- sum
            if a in l:
                print("True")
                c=1
                break
    if(c==1):
        break
if(c==0):
    print("False")
            
        
