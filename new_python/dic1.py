student={'name':'ziyaulhaq','age':20,'course':'BCA'}
std={}
students=student.copy()
for i in student.values():
    print(i)
    #print("%s=%s"%(i,student[i]))
dic={}
n=int(input("enter the number="))
for i in range(1,n):
    dic[i]=i*i
print(dic)
sq={x:x*x for x in range(10,20)}
    
print(sq)
print("enter the run time dictionary")
for z in range(n):
    j=input("enter the key=")
    k=input("enter the values=")
    std[j]=k
print(std)
    
