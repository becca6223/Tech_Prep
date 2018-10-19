import sys

class Node:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

def isBST(root):
	if root is None:
		return True
	else:
		result = preorder_traverse(root, None, None)
		return result

def preorder_traverse(root, minVal, maxVal):
	if root is None:
		return True
	if (minVal is not None and root.value <  minVal) or (maxVal is not None and root.value >= maxVal):
		return False
	
	result1 = preorder_traverse(root.left, minVal, root.value)

	if result1 is False:
		return False

	result2 = preorder_traverse(root.right, root.value, maxVal)
	return result1 and result2

if __name__ == "__main__":
	root = Node(0)
	root.left = Node(-2)
	root.right = Node(5)
	print(isBST(root))
