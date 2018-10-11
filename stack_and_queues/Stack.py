class MyStack:
	def __init__(self):
		self.stack = []
		self.top = None
		self.size = 0

	def push(self, item):
		self.stack.append(item)
		self.top = item		
		self.size += 1

	def pop(self):
		if(not self.isEmpty()):
			self.size -= 1
			self.top = None if self.size == 0 else self.stack[self.size - 1]
			return self.stack.pop()
		else:
			return None 

	def isEmpty(self):
		if self.stack == []:
			return True
		else:
			return False

	def peek(self):
		return self.top

