def mergeSortWrapper(array):
	length = len(array)
	
	if length <= 1:
		return array 
	else:
		result = mergeSort(array, 0, length - 1)
		return result

def mergeSort(array, lb, ub):
	if lb == ub:
		return [array[lb]]
	
	mid = int((lb + ub) / 2)
	
	leftResult = mergeSort(array, lb, mid)
	rightResult = mergeSort(array, mid + 1, ub)
	mergeResult = mergingProcess(leftResult, rightResult)
	return mergeResult


def mergingProcess(leftResult, rightResult):
	result = []
	left_lb = 0
	right_lb = 0
	left_ub = len(leftResult) - 1
	right_ub = len(rightResult) -1
	
	#print("left array ", leftResult, left_lb, left_ub)
	#print("right array ", rightResult, right_lb, right_ub)
	
	while left_lb <= left_ub or right_lb <= right_ub:
		if left_lb > left_ub:
			result += rightResult[right_lb:right_ub + 1]
			break
		elif right_lb > right_ub:
			result += leftResult[left_lb:left_ub + 1]
			break

		if rightResult[right_lb] < leftResult[left_lb]:
			#ascending order 
			result.append(rightResult[right_lb])
			right_lb += 1
		else:
			result.append(leftResult[left_lb])
			left_lb += 1
	
	return result


if __name__ == "__main__":
	array = [4,0,-1,45,25]
	result = mergeSortWrapper(array)
	print(result)
