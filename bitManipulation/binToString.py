#double to string 
#Given a double that is between 0 and 1 exclusively, convert that to a binary number

def doubleToBin(doubleNum):
	#assume input value is correct
	string = "."
	
	while doubleNum > 0:
		newNum = doubleNum * 2
		
		if len(string) > 32:
			return "ERROR"
		else:
			if newNum >= 1:
				string += "1"
				doubleNum = newNum - 1
			else:
				string += "0"
				doubleNum = newNum
	
	return string
	
	
if __name__ == "__main__":
	inputDouble = input("Please enter a double number that is less than 1 and greater than 0: ")
	result = doubleToBin(float(inputDouble))
	print(result)