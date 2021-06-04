import pandas as pd
a=[1,7,2]
myvar=pd.Series(a)
print(myvar)

print(myvar[0])#return the value of series the value first index is 0;


#pandas set index

myvar1=pd.Series(a,index=["x","y","z"])
print(myvar1)


#Keys/Values Objects as Series
Calories={"day1":420,"day2":230,"days3":390}
myvar=pd.Series(Calories)
print(myvar)

myvar=pd.Series(Calories, index=["day1","day2"])
print(myvar)


#DataFrams
data={"calories":[420,380,390],"duration":[30,40,70]}
myvar=pd.DataFrame(data)
print("this is data fram")
print(myvar)


#return DataFrame row by loc
print("return 1 raw")
print(myvar.loc[0])#return raw 1
print("return 2 rows")
print(myvar.loc[[0,1]])#return two rows

df=pd.DataFrame(data, index=["Day1","Day2","Day3"])
print(df)
print(df.loc["Day1"])
                             

