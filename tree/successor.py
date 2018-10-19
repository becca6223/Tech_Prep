class Node:
	def __init__(self, value, parent = None):
		self.value = value
		self.left = None
		self.right = None
		self.parent = parent


def find_successor(node):
	if node.right is None:
		temp = node
		parent = temp.parent 
		while parent is not None and parent.right == temp:
			parent = parent.parent 
			temp = temp.parent

		return parent
	else:
		temp = node.right 
		parent = temp
		while temp is not None:
			parent = temp
			temp = temp.left 
		
		return parent

if __name__ == "__main__":
	root = Node(0)
	root.left = Node(1, root)
	root.right = Node(2, root)
	root.left.left = Node(5, root.left)
	root.left.right = Node(6, root.left)

	result = find_successor(root.right)
	a = None  if result is None else result.value
	print(result, a)
