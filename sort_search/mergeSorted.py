#Sorted merge 
def mergeSorted(a_list, b_list, a_pointer, b_pointer):
	#set last index for both list 
	all_pointer = a_pointer + b_pointer + 1
	
	while b_pointer >= 0 and a_pointer >= 0:
		#keep looping until one list is all sorted
		if a_list[a_pointer] >= b_list[b_pointer]:
			a_list[all_pointer] = a_list[a_pointer]
			a_pointer -= 1
		else:
			a_list[all_pointer] = b_list[b_pointer]
			b_pointer -= 1
		
		all_pointer -= 1
	
	#move rest of the numbers from one list to another list
	if a_pointer < 0:
		#move b_list numbers from 0 to b_pointer to a_list
		for i in range(0, b_pointer):
			a_list[i] = b_list[i]
	
	
	
if __name__ == "__main__":
	a_list = input("Enter first sorted list of numbers in ascending order: ")
	a_list = [int(i) for i in a_list.split(" ")]
	a_pointer = len(a_list) - 1
	b_list = input("Enter second sorted list of numbers in ascending order: ")
	b_list = [int(i) for i in b_list.split(" ")]
	b_pointer = len(b_list) - 1
	
	for i in range(0, len(b_list)):
		a_list.append(None)
	
	mergeSorted(a_list, b_list, a_pointer, b_pointer)
	
	print("Sorted a_list with b_list merged: \n", a_list)