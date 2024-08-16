import random


# Create two sets. In each set, add 5 different random numbers between 1 and 10. Then, print out these two sets, the union of these two sets, and the intersection of these two sets.

a = set()
b = set()

while len(a) < 5:
	a.add(random.randint(1, 10))

while len(b) < 5:
	b.add(random.randint(1, 10))

print(a)
print(b)
print(a.union(b))
print(a.intersection(b))

# For your second random set, either print out "The number 1 is inside the second set" or "The number 1 is not inside the second set"

if 1 in b:
	print("The number 1 is inside the second set")
else:
	print("The number 1 is not inside the second set")

# Ask the user for a word. Then, use a set to print out all of the unique letters in the word and the number of unique letters in the word.

word = input("Give me a word: ")
letters = set()
for letter in word:
	letters.add(letter)
print(letters)
print("This word has " + str(len(letters)) + " unique letters")

# Ask the user for another word. Print out the letters these two word have in common.

word2 = input("Give me another word: ")
letters2 = set()
for letter in word2:
	letters2.add(letter)

print(letters.intersection(letters2))


# Write a function that takes in a set of numbers and returns a set with only the even numbers from that set.

def getEvens(s):
	newSet = set()
	for num in s:
		if num % 2 == 0:
			newSet.add(num)
	return newSet


s = set()
s.add(1)
s.add(2)
s.add(3)
s.add(4)
print(getEvens(s))


# Write a function that takes in a set of words and returns a set with only the words that have 3 letters in them.

def getThreeLetterWords(s):
	newSet = set()
	for word in s:
		if len(word) == 3:
			newSet.add(word)
	return newSet


s = set()
s.add("cat")
s.add("bat")
s.add("house")
print(getThreeLetterWords(s))
