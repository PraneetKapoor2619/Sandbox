class Wrestler:

        def __init__(self):
                self.__name = ""

        @property
        def name(self):
                return self.__name
        
        @name.setter
        def name(self, name):
                self.__name = name
        
        @name.deleter
        def name(self):
                del(self.__name)
        
if __name__ == "__main__" :
        wObj1 = Wrestler
        wObj1.name = "Praneet"
        print(wObj1.name)
        del(wObj1.name)
        print(wObj1.name)