import matplotlib.pyplot as mt
import numpy as np
xpoint=np.arange(0,7)

ypoint=np.array([3,8,1,10])
mt.plot(ypoint,linestyle="dotted")

y1 = np.array([3, 8, 1, 10])
y2 = np.array([6, 2, 7, 11])

mt.plot(y1)
mt.plot(y2)
font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':15}
mt.xlabel("X Axis",fontdict=font2)
mt.ylabel("Y Axis",fontdict=font2)
mt.title("Student Increasing Graph",fontdict=font1)      
mt.show()

