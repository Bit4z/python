import matplotlib.pyplot as mt
import numpy as np
x=np.array([0,1,2,3])
y=np.array([10,20,30,40])
sizes=np.array([110,730,240,470])
colors = np.array(["red","green","blue","yellow"])
mt.scatter(x,y,  color="hotpink",s=sizes,alpha=0.9)
x1=np.array([12,8,9,4])
y1=np.array([3,7,4,10])
mt.scatter(x1,y1, c=colors,cmap='viridis',alpha=0.4)
mt.colorbar()#it is used for showing colorbar
mt.show()

