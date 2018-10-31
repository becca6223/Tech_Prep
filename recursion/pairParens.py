def getAllPairParens(n):
	"""
	n: n pairs of parentheses
	"""
	if n == 0:
		return None
		
	result = []
	getAllPairParensVisit(n, 0, result, "")
	
	return result

def getAllPairParensVisit(n, openLeft, result, string):
	"""
	n: remaining pairs
	openLeft: number of left parentheses
	result (list): contains all the possible valid n pairs of parentheses
	string: current parentheses string
	"""
	
	if n == openLeft and n == 0:
		#no more remaining pairs (n = 0) and it's balanced pairs (openLeft = 0)
		result.append(string)
	else:
		if openLeft <= n:
			#can still add ( cuz still have remaining pairs left
			getAllPairParensVisit(n, openLeft + 1, result, string + "(")
		if openLeft != 0: 
			#can add ) cuz there is at least one (
			getAllPairParensVisit(n - 1, openLeft - 1, result, string + ")")

if __name__ == "__main__":
	n = input("Enter number of pairs of parentheses: ")
	result = getAllPairParens(int(n))
	print(result)
		