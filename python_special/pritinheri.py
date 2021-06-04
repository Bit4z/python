class Father:
    money = 1000
    def __init__(self , m):
        self.mother = m
        print('mother', self.mother)
        print("father class constructor")
    def showF(self):
        print("father class instance method")

    @classmethod
    def money(cls):
        
        print('father class classmethod')
        print('money' , cls.money)

    @staticmethod
    def statf():
        a = 10
        print('father class static method', a)


class Son(Father):
    price =500
    def __init__(self,m, f):
        super().__init__(m)
        self.father =f
        print('father', self.father)
        print("son class constructor")
    def showS(self):
        print("son class instance method")
    
    @classmethod
    def price(cls):
        
        print('son class classmethod')
        print('money' , cls.price)

    @staticmethod
    def stat():
        b = 10
        print('son class static method', b)


class Grandson(Son):
    want = 400
    def __init__(self,m ,f , s ):
        super().__init__(m,f)
        self.sister =s
        print('sister', self.sister)
        print("father class constructor")
    def shows(self):
        print("father class instance method")

    @classmethod
    def want(cls):
        print('grandson class classmethod')
        print('money' , cls.want)

    @staticmethod
    def statg():
        c= 10
        print('grandson class static method', c)


s = Grandson("uma" , "rajeev", "lovely")
s.showF()
s.showS()
s.shows()
s.money()
s.price()
s.want()
s.statf()
s.stat()
s.statg()
