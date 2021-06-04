import matplotlib.pyplot as mt
import numpy as np
x=np.array([0,1,2,3])
y=np.array([1,13,3,8])
#plot1
mt.subplot(2,3,1)
mt.plot(x,y)
 #plot2
mt.subplot(2,3,2)
mt.plot(x,y)
#plot3
mt.subplot(2,3,3)
mt.plot(x,y)
#plot4
mt.subplot(2,3,4)
mt.plot(x,y)
#plot5
mt.subplot(2,3,6)
mt.plot(x,y)
#plot6
mt.subplot(2,3,5)
mt.plot(x,y)
mt.show()
