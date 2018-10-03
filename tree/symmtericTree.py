def isSymmetric(root):
	"""
	:type root: TreeNode
	:rtype: bool
	"""
	# cut a tree into two halves and traverse and see if they are the same 
	list1 = []
	list2 = []
	if root != None:
	    traverse(root.left, "L", list1)   
	    traverse(root.right, "R", list2)        
	if len(list1) != len(list2):
		return False
        
	for i, j in zip(list1, list2):
		if i != j:
			return False        
	return True
        
def traverse(node, direct, cur_list):
	if node == None:
        cur_list.append(" ")
	else:
        cur_list.append(node.val)
		if direct == "L":
            traverse(node.right, "R", cur_list)
        else:
            traverse(node.left, "L", cur_list) 
         