import random
list=['paper','stone','scissor']
n=1
while(n==1):
    user2=input("enter your choice")
    user1=random.choice(list)
    print("computer choice",user1)
    print("your choice",user2)
    if(user1=='stone'):
        if(user1==user2):
            print("\ngame is tie")
        elif(user2=='scissor'):
            print("\nyou win")
        else:
            print("\nyou loss")

    elif(user1=='scissor'):
        if(user1==user2):
            print("\ngame tie")
        elif(user2=='paper'):
            print("\nyou loss")
        else:
            print("\nyou win")
    else:
        if(user1==user2):
            print("\ngame tie")
        elif(user1=='scissor'):
            print("you win")
        else:
            print("you loss")
            
print("\ngame is continue")
print("\nenter your choice")
                
        
