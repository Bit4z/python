class human:
    fp='priti'
    def __init__(self,eyes,foot):
        self.e=eyes
        self.f=foot
    def details(self,name,bldgroup):
        self.n=name
        self.b=bldgroup
    def display(self):
        print("human eyes=",self.e)
        print("human foot=",self.f)
        print("human name=",self.n)
        print("human bnloodgroupo=",self.b)
    def is_fp(cls):
        print("this is under=",cls.fp)
        return cls.fp
        
class woman(human):
    def __init__(self,eyes,foot):
        super().__init__(eyes,foot)
    def disp(self,name,bldgroup):
        self.n=name
        self.b=bldgroup
        print("woman eyes=",self.e)
        print("woman foot=",self.f)
        print("woman name=",self.n)
        print("woman bloodgroup=",self.b)
hu=human(2,2)
hu.details("ziyaulhaq","o+")
hu.display()
wo=woman(2,2)
wo.disp("snhivangi","a+")

print(human.fp)
print(Mobile.is_fp(Mobile))


    
