#rotated array
def searchRotatedArray(num_list, num):
	left_pt = 0
	right_pt = len(num_list) - 1
	
	min_left = num_list[0]
	max_right = num_list[-1]
	
	index = -1 #index of the searched number
	
	while left_pt <= right_pt:
		mid = int((left_pt + right_pt) / 2)
		
		#check if mid point is searched num
		if num_list[mid] == num:
			index = mid
			break
		
		'''#check if mid belongs to left part or right part
		if num_list[mid] >= min_left:
			#mid belong to the left 
			if num < num_list[mid] and num >= min_left:
				#go to right
				left_pt = mid + 1
				min_left = num_list[left_pt]
				
			else:
				#go to left
				right_pt = mid - 1
				max_right = num_list[right_pt]
				
		else:
			#mid belong to the right
			if num > num_list[mid] and num <= max_right:
				#go to right
				left_pt = mid + 1
				min_left = num_list[left_pt]
				
			else:
				#go to left 
				right_pt = mid - 1
				max_right = num_list[right_pt]'''
				
		if max_right >= min_left:
			#do proper binary search
			if num > num_list[mid]:
				#go right
				left_pt = mid + 1
				min_left = num_list[left_pt]
			else:
				#go left
				right_pt = mid - 1
				max_rigth = num_list[right_pt]
		else:
			if num <= max_right:
				#go right
				left_pt = mid + 1
				min_left = num_list[left_pt]			
			elif num > min_left:
				#go left 
				right_pt = mid - 1
				max_rigth = num_list[right_pt]
			else:
				return -1
							
	return index
	
if __name__ == "__main__":
	num_list = input("Enter a rotated array with integers: ")
	num_list = [int(i) for i in num_list.split(" ")]
	num = input("Enter search number: ")
	index = searchRotatedArray(num_list, int(num))
	
	print("search number ", num, " index: ", index) 