"""
Program a number guessing game, in which the computer picks a random number from 1 to 50 and the user tries to guess the number. The computer should tell the user whether their guess was too low or too high, and at the end it should print the number of guesses it took to get to the correct number.

Note: To have the computer pick a random number, import the random module at the beginning of your program, and then randNum = random.randint(1,50) will save a random number between 1 and 50 in randNum.
"""

import random


randNum = random.randint(1, 50)
numGuesses = 1

guess = int(input("I am thinking of a random number between 1 and 50. Guess what it is! "))

while guess != randNum:
	if guess > randNum:
		print("That's too high!")
	else:
		print("That's too low!")
	
	guess = int(input("Enter a new guess: "))
	numGuesses += 1

print("You got it! I was thinking of the number " + str(guess) + "!")
print("It took you " + str(numGuesses) + " tries to guess my number.")
