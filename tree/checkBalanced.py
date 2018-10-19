class Node:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None


def checkTreeBalanced(root):
	if root is None:
		return [True, 0]
	else:
		left_stat, left_height  = checkTreeBalanced(root.left)
		
		if left_stat is False:
			return [False, 0]

		right_stat, right_height = checkTreeBalanced(root.right)
		
		if right_stat is False:
			return [False, 0]
		
		diff_height = abs(left_height - right_height)
		max_height = max(left_height, right_height)
		if diff_height <= 1:
			return [True, max_height + 1]
		else:
			return [False, 0]


if __name__ == "__main__":
	#construct tree
	print("case 1")
	root = Node(1)
	result = checkTreeBalanced(root)
	print(result)

	print("\ncase2")
	root = Node(1)
	root.left = Node(2)
	result = checkTreeBalanced(root)
	print(result)
	
	print("\ncase 3")
	root = Node(1)
	root.left = Node(2)
	root.right = Node(3)
	root.left.left = Node(4)
	root.left.right = Node(5)
	root.left.left.left = Node(6)
	root.left.left.right = Node(7)
	result = checkTreeBalanced(root)
	print(result)

	print("\ncase 4")
	root = Node(1)
	root.left = Node(2)
	root.right = Node(3)
	root.right.left = Node(13)
	root.left.left = Node(4)
	root.left.right = Node(5)
	root.left.left.left = Node(6)
	root.left.left.right = Node(7)
	result = checkTreeBalanced(root)
	print(result)

