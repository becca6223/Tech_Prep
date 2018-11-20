class Box:
	def __init__(self, w, h, d):
		self.width = w
		self.height = h
		self.depth = d
		

def stackBoxes(remainBoxes):
	maxHeight = stackBoxesVisit(remainBoxes, [], 0)
	return maxHeight

def stackBoxesVisit(remainBoxes, stack_box, maxHeight):
	for pick_box in remainBoxes:
		if checkBoxValid(stack_box, pick_box):
			stack_box.append(pick_box)
			maxHeight = stackBoxesVisit(remainBoxes, stack_box, maxHeight)
			stack_box.pop()
	
	#calculate the height
	totalHeight = 0
	for box in stack_box:
		totalHeight += box.height
	if totalHeight > maxHeight:
		return totalHeight
	else:
		return maxHeight
	
	
def checkBoxValid(stack_box, cur_box):
	if stack_box == []:
		#if empty, than cur_box can be the bottom 
		return True 
	else:
		top_box = stack_box[-1]
		if (cur_box not in stack_box) and (cur_box.width > top_box.width and cur_box.height > top_box.height and cur_box.depth > top_box.depth):
			return True
		else:
			return False

if __name__ == "__main__":
	a = [Box(1,2,3), Box(4,1,6), Box(12,9,50), Box(7,15,30)]
	height = stackBoxes(a)
	print(height)
	
	#better method is to sort first
	
	
	
	
	
	