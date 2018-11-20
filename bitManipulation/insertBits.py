#Insertion 
#This is not correct because we are operating the number as decimal not as binary
# ONLY work if N, M are actual binary
#all bitwise operation result represented as decimal

def insertBits(N, M, start, last):
	allOne = ~0 
	left = allOne << (last + 1)
	right = (1 << start) - 1
	mask = left | right  # 1110000111
	shift_M = M << (start + 1)
	
	result = shift_M | mask
	
	return result 

	
if __name__ == "__main__":
	userInput = input("Enter N(big num binary), M(big num binary), start, last: ")
	userInput = [int(i) for i in userInput.split(" ")]
	N = userInput[0]
	M = userInput[1]
	
	result = insertBits(userInput[0], userInput[1], userInput[2], userInput[3])
	print("N: ", bin(N), "M: ", bin(M), " ", bin(result))