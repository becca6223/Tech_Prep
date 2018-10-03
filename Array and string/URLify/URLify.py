def replace_percent_20(str1, length):
	result = (str1.strip()).split(" ")
	str2 = "%20".join(result)
	return str2

if __name__ == "__main__":
	str1 = input("Give one string with spaces: ")
	length = input("string length: ")
	result = replace_percent_20(str1, length)
	print(result)
