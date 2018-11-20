def getAllMoneyComb(n):
	cents = [1, 5, 10, 25]
	level = 0
	total = getAllMoneyCombVisit(n, cents, level)
	
	
def getAllMoneyCombVisit(remain, cents, level):
	#base case
	if level >= len(cents) - 1:
		#means it can't replace remain with other coin, find one combo
		return 1
	else:
		i = 0;
		total = 0
		while remain - i * cents[level] >= 0:
			remain = remain - i*cents[level]
			total += getAllMoneyCombVisit(remain, cents, level + 1)
			i += 1 #update, to check if can replace with another coin
			
		return total

	
if __name__ == "__main__":
	n = input("total cents: ")
	result = getAllMoneyComb(int(n))
	print(result)