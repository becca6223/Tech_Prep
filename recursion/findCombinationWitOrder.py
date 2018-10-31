def findComboWrapper(string, digits):
	totalCombo = findComboVisit(string, digits, 0)
	return totalCombo
	
def findComboVisit(string, digits, loc):
	"""
	string: input string integer values
	digits: a list with 3 digits in order 
	loc: location in digits' list
	"""
	#can make it better by caching result
	
	if loc > 2:
		return 1
	
	total = 0
	for cur_loc, i in enumerate(string):
		#print(i)
		if i == digits[loc]:
			total += findComboVisit(string[cur_loc + 1:], digits, loc + 1)
	
	return total
	
if __name__ == "__main__":
	string = input("Enter a integer value: ")
	digits = input("Enter 3 digits in order in between 0 and 10 exclusively: ")
	digits = digits.split(" ")
	print(digits)
	total = findComboWrapper(string, digits)
	print("Total Combinations: ", total)
	
			