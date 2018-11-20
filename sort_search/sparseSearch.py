#Sparse search, return the location of the string
def searchString(list_str, searchStr):
	if list_str == [] or searchStr == "":
		# not valid input
		return -1 
	
	
	left_pt = 0
	right_pt = len(list_str) - 1
	index = binarySearch(list_str, searchStr, left_pt, right_pt)
	
	return index
	
def binarySearch(list_str, searchStr, lb, ub):
	#print("lb", lb, "ub", ub)
	if lb <= ub:
		mid = int((lb + ub) / 2 )
		middle = list_str[mid]
		
		if middle == "" or middle == " ":
			index = binarySearch(list_str, searchStr, lb, mid - 1)
			if index == -1:
				index = binarySearch(list_str, searchStr, mid + 1, ub)
		
		elif middle == searchStr:
			return mid
		elif searchStr > middle:
			index = binarySearch(list_str, searchStr, mid + 1, ub)
		elif searchStr < middle: 
			index = binarySearch(list_str, searchStr, lb, mid - 1)
		
		#print("index", index)
		return index
	
	else:
		#print(-1)
		return -1

if __name__ == "__main__":
	str_list = input("Enter a string of list: ")
	str_list = str_list.split(',')
	searchStr = input("Enter string to be searched: ")
	print(str_list)
	index = searchString(str_list, searchStr)
	print(searchStr, "is at index", index)
	