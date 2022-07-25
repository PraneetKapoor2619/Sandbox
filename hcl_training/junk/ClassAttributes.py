class MyAttributeClass(object) :
	"""
	Pass attributes to a class.
	Find the number of attributes in a class by custom implementation of __len__()
	"""

	def __init__(self, **kwargs):
		self.__kwargs = kwargs
		for k, v in self.__kwargs.items() :
			setattr(self, k, v)
	
	def __len__(self):
		return len(self.__kwargs)

if __name__ == "__main__" :

	arg_dict = dict()
	for _ in range(int(input())) :
		arg_list = input().split()
		key = arg_list[0]
		value = arg_list[1]

		arg_dict[key] = value
	obj = MyAttributeClass(**arg_dict)
	print(len(obj))