import pandas as pd
import numpy as np
ls=[x for x in input("enter the students").split()]
Uid=[y for y in input("enter the uid").split()]
myvar=pd.Series(ls,index=Uid)
#myvar=pd.Series(ls,index=["20MCA1307","20MCA1300","20MCA1234"])
print(myvar)
s=pd.Series(np.arange(4),index=["Ziya","Navi","Shivang","Updesh"])
print(s)
d=dict(zip(Uid,ls))#convert in dictionary
print(d)
sr=pd.Series(4,index=range(3))
print(sr)
for i in ls:
    print(ls)


# DataFrame

df=pd.DataFrame(["MCA","BCA","BTECH","MTECH"],index=range(4),columns=["Students"])
print("DataFrame is")
print(df)
print("The shape is=",df.shape)
print("The colluns is=",df.columns)
df=pd.DataFrame([range(10),range(0,20,2)])
print(df)
dft=pd.DataFrame([['Rydhm','20MCA2020'],['ziya','20MCA1307']],columns=['Name','Uid'])
print(dft)
