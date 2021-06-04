class ractangle:
    def __init__(self):
        self.l=10
        self.b=20
    def calculate(self):
        A=self.l*self.b
        return A
class Area(ractangle):
    def __init__(self):
        super().__init__()
rect=Area()
c=rect.calculate()
print(c)
