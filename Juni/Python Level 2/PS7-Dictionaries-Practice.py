"""
Create a dictionary where there are five key-value pairs. Each key should be a word in English language and each value should be the word's definition. Then, print out the dictionary.
Create a dictionary where the keys are the numbers 1 to 25 and the values are their squares. Then, print out the dictionary.
Create a dictionary where the keys are the numbers 1 to 25 and the values are their factorials. Then, print out the dictionary. Try to write your factorial function from the other day from scratch!
Challenge: Ask the user for a word. Create a dictionary where the keys are the letters in the word and the values are the number of times each letter appears in the word. Then, print out the dictionary.
"""

# Create a dictionary where there are five key-value pairs. Each key should be a word in English language and each value should the word's definition. Then, print out the dictionary.

words = {}
words[
	"cake"] = "a sweet, baked, breadlike food, made with or without shortening, and usually containing flour, sugar, baking powder or soda, eggs, and liquid flavoring"
words[
	"chocolate"] = "a preparation of the seeds of cacao, roasted, husked, and ground, often sweetened and flavored, as with vanilla"
words["sherbert"] = "a frozen fruit-flavored mixture, similar to an ice, but with milk, egg white, or gelatin added"
words[
	"pie"] = "a dessert consisting of a filling (as of fruit or custard) in a pastry shell or topped with pastry or both"
words["jello"] = "a gelatin dessert"
print(words)

# Create a dictionary where the keys are the numbers 1 to 25 and the values are their squares. Then, print out the dictionary.

squares = {}
for i in range(1, 26):
	squares[i] = i * i
print(squares)


# Create a dictionary where the keys are the numbers 1 to 25 and the values are their factorials.  Then, print out the dictionary. Try to write your factorial function from the other day from scratch!

def factorial(n):
	answer = 1
	for i in range(1, n + 1):
		answer *= i
	return answer


factorials = {}
for i in range(1, 26):
	factorials[i] = factorial(i)
print(factorials)

# Challenge: Ask the user for a word. Create a dictionary where the keys are the letters in the word and the values are the number of times each letter appears in the word.  Then, print out the dictionary.

word = input("Type in a word: ")
letters = {}
for letter in word:
	if letter in letters:
		letters[letter] += 1
	else:
		letters[letter] = 1
print(letters)
