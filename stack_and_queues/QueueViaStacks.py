from Stack import *

class MyQueue:
	def __init__(self):
		self.first = None
		self.last = None
		self.size = 0
		self.addItemStack = MyStack()
		self.removeItemStack = MyStack()
	
	def add(self, item):
		self.addItemStack.push(item)
		self.size += 1
		self.last = item

		if self.size == 1:
			self.first = self.last


	def remove(self):
		#This is when the first value in queue will change after remove action
		topItem = self.peek()
		self.removeItemStack.pop()
		self.size -= 1

		#update self.first
		self.first = self.peek()
		if self.size <= 1:
			self.last = self.first

		return topItem

	def isEmpty(self):
		return True if self.size == 0 else False
	
	def peek(self):
		if self.removeItemStack.isEmpty():
			if self.addItemStack.isEmpty():
				return None
			else:
				#pop all the items from addItemStack, push all the items to removeItemStack
				while not self.addItemStack.isEmpty():
					popItem = self.addItemStack.pop()
					self.removeItemStack.push(popItem)

				topItem = self.removeItemStack.top
				return topItem
		else:
			topItem = self.removeItemStack.top
			return topItem

if __name__ == "__main__":
	qstack = MyQueue()
	for i in range(1, 6):
		qstack.add(i)
	
	print("first: ", qstack.first)
	print("last: ", qstack.last)
	print("peek: ", qstack.peek())
	
	print("remove item: ", qstack.remove())

	print("first: ", qstack.first)
	print("peek: ", qstack.peek())
	print("last: ", qstack.last)

	while not qstack.isEmpty():
		print(qstack.remove())

	print("after queue is empty: ")
	print("first: ", qstack.first)
	print("last: ", qstack.last)


