import math

class circle:
        """
        Class circle
        - Attributes are radius and color
        - Radius is a floating point number, default value = 1.0
        - Color is a string, default value = Red
        - methods are getRadius() and getArea() for getting the radius
        and area of the circle, respectively
        """
        def __init__(self, radius = 1.0, color = "Red"):
                self.__radius = radius
                self.__color = color
        
        def getRadius(self):
                return self.__radius
        
        def getColor(self):
                return self.__color
        
        def getArea(self):
                return math.pi * (self.getRadius() ** 2)