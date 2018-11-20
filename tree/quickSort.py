#quick sort -> average time complexity O(nlogn), worst case -> O(n^2)
#all the elements on the right will be equal or greater than the pivot
#all the elements on the left of the pivot will be less than the pivot


def quickSort(num_list):
	length = len(num_list)
	
	if length == 0 or length == 1:
		return 
	else:
		sortProcess(num_list, 0, length  - 1)
		
def sortProcess(num_list, lb, ub):
	if lb > ub:
		return
	else:
		index = partition(num_list, lb, ub)
		#index is the boundary. don't sort if there is only one element
		if lb < index - 1:
			sortProcess(num_list, lb, index - 1)
		if index < ub: 
			sortProcess(num_list, index, ub)
		
def partition(num_list, lb, ub):
	mid = int((lb + ub) / 2)
	middle = num_list[mid]
	
	while lb <= ub:
		while num_list[lb] < middle:
			lb += 1
		while num_list[ub] > middle:
			ub -= 1
		
		if lb <= ub:
			#swap element
			temp = num_list[lb]
			num_list[lb] =num_list[ub]
			num_list[ub] = temp
			lb += 1
			ub -= 1
			
	return lb 
			
		
		
		
		
if __name__ == "__main__":
	num_list = input("Enter a list of random numbers: ")
	num_list = [ int(i) for i in num_list.strip().split(" ") ]
	
	print("original array")
	print(num_list)
	
	quickSort(num_list)
	
	print("sorted array")
	print(num_list)