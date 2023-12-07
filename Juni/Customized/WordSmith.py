import random
import itertools
import time

# I could set the program to continuously make a set of letters and a list of corresponding words and then write that to a file that it reads later for added speed

# reads words into list
with open("valid_words.txt") as f:
    validWords = f.readlines()
    validWords = [x.strip() for x in validWords]

allValidWords = []

#
# input("Welcome to Type Racer. Press Enter to play.")
# time.sleep(1)
# print("Ready.......")
# time.sleep(1)
# print("Set.......")
# time.sleep(1)
# print("Go.......")

#
while True:
    letters = set()
    wordFound = False
    allValidWords = []
    lettersComb = []

    while len(letters) < 7:
        startNum = ord('a')
        endNum = ord('z')
        randomNum = random.randint(startNum, endNum)
        letter = chr(randomNum)
        letters.add(letter)

    for i in range(1, len(letters) + 1):
        lettersComb = [''.join(comb) for comb in list(itertools.permutations(letters, i))]  # Here we use '=' to reset it each time so as not to waste time repeating combinations from previous iterations
        for comb in lettersComb:
            if comb in validWords:
                allValidWords.append(comb)

    if len(allValidWords) != 0:
        break
print(letters)
print(allValidWords)

#   For Quicker Runtime, use:   #
"""
lettersComb = []
for i in range(1, len(letters)+1):
  lettersComb.extend([''.join(comb) for comb in list(itertools.permutations(letters, i))])
  for comb in lettersComb:
    if comb in validWords:
      break
  else:
    lettersComb = [] # initialize to save time on repetition of loop processing
    continue  # only executed if the inner loop did NOT break
  break  # only executed if the inner loop DID break
"""

#   To print all the available words, use:   #
"""
for i in range(1, len(letters) + 1):
    lettersComb = [''.join(comb) for comb in list(itertools.permutations(letters, i))]  # Here we use '=' to reset it each time so as not to waste time repeating combinations from previous iterations
    for comb in lettersComb:
        if comb in validWords:
            allValidWords.append(comb)

if len(allValidWords) != 0:
    break
"""



# ideas for hint, create a list of found words (including hints given),
# Then when a hint is asked for, loop until one is found then exit
# this saves time from having to find all possible words

# Also, maybe count all found words of each length and give that as a hint

#
print("Your random letters are:")
print(letters)
while True:
    isValidWord = True
    word = input("enter a word:")
    # Will probably want to implement hint version to greatly speed up runtime
    while word == "?":
        for vWord in allValidWords:
            print(vWord, end=", ")
        print()
        word = input("enter a word:")

    for letter in word:
        if letter not in letters:
            print("try again")
            isValidWord = False
            # add something here
    if word not in validWords:
        print("try again")
        isValidWord = False
    else:
        print("valid word")  # Print score as well
        if word in allValidWords:
            allValidWords.remove(word)
    # for letter in word, if letter not in letters: error
    # if word not in valid words: error
    # else points
