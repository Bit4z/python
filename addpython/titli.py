class restaurant:
    def r_name(self):
        print(end= "                  ")
        print("WELCOME TO Spicy RESTAURENT:-")
        
        print("     ")
        print("INFORMATION:-every item has 8%GST")
        print("                ")
    def name(self):
        self.name=input("Enter the name of The costumer=")
    def mat(self):
        b=[]
        self.total=0
        m=int(input("Enter the item number="))
        c=m
        for i in range(1,m+1):
            number=input("item {}=".format(i))
                                           
            b.append(number)
            rate=int(input("Enter the rate of this item="))
            self.total=self.total+rate

            self.GST=self.total*8/100
    def display(self):
        print("-----------------------------------------------------------------------------------------------")
        print("                   Generating Bill..")
        print("Name=",self.name)
        print("Total=",self.total)
        print("GST=",self.GST)
        print("the total amount with GST BILL=",self.total+self.GST)
        print("    ")
        print(end="                   ")
        print("THANK YOU  FOR  VISIT MY  RETAURENT")   
ob=restaurant()
ob.r_name()
ob.name()
ob.mat()
ob.display()
            
            
    
