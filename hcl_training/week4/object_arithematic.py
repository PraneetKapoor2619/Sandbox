class points:

        def __init__(self, x, y, z):
                self.__x = x
                self.__y = y
                self.__z = z

        def getx(self):
                return self.__x
        
        def gety(self):
                return self.__y

        def getz(self):
                return self.__z

        def __sub__(self, p2):
                obj = points(self.__x - p2.getx(), self.__y - p2.gety(), self.__z - p2.getz())
                return obj

a = points(1, 2, 3)
b = points(2, 4, 10)
print(type(b - a), b - a, (b-a).getx(), (b-a).gety(), (b-a).getz())