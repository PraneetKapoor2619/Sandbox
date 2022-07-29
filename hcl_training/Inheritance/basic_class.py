class Shape():
	const_var = 0.23

	def __init__(self, shape_type, color = "Red"):
		self.__type = shape_type
		self.__color = color
	
	def get_type(self):
		return self.__type
	
	def get_color(self):
		return self.__color
	
	def set_color(self, color):
		self.__color = color
	
	def set_extra_var(self, var):
		self.__extra = var

if __name__ == "__main__" :
	shape1 = Shape("square", color = "Green")
	print("Dictionary of attributes of shape1 before calling set_extra_var:\n", shape1.__dict__)

	shape1.set_extra_var(12.34)
	print("Dictionary of attributes of shape1 after calling set_extra_var:\n", shape1.__dict__)

	shape2 = Shape("Circle")
	print("Dictionary of attributes of shape2 before calling set_extra_var:\n", shape2.__dict__)
	print("dir() on shape2\n", dir(shape2))

	print("dir() on Shape()\n", dir(Shape))

	print("__dict__ on Shape()\n", Shape.__dict__)