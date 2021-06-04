tuple=('apple','mango',50,'tree',1,2,3,4,5)
list=['vegetable','papaya','grapes']
print(tuple)
print(tuple[0])
list[0]='orange'
print(list)
list=tuple
print(list)
list[0]='mango'
print(list)
list1=[]

for i in range(1,10):
    list1.append(i)
print(tuple(list1))

