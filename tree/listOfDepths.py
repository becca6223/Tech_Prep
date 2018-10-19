from minimalTree import *

class Node:
	def __init__(self, value):
		self.value = value
		self.right = None 
		self.left = None

def listOfDepths(root):
	depth_lists = []
	len_list = 0
	preorder_traverse(root, 0, depth_lists, [0])

	return depth_lists 


def preorder_traverse(root, level, depth_lists, len_list):
	if root is None:
		return 
	else:
		if level >= len_list[0]:
			# visited D depth of the tree first time
			depth_lists.append([root.value])
			len_list[0] += 1		
		else:
			depth_lists[level].append(root.value)

		preorder_traverse(root.left, level + 1, depth_lists, len_list)
		preorder_traverse(root.right, level + 1, depth_lists, len_list)


if __name__ == "__main__":
	value = input("put a number b that construct a tree with a height of log2(b): ")
	a = [ i for i in range(0,int(value))]
	root = minimalTree(a)
	D_lists = listOfDepths(root)
	print(D_lists)
