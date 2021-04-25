class Node: 
	''' put description on what this class is all about '''
	def __init__(self, data= None, next_node=None):
		self.data = data
		self.next_node = next_node

class LinkedList:
	''' wrapper class that helps us keep track of the head of our 
		linked list 
	'''
	def __init__(self):
		self.head = None
		self.last_node = None

	# print data in Node 
	def print_linked_list(self):
		ll_string = ""
		node = self.head

		# check if node is none, it is empty, so we should just print NOne 
		if node is None: 
			print(None)

		#  otherwise transverse the linked list using a while loop
		while node: 
			ll_string += f"{str(node.data)} ->"
			node = node.next_node

		ll_string += " None"
		print(ll_string)

	# insert node at beginning of a linked list 
	def insert_beginning(self, data):
		# keep track of both the head and end of linked list
		if self.head is None:
			self.head = Node(data, Node)
			self.last_node = self.head

		new_node = Node(data, self.head)
		self.head = new_node

	# insert node at end of a linked list 
	def insert_end(self, data):
		if self.head is None:
			self.insert_beginning(data)
			return 

		self.last_node.next_node = Node(data, None)
		self.last_node = self.last_node.next_node
		