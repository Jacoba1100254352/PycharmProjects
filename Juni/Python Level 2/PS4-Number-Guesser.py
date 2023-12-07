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
