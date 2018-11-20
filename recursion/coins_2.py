#Coins, see how many combinations can represent n coings with 25 cents, 10 cents 5 cents, 1 cents
#try memoization to cache the result

def coins(n):
	dollars = [25, 10, 5, 1]
	result = getAllCoinsCombo(n, dollars, 0)
	
	return result
	
def getAllCoinsCombo(remainDollar, dollars, cur_dollar):
	if dollars[cur_dollar] == 1:
		return 1
	else:
		ways = 0
		for i in range(int(remainDollar/dollars[cur_dollar]), -1, -1):
			newRemainDollar = remainDollar - i * dollars[cur_dollar]
			ways += getAllCoinsCombo(newRemainDollar, dollars, cur_dollar + 1)

		return ways

def uniqueID(dollar):
	if dollar == 25:
		return 3
	elif dollar == 10:
		return 2
	elif dollar == 5:
		return 1
	elif dollar == 1:
		return 0
		
if __name__ == "__main__":
	n = input("how many cents: ")
	result = coins(int(n))
	print(result)