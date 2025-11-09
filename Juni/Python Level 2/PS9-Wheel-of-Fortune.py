"""
Program the Wheel of Fortune, as shown in the graphic below! Write out pseudocode in your code comments to plan out the program flow and data structures you'll need to set up.
"""

correctWord = "programming"
guessedLetters = set()
numGuessesRemaining = 15

# fill up set with the correct letters
# Pythonic shortcut: correctLetters = set(correctWord)
correctLetters = set()
for letter in correctWord:
	correctLetters.add(letter)

print("Welcome to the Wheel of Fortune! You have " + str(
	numGuessesRemaining) + " guesses to figure out the correct word. Good luck!")

# alternatively, could use while numGuessesRemaining > 0
while True:
	# print out the current state of the guessed word
	currentState = ""
	for letter in correctWord:
		if letter in guessedLetters:
			currentState += letter + " "
		else:
			currentState += "_ "
	print(currentState)
	print("")
	
	# ask for a guess
	guessedLetter = input("Guess a letter! You have " + str(numGuessesRemaining) + " guesses remaining.")
	numGuessesRemaining -= 1
	
	# add the guessed letter to the set if it's a correct letter
	if guessedLetter in correctLetters:
		guessedLetters.add(guessedLetter)
	
	# check if all of the letters have been guessed
	if len(guessedLetters) == len(correctLetters):
		print("Congratulations, you win!")
		break
	
	# check if the player is out of guesses
	if numGuessesRemaining == 0:
		print("Sorry, you're out of guesses!")
		break
