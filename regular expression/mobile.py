import re
a=["9536209312","8936548757","9856437658","8694645443","9536278342","78645329"]
for i in range(len(a)):
    mt=re.match('[9]\d{9}',a[i])
    if(mt!=None):
        print(mt.group())
    
        
               
   
