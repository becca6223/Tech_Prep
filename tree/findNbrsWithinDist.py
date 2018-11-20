#return all the neighbors that can be reached within a distance (inclusive)

#Question to ask:
# 1. acylic or cyclic 
# 2. directed or undirected 
# 3. 


#Test examples 
# 

#Possible approace - BFS/DFS 
# Try both 

class BusinessLayout:
	def __init__(self, name):
		self.name = name
		self.neighbors = {}
		
	def setUpNeightbors(self, neighbors:list, cost:list):
		for i, j in zip(neighbors, cost):
			self.neighbors[i] = j


def findAllNeighbors(source, distance):
	#BFS method
	queue = []
	visited = []
	reachable_nbr = []
	
	queue.append((source, 0)) #need to include relative distance to the source 
	
	while queue != []:
		curr, curr_dist = queue.pop(0) 
		visited.append(curr.name) #visit the node 
		
		#visit curr's neighbors 
		for key, value in curr.neighbors.items():
			if key.name not in visited:
				new_dist = value + curr_dist
				if new_dist <= distance:
					reachable_nbr.append(key.name)
					queue.append((key, new_dist))
				
	return reachable_nbr

	
def wrapperDFS(source, distance):
	visited = []
	result = []
	findAllNeighborsDFS(source, distance, 0, visited, result)
	
	return result
		
		
def findAllNeighborsDFS(source, distance, cur_distance, visited, result):
	#you are currently visiting source node 
	#so add that source into visisted list 
	visited.append(source.name)
	
	if cur_distance <= distance:
		if cur_distance != 0: 
			#not itself
			result.append(source.name)
	
		for nbr, dist in source.neighbors.items():
			if nbr.name not in visited:
				#visit this nbr if has not been visited yet
				findAllNeighborsDFS(nbr, distance, cur_distance + dist, visited, result)
	else:
		# no need to continue 
		return

if __name__ == "__main__":
	cont = True
	businessUnitsDict = {}
	
	while cont:
		source = input("Enter a source: ")
		neighbors = input("Enter new neighbors: ")
		onecost = input("Enter cost to get from source to neighbors: ")
		neighbors = neighbors.strip().split(" ")
		cost = [int(i) for i in onecost.strip().split(" ")]

		neighbors_obj = []
		
		for i in neighbors:
			if i not in businessUnitsDict:
				curr = BusinessLayout(i)
				businessUnitsDict[i] = curr
			else:
				curr = BusinessUnitsDict[i]
			
			neighbors_obj.append(curr)
		
		#set up neighbors for source
		if source not in businessUnitsDict:
			source_obj = BusinessLayout(source)
			source_obj.setUpNeightbors(neighbors_obj, cost)
			businessUnitsDict[source] = source_obj
		else:
			source_obj = businessUnitsDict[source]
			source_obj.setUpNeightbors(neighbors_obj, cost)
			
		#set up source as neighbors' neighbor
		for loc, i in enumerate(neighbors_obj):
			i.setUpNeightbors([source_obj], [cost[loc]])
		
		code = input("Enter 1 to continue")
		if code == '1':
			cont = True
		else:
			cont = False
	
	print("\nStart")
	selected_source = input("Enter a source id: ")
	distance = input("Enter reachable distance: ")
	
	print("BFS")
	reachable_dest = findAllNeighbors(businessUnitsDict[selected_source], int(distance.strip())) 
	print(source, "reachable neighbors within", distance)
	print(reachable_dest)
	
	print("DFS")
	reachable_dest = wrapperDFS(businessUnitsDict[selected_source], int(distance.strip()))
	print(source, "reachable neighbors within", distance)
	print(reachable_dest)
			
		
		
		
		
	
	

	
	

	

	
	
