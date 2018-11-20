def parens(n):
	result = []
	getAllParens(n, n, "", result)
	return result

def getAllParens(remainL, remainR, string, result):
	if remainR == remainL == 0:
		#used up all the right, left parens
		result.append(string)
		return 
	else:
		if remainL != 0:
			#can still insert (
			getAllParens(remainL - 1, remainR, string + "(", result)		
		if remainL < remainR:
			getAllParens(remainL, remainR - 1, string + ")", result)
		
		
if __name__ == "__main__":
	num = input("Enter number of parens: ")
	result = parens(int(num))
	print(result)
		
	