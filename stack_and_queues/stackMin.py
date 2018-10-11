from Stack import *

#This stackmin can be more optimized that it doesn't have to store all the min value 
class StackMin:
	def __init__(self):
		self.oriStack = MyStack()
		self.minStack = MyStack()
		self.minValue = None

	def push(self, item):
		self.oriStack.push(item)
		
		if self.minValue == None:
			self.minStack.push(item)
			self.minValue = item
		else:
			if item < self.minValue:
				self.minStack.push(item)
				self.minValue = item
			else:
				self.minStack.push(self.minValue)

	def pop(self):
		popMin = self.minStack.pop()
		topMin = self.minStack.peek()
		self.minValue = topMin
		return self.oriStack.pop()
			
	def minMember(self):
		return self.minValue

if __name__ == "__main__":
	minStack = StackMin()
	minStack.push(1)
	minStack.push(-2)
	minStack.push(-8)
	minStack.push(10)

	print(minStack.minMember())

	minStack.pop()
	print(minStack.minMember())

	minStack.pop()
	print(minStack.minMember())

	minStack.pop()
	print(minStack.minMember())

	minStack.pop()
	print(minStack.minMember())




	




