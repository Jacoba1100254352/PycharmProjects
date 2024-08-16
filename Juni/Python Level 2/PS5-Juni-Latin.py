def translate(word):
	newWord = ""
	
	for i in range(1, len(word)):
		newWord += word[i]
	
	newWord += word[0] + 'ay'
	
	return newWord


word = input("Enter a word to translate into Juni Latin: ")
print("The word " + word + " in Juni Latin is " + translate(word))
