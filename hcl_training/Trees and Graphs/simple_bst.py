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
	
	def BFT(self):
		path = []

		queue = MyQueue()
		queue.enqueue(self)

		while len(queue) > 0 :
			#print(queue.print_queue())
			current = queue.dequeue()

			path.append(current.data)

			if current.get_left_child() != None :
				queue.enqueue(current.get_left_child())
			
			elif current.get_right_child() != None :
				queue.enqueue(current.get_right_child())
		
		return path


class MyQueue:

	def __init__(self):
		self.queue = []
	
	def enqueue(self, obj):
		self.queue.append(obj)
	
	def dequeue(self):
		return self.queue.pop(0)

	def __len__(self):
		return len(self.queue)
	
	def isEmpty(self):
		return len(self) == 0
	
	def peek(self):
		if self.isEmpty() :
			raise Exception("Nothing to peek")
		
		return self.queue[0]
	
	def print_queue(self):
		print(self.queue)


if __name__ == "__main__" :
	Head = Node(12)
	Head.insert(Node(9))
	Head.insert(Node(5))
	Head.insert(Node(8))
	Head.insert(Node(10))
	Head.insert(Node(16))
	Head.insert(Node(15))
	Head.insert(Node(19))
	Head.insert(Node(18))
	Head.insert(Node(20))

	Head.inorder_print()
	print()

	print(Head.get_right_child().BFT())