class A:
    a=10
    b=20
    def get(self):
        print("hey guys how are you")
class B(A):
    def set(self):
        print(self.a,self.b)
        self.get()
obj=B()
obj.set()


"""
# Python program to demonstrate private members 
# of the parent class 
class C(object): 
       def __init__(self): 
              self.c = 21
  
              # d is private instance variable  
              self.__d = 42    
class D(C): 
       def __init__(self): 
              self.e = 84
              C.__init__(self) 
object1 = D() 
  
# produces an error as d is private instance variable 
print(object1.d)                
"""
