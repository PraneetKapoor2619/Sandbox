class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None
	
	def get_left_child(self):
		return self.left
	
	def set_left_child(self, left):
		self.left = left
	
	def get_right_child(self):
		return self.right
	
	def set_right_child(self, right):
		self.right = right
	
	def get_data(self):
		return self.data
	
	def set_data(self, data):
		self.data = data

	def insert(self, node):
		print(self.get_data(), node.get_data())
		if (node.get_data() <= self.get_data()) :
			if (self.get_left_child() == None) :
				self.set_left_child(node)
			else :
				self.get_left_child().insert(node)
		elif (node.get_data() > self.get_data()) :
			if (self.get_right_child() == None) :
				self.set_right_child(node)
			else :
				self.get_right_child().insert(node)

	def lookup(self, value):
		if (value != self.data) and (self.left is None)\
		 and (self.right is None) :
			return None
		if (value < self.data) :
			return self.get_left_child().lookup(value)
		elif (value == self.data) :
			return self
		elif (value > self.data) :
			return self.get_right_child().lookup(value)

	def min(self):
		if (self.left is None) :
			return self
		else :
			return self.left.min()
	
	def max(self):
		if (self.right is None) :
			return self
		else :
			return self.right.max()

	def print_node(self):
		print(self.data, end = " ")
	
	def inorder_print(self):
		if (self.get_left_child() is not None) :
			self.get_left_child().inorder_print()
		
		self.print_node()

		if (self.get_right_child() is not None) :
			self.get_right_child().inorder_print()


if __name__ == "__main__" :
	Head = Node(12)
	Head.insert(Node(11))
	Head.insert(Node(13))
	Head.insert(Node(9))
	Head.insert(Node(15))
	Head.insert(Node(16))
	Head.insert(Node(20))
	Head.insert(Node(14))

	Head.inorder_print()
	Head.get_left_child().get_data()
	print()

	print(Head.lookup(41))
	print(Head.lookup(14))
	print(Head.lookup(13).get_data())
	print()
	
	print(Head.min().get_data())
	print(Head.max().get_data())