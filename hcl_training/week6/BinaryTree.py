class Node:

        def __init__(self, data):
                self.left = None
                self.right = None
                self.data = data
        
        # getter-setter for right child of a node
        def get_right_child(self):
                return self.right
        
        def set_right_child(self, right):
                self.right = right
        
        # getter-setter for left child of a node
        def get_left_child(self):
                return self.left
        
        def set_left_child(self, left):
                self.left = left
        
        # getter-setter for data stored in a node
        def get_data(self):
                return self.data
        
        def set_data(self, data):
                self.data = data
        
        # print node and associated subtree
        def print_node(self):

                if self.left :
                        self.left.print_node()
                
                print("|-{0}-|".format(self.data))

                if self.right :
                        self.right.print_node()

def insert(head, node):

        if head == None :
                return node
        
        if node.get_data() <= head.get_data() :
                head.set_left_child(insert(head.get_left_child(), node))
        else :
                head.set_right_child(insert(head.get_right_child(), node))
        
        return head

if __name__ == "__main__" :

        ROOT = Node(15)
        a = Node(25)
        b = Node(65)
        c = Node(12)
        d = Node(1)
        e = Node(15)

        ROOT = insert(None, ROOT)
        insert(ROOT, a)
        insert(ROOT, b)
        insert(ROOT, c)
        insert(ROOT, d)
        insert(ROOT, e)
        ROOT.print_node()