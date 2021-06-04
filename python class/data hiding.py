class myclass:
    __hidden=0
    def add(self,increment):
        __hidden=increment
        print(__hidden)
ob=myclass()
ob.add(5)
ob.add(3)
