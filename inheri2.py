
class Base1(object):
    a=10
    def __init__(self): 
        self.str1 = "Geek1"
        print("Base1")
    def check(self):
        print("bas1 class")
  
class Base2(object):
    b=20
    def __init__(self): 
        self.str2 = "Geek2"        
        print("Base2")
    def check1(self):
        print("bas2 class")




    
  
class Derived(Base1, Base2): 
    def __init__(self): 
          
        # Calling constructors of Base1 
        # and Base2 classes 
        Base1.__init__(self) 
        Base2.__init__(self)
        self.check()
        self.check1()
        print("Derived") 
          
    def printStrs(self): 
        print(self.a, self.b) 
         
  
ob = Derived() 
ob.printStrs() 

