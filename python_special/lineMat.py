import matplotlib.pyplot as mt
import numpy as np
xpoint=np.arange(0,7)
#print(xpoint)
ypoint=np.array([3,8,1,10])
mt.plot(ypoint,linestyle="dotted")#linestyle can be written as ls. and dotted can be written as :.
#mt.plot(ypoint,linestyle="dashed",color='r',linewidth="20.7")#dashed can be written as --
y1 = np.array([3, 8, 1, 10])
y2 = np.array([6, 2, 7, 11])

mt.plot(y1)
mt.plot(y2)
font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':15}
mt.xlabel("X Axis",fontdict=font2)#this is a label is used to showing the information of x axis.
mt.ylabel("Y Axis",fontdict=font2)#this is a label is used to showing the information of y axis
mt.title("Student Increasing Graph",fontdict=font1)#loc='left'   is used to shift position of title.       
mt.show()

