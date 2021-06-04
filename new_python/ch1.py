a="AAAAABBBBCCDE"
#a=input("enter the number")
c=0
li=[]
for i in a:
    c=0
    for j in a:
        if(i==j):
            c=c+1
    if i not in li:
        li.append(i)
        print("%c=%d"%(i,c))
    
        
    
    
