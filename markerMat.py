import matplotlib.pyplot as mt
import numpy as np
xpoint=np.array([3,9,7])
ypoint=np.array([3,8,1,10])
#mt.plot(ypoint,marker='o')

#mt.plot(ypoint,marker='*', ms=20,mec='r')#ms indicate marker size and mec indicatete marker degree color
mt.plot(ypoint,marker='<', ms=20, mfc='r')#mfc indicate facecolor
#mt.plot(ypoint,'o:r')

mt.show()
