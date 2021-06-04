class MBA:
    
    
    def name(self):
        self.student=input("enter the name=")
    def marks(abc):
        abc.bc=int(input("enter the marks of BC="))
        abc.me=int(input("enter the marks of ME="))
        abc.be=int(input("enter the maerks of BE="))
        abc.cam=int(input("enter the marks oF CAM="))
            
        abc.qt=int(input("enter the marks of QT="))
        abc.ppm=int(input("enter the marks of PPM="))
        abc.ma=int(input("enter the marks of MA="))
        abc.fa=int(input("enter the ,marks of FA="))
    def percentage(abc):
        
        
               
        abc.total=(abc.bc+abc.me+abc.be+abc.cam+abc.qt+abc.ppm+abc.ma+abc.fa)*100/800

    def display(abc):
        print("student name=",abc.student)
        print("BC=",abc.bc)
        print("ME=",abc.me)
        print("BE=",abc.be)
        print("CAM=",abc.cam)
        print("QT=",abc.qt)
        print("PPM=",abc.ppm)
        print("MA=",abc.ma)
        print("FA=",abc.fa)


        print("total=",abc.total)

A=MBA()
A.name()
A.marks()
A.percentage()               
A.display()
               

            
               
