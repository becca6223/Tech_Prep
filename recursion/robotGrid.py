def robotPath(matrix, r, c):
	queue = []
	if r == 1 and c == 1: 
		return queue
	elif r == 1:
		queue = ["r" for i in range(1, c)]
	elif c == 1:
		queue = ["d" for i in range(1, r)]
		
	final_r = r - 1
	final_c = c - 1
	cur_r = 0
	cur_c = 0

	while [cur_r, cur_c] != [final_r, final_c]:
		print(cur_r, cur_c)
		if matrix[cur_r][cur_c] == 0:
			#not walkable 
			if queue[-1] == "d":
				queue.pop()
				queue.pop()
				queue.append("d")
				cur_c -= 1
			else:
				queue.pop()
				queue.append("d")
				cur_r += 1
				cur_c -= 1
		else:
			if cur_c + 1 < c:
				queue.append("r")
				cur_c += 1
			else:
				queue.append("d")
				cur_r  += 1
	print(cur_r, cur_c)

	return queue

if __name__ == "__main__":
	matrix = [[1,1,1,1],[1,1,0,0],[0,1,1,1],[1,1,1,1]]
	path = robotPath(matrix,4,4)
	print(path)
