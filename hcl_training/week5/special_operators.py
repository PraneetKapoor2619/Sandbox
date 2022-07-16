class MethodMod:

        def __init__(self, number):
                self.__number = number

        def __mod__(self, other):
                return self.__number % other.__number
        
obj1 = MethodMod(10)
obj2 = MethodMod(3)

print(obj1 % obj2)
print(MethodMod.__mod__(obj1, obj2))