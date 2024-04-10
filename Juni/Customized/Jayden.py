def allSubstrings(_input_string):
	substrings = []
	
	for i in range(0, len(_input_string) - 1):
		for j in range(i + 1, len(_input_string)):
			substring = _input_string[i:j]
			substrings.append(substring)
	
	return substrings


allSubstrings("Tacos")
