import pandas as pd
print(pd.__version__)
mydataset={'cars':["BMW","VOLVO","FOED"],'passing':[3,7,2]}
myvar=pd.DataFrame(mydataset)
print(myvar)
