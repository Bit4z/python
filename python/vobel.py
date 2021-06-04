b=[]
v="AIOUEaioue"
a=input("enter the string")
for i in v:
    cout=0
    for j in range(len(a)):
        if(i==a[j]):
            cout+=1
    if([i,cout]) not in b:

        b.append([i,cout])
print(b)
