a="AweSome Bhai You arE sO gOOD";
print(a)
b=a.split()
ls1=[]
ls=[]
x=" "
y=ord(x)
print(y)
for i in range(len(b)-1,-1,-1):
    ls1.append(b[i])
for i in ls1:
    x+=i;
    x+=" "
for i in x:
    
    c=ord(i)
   
    if(c>=97 and c<=122):
        c=c-32;
        ls.append(chr(c))
    elif(c<=96 and c>=65):
        c=c+32
        ls.append(chr(c))
    elif(c==32):
        ls.append(chr(c))
        
       
       
print(ls1)       
print(''.join(ls))
print("string=",x)

    
