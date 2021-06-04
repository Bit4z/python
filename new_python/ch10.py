list=[['1','3','4','7','13'],['1','2','4','13','15']]
li=[]
for i in range(len(list[0])):
    for j in range(len(list[1])):
        if(list[0][i]==list[1][j]):
            if list[0][i] not in li:
                li.append(list[1][j])
                #print(list[1][j])
list1=[['1','3','9','10','17','18'],['1','4','9','10']]
li1=[]
for i in range(len(list1[0])):
    for j in range(len(list1[1])):
        if(list1[0][i]==list1[1][j]):
            if list[0][i] not in li1:
                li1.append(list1[1][j])
s=","
s=s.join(li)
print(s)

s1=","
s1=s1.join(li1)
print(s1)
        
        
        
        
                   

