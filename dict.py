#d={x:(x*x) for x in range(1,10)}
dic={'name':"Ziyaulhaq", 'course':"mca" ,'age':30,'desig':"Ziyaulhaq",'colors':['red','orange','pink']}
for k,v in dic.items():
    print("keys=",k,"values=",v)
print("length is dictionary=",len(dic))
print(dic.keys())
print(dic.values())
#print(d)
d={}
n=int(input("eneter the element"))
i=0
while(i!=n):
    #l=[int(i) for i in input("enter the element:")]
    x=input("enter the key")
    d[x]=input("enter value")
    i=i+1
    
print(d)
l=[int(i) for i in input("enter the element:").split()]
print(l)
l1=[1,2,3,4]
d1={}
d1.fromkeys(l1)
print(d1)
keys = {'a', 'e', 'i', 'o', 'u' }

vowels = dict.fromkeys(keys)
print(vowels)
