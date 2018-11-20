#triple steps, calculate how many ways can the person to climb the stairs
def climbStairs(stairs):
	total_ways = visitStairs(stairs, 0)
	return total_ways 
	
def visitStairs(stairs, cur_steps):
	if cur_steps == stairs:
		return 1
	elif cur_steps > stairs:
		#not valid step
		return 0 
	else: 
		#attemp another one with different steps
		ways = 0
		for i in range(1,4):
			ways += visitStairs(stairs, cur_steps + i)
		
		return ways
		
if __name__ == "__main__":
	stairs = input("how many stairs do you wanna climb? ")
	result = climbStairs(int(stairs))
	print(result)