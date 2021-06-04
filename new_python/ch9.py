k=0
list=[]
li=["1,2,3,4,5,6,7,8","2,4,7,9,10,11,12"]


for i in range(len(li[0])):
    
    for j in range(len(li[1])):
      
       
       if(li[k][i]==li[1][j]):
            if li[k][i] not in list:
                list.append(li[k][i])
print(list)
