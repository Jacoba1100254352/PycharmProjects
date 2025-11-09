"""
Write a program where the correct password is saved as a string in a variable in the code, and the user has to continuously guess until they get the correct password. Once the user guesses correctly, print the number of guesses it took!
"""

password = "ilovecs"

userGuess = input("Enter the password: ")
numGuesses = 1
while userGuess != password:
	userGuess = input("Incorrect password. Try again: ")
	numGuesses = numGuesses + 1

print("System unlocked! It took you " + str(numGuesses) + " tries to guess the password.")
