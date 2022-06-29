class datatype1:
        """
                New Data Type
                Contains value, and minimum and maximum error
        """

        def __init__(self, x, e_min, e_max):
                self.__x = x
                self.__e_min = e_min
                self.__e_max = e_max
        
        def get_x(self):
                return self.__x
        
        def get_err(self):
                return [self.__e_min, self.__e_max]
        
        def get_all(self):
                x = self.get_x()
                e_min = self.get_err()[0]
                e_max = self.get_err()[1]
                return [x, e_min, e_max]
        
        def set_x(self, x):
                self.__x = x
        
        def set_err(self, e_min, e_max):
                self.__e_min = e_min
                self.__e_max = e_max
        
        def set_all(self, x, e_min, e_max):
                self.set_x(x)
                self.set_err(e_min, e_max)
        
        def print_data(self):
                print("Value: {:.2f}, Min. Error: {:.2f}, Max. Error: {:.2f}".format(self.__x, self.__e_min, self.__e_max))


obj1 = datatype1(1, 0.5, 0.1)
obj1._datatype1__x = 15.6               # Setting value outside the class definition

obj1.print_data()
print(obj1.get_all())

obj1.set_all(13.59624, -1.29e-03, 1.58e+01)
obj1.print_data()