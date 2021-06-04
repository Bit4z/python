class Mobile:
    fp ='priti'
    def __init__(self , mobile, camara):
        self.mob = mobile
        self.cam = camara
    @classmethod
    def is_fp(cls):
        #print(cls.fp)
        return cls.fp
    def show(self):
        print('mobile is:' , self.mob)
        print('camara is ' , self.cam)


realme = Mobile('redmi' , 'sony')
realme.show()
print(Mobile.is_fp())
print(Mobile.fp)
print(type(Mobile.fp))
Mobile.fp ='no'
print(Mobile.fp)
