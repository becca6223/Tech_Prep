#Group anagram 
from collections import defaultdict
from functools import cmp_to_key
i = 0
def sortAnagram(str_list):
	anagram_dict = defaultdict(list)
	
	#create a dictionary for anagrams
	for cur_str in str_list:
		sorted_str = " ".join(sorted(cur_str))
		anagram_dict[sorted_str].append(cur_str)
	
	i = 0
	for cur_list in anagram_dict.values():
		for cur_str in cur_list:
			str_list[i] = cur_str
			i += 1

def cmp_to_key(mycmp):
    'Convert a cmp= function into a key= function'
    class K(object):
        def __init__(self, obj, *args):
            self.obj = obj
        def __lt__(self, other):
            return mycmp(self.obj, other.obj) < 0
        def __gt__(self, other):
            return mycmp(self.obj, other.obj) > 0
        def __eq__(self, other):
            return mycmp(self.obj, other.obj) == 0
        def __le__(self, other):
            return mycmp(self.obj, other.obj) <= 0  
        def __ge__(self, other):
            return mycmp(self.obj, other.obj) >= 0
        def __ne__(self, other):
            return mycmp(self.obj, other.obj) != 0
    return K			
			
def sort_practice(a_list):
	print(sorted(a_list, key=cmp_to_key(mycmp)))
	

def mycmp(a, b):
	a_str = "".join(sorted(a))
	b_str = "".join(sorted(b))
	print(a_str, b_str)
	
	global i 
	if a_str == b_str:
		i = i + 1
		return i
	else:
		return -1
	
if __name__ == "__main__":
	select = input("Enter 1 for sort, 0 for group anagram: ")
	if int(select) == 1:
		num_list = input("Enter a list of string: ")
		num_list =  num_list.split(" ")
		sort_practice(num_list)
	else:
		str_list = input("Enter a list of strings: ")
		str_list = str_list.split(" ")
		sortAnagram(str_list)
		print(str_list)