class area:
    def get(self):
        self.x=12
        self.y=3
    def show(self):
        self.a=self.x*self.y
        print(self.a)
class rect(area):
    def put(self):
        self.b=self.x+self.y
        print(self.b)
    
pt=rect()
pt.get()

pt.show()
pt.put()
    
