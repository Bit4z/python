class rectangle:
    def __init__(self,l,b):
        self.l=4
        self.b=5
    def calculate(self):
        a=self.l*self.b
        return a
class area(rectangle):
    def __init__(self,l,b):
        super().__init__(l,b)
rect=area(7,8)
rt=rect.calculate()
print(rt)
