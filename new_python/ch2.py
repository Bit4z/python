a=input("enter the string=")
li=[]
c=0
for i in a:
    c=0
    for j in a:
        if(i==j):
            c=c+1
    if i not in li:
        li.append(i)
        print("%c%d"%(i,c),end="")


