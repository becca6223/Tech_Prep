#practice dijkstra algorithm 

#Psuedo code of dijstra algorithm 
'''
Logic flow 
1. create a minimum distance set 
2. create a set that keep tracks of current nodes with sorted distance in ascending order
3. initialize all other nodes' distance as infinity 
4. initialize source distance as 0
5. add source to tracking_set 
6. retrieve the next node in tracking set with min distance
7. add to minimum dist set 
8. process selected node neighbors and update neighbors' dist accordinly if the calc dist is shorter
(look back to step6, stop until no more node in tracking_set)

MODIFICATION:
what if you want to store the shortest path to all neighbors ?? 
(How to do it space efficiently)
'''
INFINITY = 999

class Node:
	def __init__(self, name):
		self.name = name
		self.neighbors = {}
	

def createGraph(file_path):
	graphDict = {}
	
	with open(file_path, 'r') as fp:
		content = fp.readlines()
		content = [i.strip() for i in content] #a list of string with source, dest, cost
		
		#build undirected graph 
		for curr in content:
			info = curr.split(" ")
			source = info[0]
			dest = info[1]
			cost = int(info[-1])
			
			#check if source exists and either create a new obj or retrieve one
			if source not in graphDict:
				source_node = Node(source)
				graphDict[source] = source_node
			else:
				source_node = graphDict[source]
			
			#check if dest exists and either create a new obj or retrieve one
			if dest not in graphDict:
				dest_node = Node(dest)
				graphDict[dest] = dest_node
			else:
				dest_node = graphDict[dest]
			
			setUpNbr(source_node, dest_node, cost)
			setUpNbr(dest_node, source_node, cost)			
	
	return graphDict
	
def setUpNbr(source, dest, cost):	
	source.neighbors[dest] = cost
	

def dijkstra(graph, source):
	'''
	graph: dict type. key: node_id, value: node object
	source: the source of the graph
	'''
	
	min_nodes = []
	remain_nodes = setUpRemainNodes(graph, source) # a list of list with nodes and costs
	total_nodes = len(graph)
	
	
	for i in range(0, total_nodes):
		cur_min_id = findMin(remain_nodes)
		cur_min_cost = remain_nodes.pop(cur_min_id, None)
		print(cur_min_id, cur_min_cost)
		print(remain_nodes)
		min_nodes.append([cur_min_id, cur_min_cost]) #add cur_min_node to min_nodes
		
		#extract info
		cur_min_node = graph[cur_min_id]
		
		#go through cur_min_node's neighbors
		#cur_min_node[0] is node_id
		for nbr, cost in cur_min_node.neighbors.items():
			nbr_id = nbr.name
			if nbr_id in remain_nodes:
				#nbr of node_id, nbr is Node type
				compute_cost = cost + cur_min_cost
				if compute_cost < remain_nodes[nbr_id]:
					remain_nodes[nbr_id] = compute_cost

	return min_nodes
	
def setUpRemainNodes(graph, source):
	global INFINITY
	remain_nodes = {}
	
	for i in graph:
		if i == source.name:
			remain_nodes[i] = 0
		else:
			remain_nodes[i] = INFINITY
			
	return remain_nodes
	

def findMin(remain_nodes):
	global INFINITY
	min_cost = INFINITY
	min_id = ""
	
	for id, cost in remain_nodes.items():
		if cost < min_cost:
			min_cost = cost
			min_id = id
	
	return min_id
	
	
if __name__ == "__main__":
	file_path = input("Please enter the graph path: ")
	graphDict = createGraph(file_path)
	
	select_id = input("Enter the node ID for the source: ")
	source_node = graphDict[select_id]
	
	result = dijkstra(graphDict, source_node)
	print("Source:", source_node.name)
	print("shortest path from source node to all other nodes")
	print(result)
	
	
	
	