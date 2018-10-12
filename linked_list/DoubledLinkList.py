class Node:
	def __init__(self, data):
		self.data = data
		self.prevNode = None
		self.nextNode = None

class DoublyLinkedList:
	def __init__(self):
		self.size = 0
		self.dummy = Node(None)
		self.head = None
		self.tail = None
	
	def addNode(self, val):
		node = Node(val)
		if self.tail is None:
			node.prevNode = self.dummy
			self.head = node
			self.tail = node 
			self.dummy.nextNode = self.head
		else:
			self.tail.nextNode = node
			node.prevNode = self.tail 
			self.tail = node

		self.size += 1
	
	def removeNode(self, val):
		cur_head = self.head
		while cur_head is not None and cur_head.data != val:
			cur_head = cur_head.nextNode
		
		if cur_head is None:
			print("no node can be removed!")
			return
		else:
			if self.size == 1:
				self.head = None
				self.tail = None
			elif cur_head == self.tail:
				self.tail = self.tail.prevNode
				self.tail.nextNode = None
			else:
				cur_head.prevNode.nextNode = cur_head.nextNode
				cur_head.nextNode.prevNode = cur_head.prevNode
			
			self.head = self.dummy.nextNode
			self.size -= 1


	def traverseList(self):
		cur_node = self.head
		while cur_node is not None:
			print(cur_node.data, end=" ")
			cur_node = cur_node.nextNode
		print()


	def postTraverseList(self):
		cur_node = self.tail
		while cur_node is not None and cur_node != self.dummy:
			print(cur_node.data, end=" ")
			cur_node = cur_node.prevNode
		print()

if __name__ == "__main__":
	doubList = DoublyLinkedList()
	for i in range(0,5):
		doubList.addNode(i)
	doubList.traverseList()

	doubList.removeNode(0)

	doubList.traverseList()
	
	doubList.postTraverseList()
