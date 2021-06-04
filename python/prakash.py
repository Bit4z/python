l=[]
li=[]
n=int(input("enter the list item="))
for i in range(n):
    x=int(input())
    l.append(x)
print(l)
for i in l:
    if i not in li:
        li.append(i)
print(li)
