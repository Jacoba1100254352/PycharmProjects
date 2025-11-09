"""
Write a function that translates a word into Juni Latin (a simplified version of Pig Latin). The rules for translation are: add the first letter of the word and the suffix "ay" to the end of the original word to create the Juni Latin word! Using this function, ask the user for a word and output its Juni Latin translation.
"""


def translate(word):
	newWord = ""
	
	for i in range(1, len(word)):
		newWord += word[i]
	
	newWord += word[0] + 'ay'
	
	return newWord


word = input("Enter a word to translate into Juni Latin: ")
print("The word " + word + " in Juni Latin is " + translate(word))
