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
	
	def print_node(self):
		print(self.data)


def BST_insert(head, node):
	if (head is None) :
		return node
	
	if (node.get_data() <= head.get_data()) :
		head.set_left_child(BST_insert(head.get_left_child(), node))
	elif (node.get_data() > head.get_data()) :
		head.set_right_child(BST_insert(head.get_right_child(), node))
	
	return head


def BST_print_inorder(head):
	if (head.get_left_child() is not None) :
		BST_print_inorder(head.get_left_child())
	
	head.print_node()

	if (head.get_right_child() is not None) :
		BST_print_inorder(head.get_right_child())


def BST_max(head):
	if (head.get_right_child() is not None) :
		return BST_max(head.get_right_child())
	else :
		return head.get_data()


def BST_min(head):
	if (head.get_left_child() is not None) :
		return BST_min(head.get_left_child())
	else :
		return head.get_data()


def BST_lookup(head, data):
	if (head.get_data() == data) :
		return head
	else :
		if (data < head.get_data()) :
			if (head.get_left_child()) :
				return BST_lookup(head.get_left_child(), data)
			else : 
				return None
		elif (data > head.get_data()) :
			if (head.get_right_child()) :
				return BST_lookup(head.get_right_child(), data)
			else :
				return None


def BST_BFS(head):
	path = []
	Q = []

	Q.append(head)
	while len(Q) > 0 :
		node = Q.pop(0)
		path.append(node.data)

		if node.get_left_child() is not None :
			Q.append(node.get_left_child())
		
		if node.get_right_child() is not None :
			Q.append(node.get_right_child())
	return path


def BFT_DFS(head, stack = []):
	stack.append(head.get_data())

	if (head.get_left_child() is not None) :
		BFT_DFS(head.get_left_child(), stack)
	if (head.get_right_child() is not None) :
		BFT_DFS(head.get_right_child(), stack)
	
	return stack


if __name__ == "__main__" :
	Head = Node(12)
	BST_insert(Head, Node(9))
	BST_insert(Head, Node(5))
	BST_insert(Head, Node(8))
	BST_insert(Head, Node(10))
	BST_insert(Head, Node(16))
	BST_insert(Head, Node(15))
	BST_insert(Head, Node(19))
	BST_insert(Head, Node(18))
	BST_insert(Head, Node(20))

	BST_print_inorder(Head)
	print(BST_max(Head))
	print(BST_min(Head))

	print()
	print(BST_lookup(Head, 16).get_data())
	print(BST_lookup(Head, 13))

	print()
	print(BST_BFS(Head))

	print()
	print(BFT_DFS(Head))