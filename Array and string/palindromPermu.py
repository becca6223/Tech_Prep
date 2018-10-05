def palindromePermu(str1):
	str1 = "".join(str1.split(" "))
	length = len(str1)
	charDict = {}
	for i in str1:
		if i not in charDict:
			charDict[i] = 1;
		else:
			charDict[i] += 1;
	
	oddFlag = False
	if length % 2 != 0 :
		for i in charDict.values():
			print(i)
			if i % 2 != 0 and not oddFlag: 
				oddFlag = True
			elif i % 2 == 0:
				pass
			else:
				return False
	else:
		for i in charDict.values():
			if i % 2 != 0:
				return False
	
	return True


if __name__ == "__main__":
	str1 = input("Enter a string: ")
	result = palindromePermu(str1)
	print(result)
