 
def compute_gcd(x, y):

   while(y):
       x, y = y, x % y
   print("The GCD=",x)
   return x

def compute_lcm(x, y):
   lcm = (x*y)//compute_gcd(x,y)
   return lcm

num1 = int(input("enter the first number="))
num2 = int(input("enter the 2nd number=")) 

print("The L.C.M. is", compute_lcm(num1, num2))
