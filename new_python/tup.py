tup=(1,2,3,4,5,6,7,8,9,'apple')
print(tup)
for i in range(3,5):
    print(tup[i])
my=2,"hello",3.6
print(my)
a,b,c=my
print(c)
my_tuple=([0,1,2],[3,4,5,6],[7,8,9])
print(my_tuple)
for i in range(len(my_tuple)):
    for j in range(len(my_tuple[i])):
        print(my_tuple[i][j], end=" ")
    print(" ")
Tuple=('p','r','o','m','m','i','n','g')
print(Tuple[1:5])
list=[]
print(Tuple[:])
print(Tuple[-3:-1])
print(Tuple+tup)
list.insert(3,1)
print("list=",list)
list.clear()
print(list)


