l=[" ","!","@","#","%","^","&","*",".","_","1","2","3","4","5","6","7","8","9","0"]
str=input("enter the string=")
for i in str:
    if i not in l:
        print(i,end=" ")
