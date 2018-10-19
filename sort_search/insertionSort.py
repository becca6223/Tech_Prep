def insertionSort(arrayVals:list):
	#assume you can't use library sort functions
	length = len(arrayVals)
	for i in range(1, length):
		for j in range(i, 0, -1):
			if arrayVals[j] < arrayVals[j-1]:
				temp = arrayVals[j]
				arrayVals[j] = arrayVals[j-1]
				arrayVals[j-1] = temp

	print(arrayVals)



if __name__ == "__main__":
	a = [1,2,390,-1,89]
	insertionSort(a)
