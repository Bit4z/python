a=int(input("enter the nuber"));
print(a)
m=0
d=0
s=0
k=0
for i in range(a,1,-1):
  m=a%i
  if((m+i)==a):
      print(i,end=" ")
      if(m>1):
          k=m-1
      elif(m==2):
        
        print(1,end=" ")
        print(1)
      else:
         for j in range(2,m):
           m1=k%j
           if((j+m1)==k):
             print(j,end=" ")
             print(m1)
           else:
             s=k%j
             if((j+s+m1)==k):
               print(j,end=" ")
               print(d)
                  

                
                

            
                  
              
      print(m)
  else:
      d=a//i
      #print(d)
      if((m+i+d)==a):
          print(i,end=" ")
          print(d,end=" ")
          print(m)
          
      
      
