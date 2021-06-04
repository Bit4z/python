list=[[1,2,3],[4,5,6],[7,8,9]]
list1=[[4,5,6],[7,8,9],[1,2,3]]
result=[[0,0,0],[0,0,0],[0,0,0]]
print("first list matrix")
for i in range(len(list)):
    for j in range(len(list[i])):
        print(list[i][j],end="    ")
    print(end="\n")
print("second list matrix")   
for i in range(len(list1)):
    for j in range(len(list1[0])):
        print(list1[i][j],end="   ")
    print(end="\n")    
for i in range(len(list)):
    for j in range(len(list[0])):
        
        
        
        result[i][j]=list[i][j]+list1[i][j]
print("adition of two matrix")    
for i in range(len(result)):
    
    for j in range(len(result[0])):
        print(result[i][j],end="  ")
    print(end="\n")    
        
                   
                   
                   
                                
                             
                            
                        
                        
                              
