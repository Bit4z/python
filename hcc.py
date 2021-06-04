s=input()
p=input()
j=1
k=0
l=[]
for i in range(len(s)):
    j=j+1
    if(s[i:j]) in p:
        l.append(k)
        k=k+1
print(l)
