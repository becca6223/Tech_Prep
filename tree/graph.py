#Practice BFS
class Graph:
	def __init__(self, num_vertices):
		self.vertices = num_vertices
		
		#represent a graph using index and the list within list is neightbors of that index node
		self.graph = [None] * num_vertices 
		
	def addNode(self, source, node):
		if source >= self.vertices:
			raise valueError("The source id should be less than total of vertices")
		else:
			if self.graph[source] is not None:
				self.graph[source].append(node)
			else:
				self.graph[source] = [node]

	
	def bfsTraverse(self, source):
		if source >= self.vertices:
			raise valueError("The source id should be less than total of vertices")
		else:
			visited = [0] * self.vertices #list that track if nodeID has been visited 
			queue = [] #a list of nodes that have not been visited yet
			visited[source] = 1 
			queue.insert(0, source) 
			
			while queue != []:
				nodeID = queue.pop(0)
				self.visit(nodeID)
				for neighbor in self.graph[nodeID]:
					if visited[neighbor] == 0:
						visited[neighbor] = 1
						queue.append(neighbor)			
			
	def visit(self, nodeID):
		print(nodeID)
		
	
	def dfsTraverse(self, source, visited):
		if source >= self.vertices:
			raise valueError("The source id should be less than total of vertices")
		else:
			self.visit(source)
			visited[source] = 1
			for neighbor in self.graph[source]:
				if visited[neighbor] == 0:
					visited[neighbor] = 1
					self.dfsTraverse(neighbor, visited)
					
				
if __name__ == "__main__":
	bfsGraph = Graph(5)
	bfsGraph.addNode(0,1)
	bfsGraph.addNode(0,2)
	bfsGraph.addNode(0,4)
	bfsGraph.addNode(1,0)
	bfsGraph.addNode(1,3)
	bfsGraph.addNode(1,4)
	bfsGraph.addNode(2,0)
	bfsGraph.addNode(3,1)
	bfsGraph.addNode(4,0)
	bfsGraph.addNode(4,1)
	
	print("BFS")
	bfsGraph.bfsTraverse(0)
	
	print("DFS")
	bfsGraph.dfsTraverse(0, [0] * 5)
	


