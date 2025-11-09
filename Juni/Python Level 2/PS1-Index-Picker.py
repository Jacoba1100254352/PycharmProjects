"""
Ask the user to enter a word, and then an index (i.e. a number). Then, print out the word the user entered and the letter at the index the user entered.
"""

word = input("Enter a word: ")
index = int(input("Enter an index: "))

print("The word you entered was: " + word)
print("The letter at index " + str(index) + " of " + word + " is: " + word[index])

range(1, 10)
