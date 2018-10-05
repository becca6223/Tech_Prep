def isOneWay(str1, str2):
	len1 = len(str1)
	len2 = len(str2)

	equal = True if len1 == len2 else False
	longerStr = str1 if len1 > len2 else str2
	shorterStr = str1 if len1 < len2 else str2

	if abs(len1- len2) > 1:
		return False
	elif equal:
		#Check one replacement
		diff = 0;
		for i, j in zip(str1, str2):
			if i != j:
				diff += 1
			
			if diff > 1:
				return False
		return True
	else:
		#Check one insertion/removement
		for loc, i in enumerate(longerStr):
			if loc < len2 and shorterStr[loc] != i:
				print(shorterStr[loc:])
				print(longerStr[loc+1:])
				return shorterStr[loc:] == longerStr[loc+1:]
		
		return True

if __name__ == "__main__":
	str1 = input("str1: ")
	str2 = input("str2: ")
	result = isOneWay(str1, str2)
	print(result)
