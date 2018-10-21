class Node:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None


def pathsWithSum(root, targetVal):
	if root == None:
		return 0
	
	sumDict = {}

	totalPaths = sumFromNode(root, targetVal, 0, sumDict) 	
	return totalPaths 

def sumFromNode(root, targetVal, currentSum, sumDict):
	if root == None:
		return 0
	
	paths = 0


	currentSum += root.val
	paths += pathsFromDict(currentSum - targetVal, sumDict)

	if currentSum == targetVal:
		paths += 1

	if currentSum in sumDict:
		sumDict[currentSum] += 1
	else:
		sumDict[currentSum] = 1

	leftPaths = sumFromNode(root.left, targetVal, currentSum, sumDict)
	rightPaths = sumFromNode(root.right, targetVal, currentSum, sumDict)

	eraseKey(currentSum, sumDict)

	return paths + leftPaths + rightPaths 

def pathsFromDict(diffVal, sumDict):
	if diffVal in sumDict:
		return sumDict[diffVal]
	else:
		return 0

def eraseKey(valErased, sumDict):
	if valErased in sumDict and sumDict[valErased] > 1:
		sumDict[valErased] -= 1
	else:
		sumDict.pop(valErased, None)


if __name__ == "__main__":
	root = Node(2)
	root.left = Node(1)
	root.right = Node(0)
	root.left.left = Node(1)

	paths = pathsWithSum(root, 2)
	print(paths)
