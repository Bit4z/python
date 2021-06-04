b=input("enter the string=")
a=len(b)
if(a>2):
    
    c=b[:2]+b[-2:]
    print(c)
else:
    print("string has less than two character")
    print(" ")
    print("so string is the empty")
