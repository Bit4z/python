class polygon:
    def __init__(self,n):
        self.s=[]
        for i in range(n):
            a=int(input("enter the number="))
            self.s.append(a)
class rectangle(polygon):
    def __init__(self):
        super().__init__(2)
    def area(self):
        print(self.s[0]*self.s[1])
class triangle(polygon):
    def __init__(self):
        super().__init__(3)
    def area(self):
        s1=(self.s[0]+self.s[1]+self.s[2])/2
        print((s1*(s1-self.s[0])*(s1-s.self[1])*(s1-s.self[2])**0.5))


rect=rectangle()
rect.area()
tr=triangle()
tr.area()
              
            
