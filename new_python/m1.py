#a="i love dogs"
a=input("enter the string=")
c=0
l=['1','2','3','4','5','6','7','8','9','0','~','@','#','$','%','^','&','*','+','_','-','!','?','/','<','>','=','|',' ']
b=a.split()
for i in b:
    k=0
    for j in i:
        if j not in l:
            k=k+1
    if(k>c):
        c=k
        d=i
print(d)            
