#sorted search no size
class sortedList:
	def __init__(self, list_num):
		self.list_num = list_num
	
	def elementAt(self, index):
		return -1 if index >= len(self.list_num) else self.list_num[index]

def searchElement(a_list, num):
	if a_list.elementAt(0) == -1:
		return None
	
	max_len = 1
	out_of_bound_index = None
	
	#find proper bst range, will need to check if the index is out of boundary
	val = a_list.elementAt(max_len - 1) #first val in a_list
	while val != -1 and val < num:
		max_len = 2 * max_len
		val = a_list.elementAt(max_len - 1)
	
	index = binarySearch(a_list, num, max_len / 2, max_len)

	return index

		
def binarySearch(a_list, num, lb, ub):
	index = None
	
	while lb <= ub:
		mid = int((lb + ub) / 2)
		middle = a_list.elementAt(mid)
		if middle == -1 or num > middle:
			ub = mid - 1
		elif num == middle:
			index = mid
			return index
		elif num < middle:
			ub = mid - 1
	
	return index
	
if __name__ == "__main__":
	user_input = input("Enter a list of number in ascending order: ")
	list_num = [int(i) for i in user_input.split(" ")]
	search = input("Enter number to be searched: ")
	
	obj_list_num = sortedList(list_num)
	result = searchElement(obj_list_num, int(search))
	print("Search number ", int(search), " at index ", result)
	