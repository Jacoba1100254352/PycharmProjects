import random


def clear():
	print("\033c", end="")


def getCorrect(code, guess):
	numCorrect = 0
	for i in range(len(guess)):
		if code[i] == guess[i]:
			numCorrect += 1
	return numCorrect


def getClose(code, guess):
	# remove correct digits from both strings
	newCode = ""
	newGuess = ""
	for i in range(len(guess)):
		if code[i] != guess[i]:
			newCode += code[i]
			newGuess += guess[i]
	code = newCode
	guess = newGuess
	
	# calculate the correct number of close digits
	numClose = 0
	while len(code) > 0:
		for i in range(len(guess)):
			if guess[i] == code[0]:
				guess = guess[0:i] + guess[i + 1:]
				numClose += 1
				break
		code = code[1:]
	return numClose


def createSecretCode(digits):
	code = ""
	for i in range(digits):
		code += str(random.randint(0, 4))
	return code


# ------------------------------------------------------------------

RULES = '''Mastermind
The secret code is composed of 4 random digits between 0-4.

Enter a 4 digit guess and see how close you are!
\t-Correct: correct number, correct location
\t-Close: correct number, incorrect location
'''

print(RULES)
input("Press enter to start:")
clear()

NUM_DIGITS = 4
correct = 0
close = 0
code = createSecretCode(NUM_DIGITS)

while correct < NUM_DIGITS:
	
	while True:
		guess = input("Type in a " + str(NUM_DIGITS) + " digit guess (0-4): ").strip()
		if len(guess) == NUM_DIGITS and guess.isdigit():
			break
	
	correct = getCorrect(code, guess)
	close = getClose(code, guess)
	print("Correct:", correct)
	print("Close:", close)
	print()

print("YOU WIN!!")
