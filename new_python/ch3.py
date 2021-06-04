def FirstFactorial(num):
    sum=1
    for i in range(1,num+1):
        sum=sum*i

    return sum
    
n=int(input("enter the factorial number"))
print(FirstFactorial(n))  


  
