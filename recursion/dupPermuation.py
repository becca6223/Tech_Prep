def allPermutations(string):
	##Compute all the permutaions with a given string
	list_str = []
	new_str = ""
	sort_str = sorted(string)
	getAllPermHelper(sort_str, new_str, list_str)

	return list_str



def getAllPermHelper(string, new_str, list_str):
	if len(string) == 1:
		list_str.append(new_str + string[0])
		return 

	used_char = set()
	for loc, i in enumerate(string):
		if i not in used_char:
			mod_str = string[0:loc] + string[loc+1:]
			getAllPermHelper(mod_str, new_str + i, list_str)
			used_char.add(i)

	return


if __name__ == "__main__":
	string = "aabb"
	result_list = allPermutations(string)
	print(result_list)
