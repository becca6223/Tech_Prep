#practice trie data structure (memory not efficient because each node(character) will have 26 pointers for each character
#for efficiency, check out ternary search tree
class TrieNode:
	def __init__(self):
		self.children = [None] * 26
		self.isEndWord = False
	
class Trie:
	def __init__(self):
		self.root = self.getNode()
	
	def getNode(self):
		return TrieNode()

	def getCharPosition(self, char):
		return ord(char) - ord('a')
	
	def insert(self, key):
		temp = self.root

		for cur_char in key:
			cur_char_pos = self.getCharPosition(cur_char)
			if temp.children[cur_char_pos] == None:
				#create a new node 
				temp.children[cur_char_pos] = self.getNode()
			
			#update temp to the cur_char 
			temp = temp.children[cur_char_pos]

		temp.isEndWord = True
			
	def search(self, key):
		temp = self.root

		for cur_char in key:
			cur_char_pos = self.getCharPosition(cur_char)
			if temp.children[cur_char_pos] is None:
				return False
			
			temp = temp.children[cur_char_pos]

		return True if temp.isEndWord else False

	
def insertWords(list_words, root):
	for cur_word in list_words:
		root.insert(cur_word)
			
def searchWords(list_words, root):
	for cur_word in list_words:
		result = root.search(cur_word)
		
		if result:
			print(cur_word + " exist in Trie!")
		else:
			print(cur_word + " doesn't exist in Trie!")


if __name__ == "__main__":
	root = Trie()
	list_words = input("Enter a list of words: ")
	list_words = list_words.strip().split(" ")

	insertWords(list_words, root)

	search_words = input("Enter a list of word to be searched: ")
	search_words = search_words.strip().split(" ")
	searchWords(search_words, root)

