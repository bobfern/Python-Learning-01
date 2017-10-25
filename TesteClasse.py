class teste():
    __cont = 0

    def __init__(self):

        self.__attr1 = 1
        self.__attr2 = 2
        teste.__cont += 1


    @property
    def attr1(self):
        return self.__attr1

    @attr1.setter
    def attr1(self,attr1value):
        self.__attr1 = attr1value
        # return self.__attr1

    def getAttr2 (self):
        return (self.__attr2)

    def getCont(self):
        return teste.__cont


testeobj = teste()
testeobj.attr1 = 5
testeobj._teste__attr1 = 6
print ('01> ' , testeobj._teste__attr1)

testeobj2 = teste()
print ('02> ' ,  testeobj2._teste__cont)
print ('03> ' ,  testeobj2.attr1)
print ('04> ', type(testeobj2.attr1))
