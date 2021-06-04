def sum():
    print("this sum not contain any argument")
def sum1(a,b):
    c=a+b
    print("sum is=",c)
def sum2(a,b):
    return a+b
sum()
sum1(2,3)
print(sum2(7,8))
def temp(list):
    print(list)
list=[1,2,3,4]
temp(list)

#required arguments
def func(name):
    print("hi",name)
name="ziyaulhaq khan"
func(name)
def simple_interest(p,t,r):    
    return (p*t*r)/100    
p = float(input("Enter the principle amount? "))    
r = float(input("Enter the rate of interest? "))    
t = float(input("Enter the time in years? "))    
print("Simple Interest: ",simple_interest(p,r,t))

#default arguement
def func1(name,age=30):
    print("name=",name,"age=",age)
name="Farman"
age=70
func1(name,age)
func1(name)

#Variable-length Arguments (*args) and element type of tuple

def func2(*arg):
    print(arg)
func2(1,2,3,4)
#element type of  dictionary
def food(**kwargs):  
    print(kwargs)  
food(a="Apple")  
food(fruits="Orange", Vagitables="Carrot")

def fung(*args):
    sum=0
    for i in args:
        sum=sum+i
    print("sum=",sum)
fung(7,8,9,1)
