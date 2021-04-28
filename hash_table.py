class Node:
	def __init__(self, data = None, next_node = None):
		self.data = data
		self.next_node = next_node

class Data:
	def __init__(self, key, value):
		self.key = key
		self.value = value

class HashTable:
	def __init__(self, table_size):
		self.table_size = table_size
		self.hash_table = [None] * table_size

	# define a method that creates a hashtable for us 
	# converts key to index in hash table enabling us to access the key in constant time using indices
	def custom_hash(self, key):
		hash_value = 0
		for i in key: 
			#  converts each letter (unicode characters) to its equivalent integer value e.g. 'A' = 65
			# hash value should be as unique as possible and this can be achieved by adding some randomness
			hash_value += ord(i) 
			hash_value = (hash_value * ord(i)) % self.table_size

		# this method always returns the same hashed value for the same key
		return hash_value

	# adds key value pair to our hash table
	def add_key_value(self, key, value):
		# create a hash key using custom_hash method
		hashed_key = self.custom_hash(key)

		# if the value at the index of our hash key is none, add new node to that index of hash table 
		# passing in the key, value data pair 
		if self.hash_table[hashed_key] is None: 
			self.hash_table[hashed_key] = Node(Data(key, value) , None)
		else:
			# if value of the index of our hash key is not none, we transverse the node 
			# until we find the next None and add it there 
			# use linked list to store addditional values 
			# the head of current node is the first node at the index of interest
			node = self.hash_table[hashed_key]

			# transverse the linked list until you find the next node that is None 
			while node.next_node:
				node = node.next_node

			# insert the key, value data pair at the index of the next node that is None 
			node.next_node = Node(Data(key, value), None)


	# retrieve the value at a specified Key
	def get_value(self, key):
		# get the hashed key/ index of this key in the table using custom_hash()
		hashed_key = self.custom_hash(key)
		# check if this index exists in our table 

		if self.hash_table[hashed_key] is not None: 
			node = self.hash_table[hashed_key]

			# check if we have multiple nodes at this index
			if node.next_node is None: 
				return node.data.value
			while node.next_node:
				if key == node.data.key:
					return node.data.value
				node = node.next_node

			if key == node.data.key:
				return node.data.value

		# key was not found in our hash tables 
		return None 

	# helper method to print and visualize our hash table 
	def print_table(self):
		print("{")
		for i , val in enumerate(self.hash_table):
			if val is not None: 
				linked_list_string = ""
				node = val
				if node.next_node:
					while node.next_node:
						linked_list_string += (str(node.data.key) + " : " + str(node.data.value) + " -->")

					linked_list_string += (str(node.data.key) + " : " + str(node.data.value) + " --> None")
					print(f" [{i}] {linked_list_string}")
				else:
					print(f"  [{i}] {val.data.key} : {val.data.value}")
			else:
				print(f"  [{i}] {val}")
		print("}")

# testing 
ht = HashTable(4)
ht.add_key_value("hi", "there")
ht.print_table()





		