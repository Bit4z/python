d={}

while True:

  c=int(input("Press 1 for input or press 2 fo exit:"))

  if c==1:

    Id=int(input("Enter key:"))

    n=input("Enter name:")

    age=int(input("Enter age:"))

    d[Id]=[n,age]

  elif c==2:

    break

  else:

    print("Wrong choice")
print(d)

Id=int(input("Enter the Id you want to search:"))

d.get(Id,"Id not Found")






