a=input()
ls=[]
str=""
for i in a:
    b=ord(i)
    if(b>=97 and b<=122):
        b=b-32
        str+=chr(b)
    elif(b<=96 and b>=65):
        b=b+32
        str+=chr(b)
    elif(b==32):
        str+=chr(b)
        
print(str)
        
        
         
    
        
   
        
        



        
    
                    
    
