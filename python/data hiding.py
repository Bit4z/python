class my_class:
    __hiddenvariable=0
    def add(self,increment):
        self.__hiddenvariable=increment
        print(self.__hiddenvariable)
myobject=my_class()
myobject.add(2)
#myobject.add(5)


