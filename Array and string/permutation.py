def check_permutation(str1, str2):
	a = sorted(str1)
	b = sorted(str2)
	if a == b:
		return True
	else:
		return False


if __name__ == "__main__":
	str1 = input("Give first string input: ")
	str2 = input("Give sec string input: ")
	result = check_permutation(str1, str2)
	print("are str1 and str2 permutation of each other: ", result)
