class Node:
	def __init__(self, value):
		self.value = value 
		self.left = None
		self.right = None
	
	def addRight(self, node):
		self.right = node
	
	def addLeft(self, node):
		self.left = node

def main():
	a = [6, 91, 34, 21, -10, 0, 65, 27]
	root = Node(a[0])
	
	#construct a binary search tree
	for i in a[1:]:
		temp = root 
		while temp.value != None:
			if i >= temp.value:
				if temp.right == None:
					temp.right = Node(i)
					break
				temp = temp.right
			else:
				if temp.left == None:
					temp.left = Node(i)
					break
				temp = temp.left

	#traverse the tree
	print("Preorder")
	preorder(root)
	print("Inorder")
	inorder(root)
	print("Postorder")
	postorder(root)


def inorder(node):
	if(node.left != None):
		inorder(node.left)
	print(node.value)
	if(node.right != None):
		inorder(node.right)

def preorder(node):
	print(node.value)
	if(node.left != None):
		preorder(node.left)
	if(node.right != None):
		preorder(node.right)

def postorder(node):
	if(node.left != None):
		postorder(node.left)
	if(node.right != None):
		postorder(node.right)
	print(node.value)
	

if __name__ == "__main__":
	main()






