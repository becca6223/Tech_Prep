def searchMatrix(matrix, element):
	numRow = len(matrix)
	numCol = len(matrix[0])

	#do BST for range
	found_row_index = matrixRangeBST(matrix, element, 0, numRow - 1, numRow, numCol)

	#the do BST within the range


def matrixRangeBST(matrix, element, lb, ub, row, col):
	#do bst in row range direction
	#return None or starting row index
	
	if lb > ub:
		#is this the right value to be returned
		return None
	else:
		#check if element is within the range or not
		mid = int((lb + ub) / 2)
		end = mid + (col - 1) #end index of that row 
		startVal = matrix[mid][0]
		endVal = matrix[mid][end]

		if startVal <= element and element <= endVal:


if __name__ == "__main__":
	pass
