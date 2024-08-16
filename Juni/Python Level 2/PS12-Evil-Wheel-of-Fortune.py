import random


def clear():
	print("\033", end="")  # "\033c"


def getGuess():
	while True:
		guess = input("Enter a guess: ").lower().strip()
		if guess in previousGuesses:
			print("You already guessed that! Try again!")
		elif not guess.isalpha():
			print("That's not a letter! Try again!")
		elif len(guess) != 1:
			print("You typed too much, or nothing at all! Try again!")
		else:
			return guess


def getGroups(guessedLetter, words):
	# Get groups of similar words
	wordGroups = {}
	for word in words:
		# Get all the words
		pattern = getPattern(guessedLetter, word)
		if pattern in wordGroups:  # add each word that follows the pattern to the dictionary with that pattern as the key
			wordGroups[pattern].add(word)
		else:  # otherwise make a new dictionary entry
			wordGroups[pattern] = {word}
	return wordGroups


def getPattern(guessedLetter, word):
	pattern = ""
	# Get add all possible patterns and options given the letter(s) guessed for each word (a_d, b_d, __d etc..., then return to getGroups)
	for letter in word:
		if letter == guessedLetter or letter in correctGuesses:
			pattern += letter
		else:
			pattern += "_"
		pattern += " "
	return pattern


def getMaxPattern(wordGroups):  # add all the patterns that have the highest possibility of producing lots of words
	maxGroupSize = 0
	maxPatterns = []
	for pattern in wordGroups:
		if len(wordGroups[pattern]) > maxGroupSize:
			maxGroupSize = len(wordGroups[pattern])
			maxPatterns = [pattern]
		elif len(wordGroups[pattern]) == maxGroupSize:
			maxPatterns.append(pattern)
	return random.choice(maxPatterns)  # choose one at random (assuming there are more than one, or just pick the (only) one that exists)


def getWordsOfLength(length, words):
	temp = set()
	for word in words:
		if len(word) == length:
			temp.add(word)
	return temp


# -----------------------------------------------------

with open("dictionary.txt") as f:
	words = set(f.read().strip().split("\n"))

length = random.randint(3, 8)
status = "_ " * length

words = getWordsOfLength(length, words)

correctGuesses = set()
previousGuesses = []
numGuesses = 15

while True:
	clear()
	print(status + "\n")
	print(str(numGuesses) + " guesses left!")
	print("Previous Guesses: " + " ".join(previousGuesses))
	
	guess = getGuess()
	previousGuesses.append(guess)
	
	# choose the worst case scenario (that's still possible)
	wordGroups = getGroups(guess, words)  # returns a dictionary
	newStatus = getMaxPattern(wordGroups)  # returns a random viable pattern (e.g. __d)
	
	# update words and status
	words = wordGroups[newStatus]
	if newStatus == status:  # "incorrect guess", no change has occurred
		# the worst case (that's still possible) is to not reveal any letters!
		numGuesses -= 1
	else:  # "correct guess"
		# the worst case (that's still possible) is to reveal letters...
		correctGuesses.add(guess)
		status = newStatus
	
	if "_" not in status:
		print("\nYOU WIN!\nThe word was: " + list(words)[0])
		break
	elif numGuesses == 0:
		print("\nYOU LOSE!\nThe word was: " + random.choice(list(words)))
		break
