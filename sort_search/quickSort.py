def quickSortWrapper(list_elements):
	length = len(list_elements)
	if length <= 1:
		return 
	else:
		#call quick sort 
		quickSort(list_elements, 0, length - 1)
	

def quickSort(list_elements, lb, ub):
	if lb >= ub:
		return 
	else:
		pivot_index = partition(list_elements, lb, ub)

		#quickSort left part
		#if pivot_index - 1 > lb:
		quickSort(list_elements, lb, pivot_index - 1)
		#quickSort right part
		#if pivot_index < ub:
		quickSort(list_elements, pivot_index, ub)

def partition(list_elements, lb, ub):
	#return pivot index 
	
	#choose mid point as pivot 
	mid = int((lb + ub) / 2)
	middle = list_elements[mid]

	while lb <= ub:
		#continue to scan through the array when lb and ub haven't crossed each other
		
		#find next element that doesn't belong to the left part 
		while list_elements[lb] < middle:
			lb += 1

		#find next element that doesn't belong to the right part
		while list_elements[ub] > middle:
			ub -= 1

		if  lb <= ub:
			#swap value at index lb and index ub
			temp = list_elements[lb]
			list_elements[lb] = list_elements[ub] 
			list_elements[ub] = temp
			lb += 1
			ub -= 1

	return lb


if __name__ == "__main__":
	list_num = input("Enter a list of numbers: ")
	list_num = [int(i) for i in list_num.strip().split(" ")]
	quickSortWrapper(list_num)
	print(list_num)
