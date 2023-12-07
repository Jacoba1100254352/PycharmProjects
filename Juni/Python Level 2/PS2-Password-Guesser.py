password = "ilovecs"

userGuess = input("Enter the password: ")
numGuesses = 1
while userGuess != password:
    userGuess = input("Incorrect password. Try again: ")
    numGuesses = numGuesses + 1

print("System unlocked! It took you " + str(numGuesses) + " tries to guess the password.")
