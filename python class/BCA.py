class BCA:
    def name_1(self):
        self.name=input("enter the name=")
    def roll_no(self):
        self.roll=int(input("enter the roll number="))
    def marks(self):
        self.coa=int(input("enter the marks of coa="))
        self.c=int(input("ente the marks of c++"))
        self.python=int(input("enter the marks of python="))
        self.descrete=int(input("enter the mjarks of descrete="))
        self.evs=int(input("enter the marks of evs="))
HHHHHHHHHHHHH    def total(self):
        self.total=(self.coa+self.c+self.python+self.descrete+self.evs)*100/75
    def display(self):
        print("name=",self.name)
        print("roll number=",self.roll)
        print("coa=",self.coa)
        print("c++=",self.c)
        print("python=",self.python)
        print("descrete mathmatic=",self.descrete)
        print("evs=",self.evs)
        print("total=",self.total)
A=BCA()
A.name_1()
A.roll_no()
A.marks()
A.total()

A.display()
              
    
