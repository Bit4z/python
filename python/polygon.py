class polygon:
    def __init__(self,n):
        self.list=[]
        for i in range(n):
            a=int(input("enter the value="))
            self.list.append(a)
class rectangle(polygon):
    def __init__(self):
        super().__init__(2)
        print("this is area of rectangle")
        print(self.list[0]*self.list[1])
class tringle(polygon):
    def __init__(self):
        super().__init__(3)
        print("this is area of triangle")
        self.s=(self.list[0]*self.list[1]*self.list[2])/2
        self.d=(self.s*((self.s-self.list[0])+(self.s-self.list[1])+(self.s-self.list[2])))*0.5
        print(self.d)
pt=tringle()
rt=rectangle()
    

