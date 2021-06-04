#from turtle import *
#forward(100)
from turtle import *
from random import randint
speed(50)
penup()
goto (-140,140)
for step in range(14):
    write(step,align='center')
    right(90)
    forward(10)
    pendown()
    forward(150)
    penup()
    backward(160)
    left(90)
    forward(20)
ada=turtle()
ada.color('red')
ada.shape('turtle')

ada.penup()
ada.goto(-160,100)
ada.pendown()
for turn in range(100):
    ada.forward(randint(1,5))
    bob.forward(randint(1,5))
    
    
    

