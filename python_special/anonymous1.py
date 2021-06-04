#fun=lambda x:x*2
fun=lambda x:x+3
print(fun(4))
fun1=lambda a,b:a*b
print(fun1(7,8))
fun2=lambda x,y,z:x+y+z
print(fun2(1,2,3))
def fun3(x):
    return lambda y:x*y
fun4=fun3(2)
print("fun=",fun4(8))


func=lambda *x:x[0]+x[1]+x[2]+x[3]
list=[1,2,3,4]
print(func(1,2,3,4))
#print(func(list))

func1=lambda *x:x
print(func1(list))
(lambda x: x*x)(5)


def cub(i):
    return (i**3)
l=[1,2,3,4]
print(map(cub,l))

def vob(a):
    l=['a','i','o','u','e']
    if a in l:
        return True
    else:
        return False
l1=['z','i','y','a','u','l','h','a','q']
print(list(filter(vob,l1)))

li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]


def sum1(arg):
    
        if(arg>4):
            return True
        else:
            return False
list1=[1,2,3,7,8,9,10]
print(list(filter(sum1,list1)))





def ev(x):
    if x%2==0:
        return True
    else:
        return False
li=[1,2,3,4,7,8,9,0]
print(list(filter(ev,li)))


  
final_list = list(filter(lambda x: (x%2 != 0) , li)) 
print(final_list)





sequences = [10,2,8,7,5,4,3,11,0, 1]
filtered_result = filter (lambda x: x > 4, sequences) 
print(list(filtered_result))


sequences = [10,2,8,7,5,4,3,11,0, 1]
filtered_result = map (lambda x: x+3, sequences) 
print(list(filtered_result))
