from Stack import *

def sort_stack(stack):
	temp_stack = MyStack()
	
	if stack.isEmpty():
		print("Stack is empty. No sorting required")
		return 
	
	status, val = _onlyOneValueInStack(stack)
	
	if status:
		print("Only one value in stack. No need to sort")
		return 
	else:
		temp_stack.push(val)
		while not stack.isEmpty():
			topVal = stack.pop()							
			_sortTempStack(topVal, stack, temp_stack)

		while not temp_stack.isEmpty():
			popVal = temp_stack.pop()
			stack.push(popVal)

def _onlyOneValueInStack(stack):
	val = stack.pop()
	if stack.isEmpty():
		stack.push(val)
		return True, val
	else:
		return False, val

def _sortTempStack(topVal, stack, temp_stack):
	step = 0
	while not temp_stack.isEmpty():
		if temp_stack.peek() > topVal: 
			popVal = temp_stack.pop()
			stack.push(popVal)
			step += 1
		else:
			break
	
	temp_stack.push(topVal)

	for i in range(0, step):
		popVal = stack.pop()
		temp_stack.push(popVal)

if __name__ == "__main__":
	stack = MyStack()
	for i in range(0, 6):
		stack.push(i)
	
	sort_stack(stack)	
	
	while not stack.isEmpty():
		print(stack.pop(), end=" ")
		
