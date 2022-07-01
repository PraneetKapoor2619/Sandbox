class base:
        def __init__(self, var):
                self.__var = var

        def get_var(self):
                return self.__var

class derived1():
        def __init__(self, var):
                self.__obj = base(var)
        
        def show(self):
                print(self.__obj.get_var())

class derived2():
        def __init__(self, var):
                self.__obj = base(var)
        
        def show(self):
                print(self.__obj.get_var())
        
class endpoint(derived1, derived2):
        def __init__(self, var1, var2):
                derived1.__init__(self, var1)
                derived2.__init__(self, var2)

        def show(self):
                derived1.show(self)
                derived2.show(self)

obj1 = endpoint(23, 43)
obj2 = endpoint(99, 100)
obj1.show()
obj2.show()