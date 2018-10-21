def getAllPerm(string):
	#Compute all the permutaions with a given string with no duplicates
	list_str = []
	new_str = ""
	getAllPermHelper(string, new_str, list_str)

	return list_str



def getAllPermHelper(string, new_str, list_str):
	if len(string) == 1:
		list_str.append(new_str + string)
		return 
	
	for loc, i in enumerate(string):
		mod_str = string[0:loc] + string[loc+1:]
		getAllPermHelper(mod_str, new_str + i, list_str)
	
	return

if __name__ == "__main__":
	string = "1234"
	list_perms = getAllPerm(string)
	print(list_perms)
