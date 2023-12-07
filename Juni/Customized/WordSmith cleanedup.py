import random
import itertools

# Read words from the file into a list
with open("valid_words.txt") as f:
    validWords = [x.strip() for x in f.readlines()]

allValidWords = []

# Generate a set of random letters and check for valid words using those letters
while True:
    letters = set()
    lettersComb = []

    # Generate a set of 7 unique random letters
    while len(letters) < 7:
        randomLetter = chr(random.randint(ord('a'), ord('z')))
        letters.add(randomLetter)

    # Check for valid words using combinations of the random letters
    for i in range(1, len(letters) + 1):
        lettersComb = [''.join(comb) for comb in list(itertools.permutations(letters, i))]  # Here we use '=' to reset it each time so as not to waste time repeating combinations from previous iterations
        for comb in lettersComb:
            if comb in validWords:
                allValidWords.append(comb)

    if len(allValidWords) != 0:
        break

    print("Your random letters are:", letters)

    # Allow the user to guess words using the random letters
    while True:
        validWord = True
        word = input("Enter a word (or ? for a hint):")

        # If the user requests a hint
        if word == "?":
            print(", ".join(allValidWords))
            continue

        # Check if the word contains only the random letters and if it's a valid word
        if not all(letter in letters for letter in word) or word not in validWords:
            print("Try again.")
        else:
            print("Valid word!")
            if word in allValidWords:
                allValidWords.remove(word)
