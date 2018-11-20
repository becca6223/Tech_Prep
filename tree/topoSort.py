#Topo Sort.
#Assume that the given input is correct. It is a DAG. (Directed Acyclic Graph)

#Technically you don't need to find the node wiht 0 in-degree if it is DAG
#but if not, you can try to find and if doesn't exist, just print Eroor

class Node:
	def __init__(self, name):
		self.name = name
		self.neighbors = []
	

def createGraph(file_path):
	graphDict = {}
	
	with open(file_path, 'r') as fp:
		content = fp.readlines()
		content = [i.strip() for i in content] #a list of string with source, dest, cost
		
		#build directed graph 
		for curr in content:
			info = curr.split(" ")
			source = info[0]
			nbr = info[1:]
			
			#check if source exists and either create a new obj or retrieve one
			if source not in graphDict:
				source_node = Node(source)
				graphDict[source] = source_node
			else:
				source_node = graphDict[source]
			
			#check if dest(s) exists and either create a new obj or retrieve one
			for dest in nbr:
				if dest not in graphDict:
					dest_node = Node(dest)
					graphDict[dest] = dest_node
				else:
					dest_node = graphDict[dest]
				
				setUpNbr(source_node, dest_node)
			
			#print(source_node.name, [i.name for i in source_node.neighbors])
	
	return graphDict
	
def setUpNbr(source, dest):	
	source.neighbors.append(dest)
	
def topoSort(graphDict):
	#get 0 in-degree nodes first
	topNodes = getTopNodes(graphDict) #this contain Class Node
	print([i.name for i in topNodes])
	
	if topNodes == []:
		return "can't create a topo sort with the graph provided"
	else:
		#doing dfs on 0 in-degree nodes (have a stack to maintain the topo order)
		topoTrack = []
		visited = set()
		for cur_node in topNodes:
			traverseDFS(cur_node, topoTrack, visited)
			
		return topoTrack
		
def traverseDFS(node, topoTrack, visited):	
	visited.add(node) #currently visiting this node. afterwards needs to be added to visited
	if node.neighbors == []:
		#no nbrs 
		topoTrack.insert(0, node.name)
	else:		
		#have more nbr, continue to travel all the nbrs (post order concept)
		for nbr in node.neighbors:
			if nbr not in visited:
				traverseDFS(nbr, topoTrack, visited)	
		
		#add yourself after visiting all your nbr
		topoTrack.insert(0, node.name)
	
	
def getTopNodes(graphDict):
	# it will return a list that contain nodes with 0 in-degree
	topNodes = set()
	notTopNodes = set() 
	
	for node_obj in graphDict.values():
		if node_obj not in notTopNodes:
			topNodes.add(node_obj)
		
		#loop through node_obj nbrs
		for nbr in node_obj.neighbors:
			#nbr will never become topNodes
			notTopNodes.add(nbr)
			
			#remove nbr from topNodes, cuz it is not 0 in-degree node
			if nbr in topNodes:
				topNodes.remove(nbr)

	return topNodes
	
if __name__ == "__main__":
	file_path = input("Please enter the graph path: ")
	graphDict = createGraph(file_path)
	
	result = topoSort(graphDict)
	print("Topo Sort Result")
	print(result)
	
	