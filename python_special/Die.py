import plotly.express as exp
import randint from random
class Die:
    def __init__(self,sides):
        self.sides=sides
    def roll(self):
        return randint(1,self.sides)
die=Die(6)
l=[]
for r in range(100):
    l.append(die.roll())
f=[]
for v in range(1,die.sides):
    f.append(l.count(v))
	
