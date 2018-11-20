from enum import Enum

class Color(Enum):
	black = 1
	white = 2
	blue = 3
	green = 4
	yellow = 5
	red = 6

def paintFill(image, row, col, new_color):
	#Assume new position (row, col) is valid position -> no error checking 
	num_rows = len(image)
	num_cols = len(image[0])

	if image[row][col] == new_color:
		print("New color is the same as the color at image[row][col]. No filling required.")
		return False

	else:
		#You will want to fill in the new color and propagate through as long as the neighbors' color didn't change from its orig color
		#call recursion function
		ori_color = image[row][col]
		visitPosition(image, num_rows, num_cols, row, col, ori_color, new_color)
		return True

def visitPosition(image, num_rows, num_cols, row, col, ori_color, new_color):
	#Check if new position row, col is valid or not 
	if row >= num_rows or row < 0 or col >= num_cols or col < 0:
		#non valid position 
		return 
	
	if image[row][col] != ori_color:
		return 
	
	image[row][col] = new_color
	visitPosition(image, num_rows, num_cols, row - 1, col, ori_color, new_color)
	visitPosition(image, num_rows, num_cols, row + 1, col, ori_color, new_color)
	visitPosition(image, num_rows, num_cols, row, col - 1, ori_color, new_color)
	visitPosition(image, num_rows, num_cols, row, col + 1, ori_color, new_color)

	return 

if __name__ == "__main__":
	image = []
	image.append([Color.black, Color.black, Color.black, Color.black])
	image.append([Color.black, Color.black, Color.blue, Color.black])
	image.append([Color.black, Color.green, Color.blue, Color.black])
	image.append([Color.green, Color.green, Color.blue, Color.black])
	
	print("original image")
	for row in range(0, len(image)):
		for col in range(0, len(image[0])):
			print(image[row][col], end=" ")
		print()

	new_color = Color.red
	row = 1
	col = 1
	paintFill(image, row, col, new_color)

	print("position: ", row, ", ", col, "new_color: ", new_color) 
	print("new image")
	for row in range(0, len(image)):
		for col in range(0, len(image[0])):
			print(image[row][col], end=" ")
		print()
