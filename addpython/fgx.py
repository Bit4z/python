# Hello World program in Py
import re
list=["dear","dog","dad","design","fghdemr"]
a=input("enter the string=")
for i in range(len(list)):
    mt=re.match(a,list[i])
    if(mt!=None):
        print(list[i])

   
