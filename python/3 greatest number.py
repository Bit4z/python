a=int(input("enter the value of a"))
b=int(input("enter the value of b"))
c=int(input("enter the value of c"))
if(a>=b and b>=c):
    print("a is greatest")
elif(b>=c and b>=a):
    print("b is greatest")
else:
    print("greatest is c")
