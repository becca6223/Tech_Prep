from collections import defaultdict

def unique_string(input_str):
	unique = set()
	flag = True
	for char in input_str:
		if char in unique:
			print("the string does not have unique char")
			flag = False
			break
		else:
			unique.add(char)
	if flag:
		print("Unique string!! ", input_str) 

if __name__ == "__main__":
	string = input("pls give a unique string: ")
	unique_string(string)
	
