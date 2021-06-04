class restaurant:
    def r_name(self):
        print(end= "                  ")
        print("WELCOME TO Spicy RESTAURENT:-")
        print("     ")
       # print("gla university retsaurent")
        print("INFORMATION:-every item has 8%GST")
        print("                ")
    def name(self):
        try:
            
            self.name=input("enter the name of costumer=")
            except(Exception):
                print(e)
    def mat(self):
        self.total=0
        self.b=[]
        self.m=int(input("enter the item number="))
        for i in range(1,self.m+1):
            #b[i]=input("item=")
            number=input("item {}=".format(i))
                                           
            self.b.append(number)
            self.rate=int(input("enter the rate of in this item="))
            self.total=self.total+self.rate
        print("loop=",self.b)
    def display(self):
        print("name=",self.name)
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
            
            
    
