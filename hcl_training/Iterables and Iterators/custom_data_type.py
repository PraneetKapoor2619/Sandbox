class array():

	# constructor
	def __init__(self):
		self.__data = None
		self.__next = None
	
	# get iterator
	def __iter__(self):
		return self
	
	# get next node
	def __next__(self):
		if (self.__next != None) :
			return self.__next
		raise StopIteration

	# append
	def append(self, data):
		# first we need to go to the last node
		if self.__data == None :
			self.__data = data
		
		else :
			if self.__next == None :
				self.__next = array()
			print(type(self.__next))
			self.__next.append(data)
	
	# get data
	def get_data(self):
		return self.__data


if __name__ == "__main__" :

	Head = array()

	Head.append(1)
	Head.append(12)
	Head.append(31)
	Head.append(41)
	Head.append(51)

	element = iter(Head)
	while next(element) :
		print(element.get_data())
		element = next(element)