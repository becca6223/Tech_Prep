#Recommend a friend with most mutual friends 
class Node:
	def __init__(self, name):
		self.name = name
		self.neighbors = {}

def createFriendNetwork(file_path):
	graphDict = {}
	
	with open(file_path, 'r') as fp:
		content = fp.readlines()
		content = [i.strip() for i in content] #a list of string with source, dests
		
		#build undirected graph 
		for curr in content:
			info = curr.split(" ")
			source = info[0]
			dest = info[1:]
			
			#check if source exists and either create a new obj or retrieve one
			if source not in graphDict:
				source_node = Node(source)
				graphDict[source] = source_node
			else:
				source_node = graphDict[source]
			
			#check if dest exists and either create a new obj or retrieve one
			for cur_dest in dest:
				if cur_dest not in graphDict:
					dest_node = Node(cur_dest)
					graphDict[cur_dest] = dest_node
				else:
					dest_node = graphDict[cur_dest]
				
				setUpNbr(source_node, dest_node)
				setUpNbr(dest_node, source_node)			
	
	return graphDict

def setUpNbr(source, dest):
	source.neighbors[dest.name] = dest
	
def recommendMostMutalFriend(friendGraph, source):
	max_cnt = 0
	recommendFriend = ""
	
	source_node = friendGraph[source]
	source_friends_set = set(source_node.neighbors.keys())
	
	for friend, friend_node in source_node.neighbors.items():
		for frnd_frnd, frnd_frnd_node in friend_node.neighbors.items():
			if frnd_frnd == source or frnd_frnd in source_friends_set:
				#don't recommend someone who is your friend already or if it's yourself
				pass 
			else:
				frnd_frnd_frnd_set = set(frnd_frnd_node.neighbors.keys())
				mutual_friends = frnd_frnd_frnd_set.intersection(source_friends_set)
				num_mutual_friends = len(mutual_friends)
				if num_mutual_friends > max_cnt:
					max_cnt = num_mutual_friends
					recommendFriend = frnd_frnd
					print(frnd_frnd)
				elif num_mutual_friends == max_cnt:
					print("Same mutual num friends ", frnd_frnd)

	return recommendFriend
	
if __name__ == "__main__":
	file_path = input("Enter a file path for friends network: ")
	friendGraph = createFriendNetwork(file_path)
	friend_name = input("Enter a friend's name: ")
	result = recommendMostMutalFriend(friendGraph, friend_name)
	print("Recommended friend with most mutual friends with " + friend_name)
	print(result)
	
	