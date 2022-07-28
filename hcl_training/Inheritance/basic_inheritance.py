import math


class Shape():
	pi = math.pi
	e = math.e

	def __init__(self, shape_type, color = "Red"):
		self.__type = shape_type
		self.__color = color
	
	def get_type(self):
		return self.__type
	
	def get_color(self):
		return self.__color
	
	def set_color(self, color):
		self.__color = color
	
	def get_area(self):
		pass
	
	def get_perimeter(self):
		pass


class Rectangle(Shape):
	def __init__(self, length, breadth, color = "Blue"):
		Shape.__init__(self, "Rectangle", color = color)
		self.__length = length
		self.__breadth = breadth

	def get_length(self):
		return self.__length
	
	def set_length(self, length):
		self.__length = length
	
	def get_breadth(self):
		return self.__breadth
	
	def set_breadth(self, breadth):
		self.__breadth = breadth
	
	def get_area(self):
		return self.__length * self.__breadth
	
	def get_perimeter(self):
		return 2*(self.__length + self.__breadth)


class Circle(Shape):
	def __init__(self, radius, color = "Red"):
		Shape.__init__(self, "Circle", color = color)
		self.__radius = radius
	
	def get_radius(self):
		return self.__radius

	def set_radius(self, radius):
		self.__radius = radius
	
	def get_area(self):
		return Shape.pi * (self.__radius ** 2)
	
	def get_perimeter(self):
		return 2 * Shape.pi * self.__radius


if __name__ == "__main__" :
	# First I print out all the attributes of Shape() class
	print(dir(Shape))
	print("")

	# Next I make a rectangle and circle object
	rect1 = Rectangle(10, 2.5, )
	circ1 = Circle(10)

	# Print out attrs. of rect1
	print(rect1.__dict__)	# only prints attributes
	print("")
	print(dir(rect1))	# prints both attributes and methods
	print("")

	# Print out attrs. of circ1
	print(circ1.__dict__)
	print("")
	print(dir(circ1))
	print("")

	print("For Rectangle:\nPerimeter:", rect1.get_perimeter(),\
	 "\nArea:", rect1.get_area())
	
	print("\nFor Circle:\nPerimeter:", circ1.get_perimeter(),\
	"\nArea:", circ1.get_area())