k=0
list=[]
li=[[1,3,4,7,13],[1,2,4,13,15]]


for i in range(len(li[0])):
    
    for j in range(len(li[1])):
      
       
       if(li[k][i]==li[1][j]):
            if li[k][i] not in list:
                list.append(li[k][i])

for i in range(len(list)):
    print(list[i].join(","))
