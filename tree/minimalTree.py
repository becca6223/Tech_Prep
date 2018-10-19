class Node:
	def __init__(self, value):
		self.value = value
		self.right = None 
		self.left = None


def minimalTree(sortArray):
	length = len(sortArray)
	root = preorder_traverse(sortArray, 0, length - 1)
	return root 

def preorder_traverse(sortArray, left_b, right_b):
	if left_b > right_b:
		#left bound should always be smaller or equal to right bound
		return 
	else:
		#calc the root node 
		middle = int((left_b + right_b) / 2)
		root = Node(sortArray[middle])
		root.left = preorder_traverse(sortArray, left_b, middle - 1)
		root.right = preorder_traverse(sortArray, middle + 1, right_b)
		
		return root 

def preorder_print(root, level):
	if root is None:
		return
	else:
		print(root.value, level)
		preorder_print(root.left, level + 1)
		preorder_print(root.right, level + 1)

if __name__ == "__main__":
	a = [i for i in range(0, 1)]
	root = minimalTree(a)
	preorder_print(root, 0)
