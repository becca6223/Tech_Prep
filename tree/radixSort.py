#radix sort 
#sort from the least significant digit all the way to the most significant digit
#
#

def radixSort(num_list):
	d = getMaxDigitCnt(num_list)
	
	for i in range(1, d + 1):
		#new bucket
		bucket = newBucket()
		
		#count sort
		#put the number into the right spot in the bucket 
		for num in num_list:
			loc = getDigitPos(num, i)
			bucket[loc].append(num)
		
		print(bucket)
		
		#put the number back to the list
		loc = 0
		for cur_list in bucket:
			for num in cur_list:
				num_list[loc] = num
				loc += 1

def getMaxDigitCnt(num_list):
	max_cnt = 0
	
	for num in num_list:
		cnt = 0
		while num != 0:
			num = int(num / 10)
			cnt += 1
		
		if cnt > max_cnt:
			max_cnt = cnt
	
	return max_cnt

def getDigitPos(num, pos):
	num = int(num / 10**(pos - 1))
	digit = num % 10
	
	return digit

def newBucket():
	bucket = []
	for i in range(0, 10):
		bucket.append([])
	
	return bucket
	
if __name__ == "__main__":
	num_list = input("Enter a list of random numbers: ")
	num_list = [int(i) for i in num_list.strip().split(" ")]
	radixSort(num_list)
	print("sorted list")
	print(num_list)
	