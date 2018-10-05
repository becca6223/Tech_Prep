def stringCompress(str1):
	length = len(str1)

	if length == 1:
		return str1
	else:
		start = str1[0]
		sameCharLen = 1
		finalStr = ""
		
		for i in str1[1:]:
			if i != start:
				finalStr += start + str(sameCharLen)
				start = i
				sameCharLen = 1
			else:
				sameCharLen += 1

		finalStr += start + str(sameCharLen) #take care last part of the string		
		
		print(str1)
		print(finalStr)

		if len(finalStr) < length:
			return finalStr
		else: 
			return str1


if __name__ == "__main__":
	str1 = input("str1: ")
	result = stringCompress(str1)
	print("result: ", result)

