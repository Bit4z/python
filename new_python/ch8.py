stri=input("enter the input=")
ls=[]
for i in stri:
    a=ord(i)
    a=a+1
    ls.append(chr(a))
print('# '.join(ls))
