import copy
from pprint import pprint as pp

def eightQueens(result, row, prev_cols):
	if row >= 8:
		result.append(insertQueensPos(prev_cols))
		return 
	else:
		for chose_col in range(0, 8):
			if validPosition(chose_col, row, prev_cols):
				prev_cols.append(chose_col)
				eightQueens(result, row + 1, prev_cols)
				prev_cols.pop() #need to pop because the col will be a different value in the next iteration
				
def validPosition(chose_col, row, prev_cols):
	#never need to check same row, cuz we will skip all the chosen rows
	for cur_row, cur_col in enumerate(prev_cols):
		if chose_col == cur_col:
			return False
		elif abs(cur_col - chose_col) == (row - cur_row):
			return False
	
	return True

def insertQueensPos(eight_cols):
	grid = []
	
	#initialzie the 8 x 8 grid to 0
	for i in range(0,8):
		grid.append([])
		for j in range(0,8):
			grid[i].append(0)
	
	for loc, i in enumerate(eight_cols):
		grid[loc][i] = 1
	
	return grid

if __name__ == "__main__":
	result = []
	prev_cols = []
	eightQueens(result, 0, prev_cols)
	
	pp(result)