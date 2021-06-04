import matplotlib.pyplot as mt
import numpy as np
#2 collmn plot
x=np.array([0,1,2,3])
y=np.array([3,8,1,10])
#plot1
mt.subplot(1,2,1)#the figure has 1 row, 2 columns, and this plot is the first plot.
mt.title("Sales")
mt.plot(x,y)

#plot2
x1=np.array([7,8,9,10])
y1=np.array([10,20,30,40])
mt.subplot(1,2,2)
mt.title("Income")
mt.plot(x1,y1)
mt.suptitle("My Shope")
mt.show()

#2 raw plot
x2=np.array([0,1,2,3])
y2=np.array([3,7,4,8])
#plot1
mt.subplot(2,1,1)
mt.plot(x2,y2)
#plot2
mt.subplot(2,1,2)
mt.plot(x2,y2)

mt.show()
