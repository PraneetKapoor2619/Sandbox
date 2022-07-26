class array():
	# constructor
	def __init__(self):
		self.__data = None
		self.__next = None
		self.__len = 0
	
	# get an array iterator
	def __iter__(self):
		return arrayIterator(self)

	# get data of a node
	def get_data(self):
		return self.__data
	
	# get an item at some given index
	def __getitem__(self, index):
		if (index < 0) :
			raise ValueError("Negative index is not supported")
		elif (index >= len(self)) :
			raise IndexError("Index exceeds (length - 1)")
		elif (type(index) is not int) :
			raise TypeError("Index is not of int() type")
		else :
			for i in range(index + 1) :
				data = self.get_data()
				self = self.__next
			return data

	# get length of the array
	def __len__(self):
		return self.__len + 1
	
	# append
	def append(self, data):
		# Special case: if there is only the head, you will fill it first
		if (self.__data is None) and (self.__next is None):
			self.__data = data

		# usually, we would want to go to the last node
		else :
			if self.__next == None :
				self.__next = array()
			self.__next.append(data)
			self.__len += 1

class arrayIterator():
	def __init__(self, object):
		if ".array'" in str(type(object)):
			self.object = object
		else :
			raise TypeError("Object should be of type array")
		self.__iter__()
	
	def __iter__(self):
		return self
	
	# get next node
	def __next__(self):
		if (self.object is None) :
			raise StopIteration
		else :
			data = self.object.get_data()
			self.object = self.object._array__next
			return data

if __name__ == "__main__" :
	Head = array()

	Head.append(1)
	Head.append(12)
	Head.append(31)
	Head.append(41)
	Head.append(51)
	Head.append(61)

	print("\nLength of our custom array:", len(Head))

	iterator1 = iter(Head)
	iterator2 = arrayIterator(Head)
	print("*Type of iterator returned by iter():", type(iterator1),\
	"\n*Type of iterator returned by arrayIterator:", type(iterator2))
	
	print("\nPrinting using for loop with the custom iterator")
	for element in iterator2 :
		print(element)

	print("\nPrinting using for loop with the data type itself")
	for element in Head :
		print(element)
	
	print("\nPrinting using for loop with index")
	for i in range(len(Head)) :
		print(Head[i])

	print("Appending a new integer")
	Head.append(91)
	for element in Head :
		print(element)

	print("Appending a new string")
	Head.append("Hello new data type!!")
	for i in range(len(Head)) :
		print(Head[i], end = " ")
	print("")