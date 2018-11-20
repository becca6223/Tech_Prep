#flip one bit
#and find the longest sequence of 1 that I can create  

def flipBit(integer):
	maxLength = 0
	first_pt = 0
	total = 0
	firstZero = True
	
	while integer > 0:
		isOne = True if integer % 2 == 1 else False
		newNum = integer >> 1
		
		if isOne and firstZero:
			#encounter one
			first_pt += 1
			total = first_pt
		
		elif isOne and not firstZero:
			total += 1
		
		else:
			#encounter zero
			if firstZero:
				first_pt += 1
				total = first_pt
				firstZero = False
				
			else:
				#reset 
				if total > maxLength:
					maxLength = total
				
				first_pt = total - first_pt + 1
				total = first_pt
		
		integer = newNum
		
	
	return maxLength

if __name__ == "__main__":
	userInput = input("Enter integer: ")
	result = flipBit(int(userInput))
	print(result)
				
		
