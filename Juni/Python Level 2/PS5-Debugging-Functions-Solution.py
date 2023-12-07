import random


def printWelcome():
    print("I am thinking of a random number between 1 and 100. Guess what it is!")


# Get my secret number between 1 and 100!
def getRandomNumber():
    return random.randint(0, 100)


# Ask the user to guess my secret number
def getGuessFromUser():
    return int(input("Enter a new guess: "))


# If the guess is correct, then return True. Otherwise, print out if the guess was too high or too low, and return False
def answerIsRight(answer, guess):
    if answer == guess:
        print("You got it!")
        return True
    elif guess < answer:
        print("You guessed too low!")
        return False
    else:
        print("You guessed too high!")
        return False


def printScore(numGuesses):
    print('It took you ' + str(numGuesses) + ' guesses to guess my number.')
    if numGuesses == 1:
        print("Lucky you, you guessed my secret number on the first try!")
    elif numGuesses < 5:
        print("Pretty solid guessing, it took you less than 5 tries to guess my number!")
    elif numGuesses < 15:
        print("Pretty average guessing!")
    else:
        print("Wow, it took you forever to guess my number!")


def playGame():
    printWelcome()
    answer = getRandomNumber()

    # Ask the user to guess the secrete number, then check if they got it right. If they didn't get it right, let them keep guessing until they guess correctly!
    guess = getGuessFromUser()
    numGuesses = 1  # Count how many guesses it took for the user to guess the number
    while not answerIsRight(answer, guess):
        guess = getGuessFromUser()
        numGuesses = numGuesses + 1

    printScore(numGuesses)


playGame()

# Bonus: Allow the user type in Y or N at the end of each game to decide whether or not to play again.

'''
keepPlaying = True
while keepPlaying:
  playGame()
  userAnswer = input("Would you like to play again? (Y/N): ')
  if userAnswer == 'N':
    keepPlaying = False
'''
