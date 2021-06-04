import matplotlib.pyplot as mt
import numpy as np
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
mt.title("Sports watch Data")
mt.xlabel("Average pulse")
mt.ylabel("Calorie Bjurnage")
mt.plot(x,y)
#mt.grid(axis='x')
#mt.grid(axis='y')
mt.grid(color = 'green', linestyle = '--', linewidth = 0.5)
mt.show()
