# FUNCTIONS

#########################################

# What is a function? Can you give me an example of a built-in function in Python?

# Define a function that takes in two numbers and returns the product of those two numbers
def mult(x, y):
	return x * y


# Using the function you wrote above, print the product of 15 and 22.
print(mult(15, 22))

# Let’s play a game! 1. Make a variable that is randomly set to either 0 or 1 (this tracks whether the player wins or not). Make another variable that contains a random number from 1 to 1000 (this is how much money the player wins). Now let’s play the lottery! 2. Define a function that takes in the two random variables we created. The function should return a string that either tells the player that they lost, or tells the player how much money they won. 3. Print a message that welcomes the user to the lottery, and then calls the function to play the game.

import random


lotto = random.randint(0, 1)
money = random.randint(1, 1000)


def lottery(lotto, money):
	if lotto == 1:
		return ("You won " + str(money) + " dollars!")
	else:
		return ("Sorry, you lost.")


print("Welcome to the lottery. \nChecking the results...")
print(lottery(lotto, money))

############################################

# LISTS

#############################################

# What is a list?

# Create an empty list called guests
guests = []

#  Let’s make a guest list for a birthday party! Add 3 friends you’d like to invite to your empty list, without typing directly in our original code to create our list.
guests.append("John")
guests.append("Sarah")
guests.append("Raul")
print(guests)

# Oh no! We have too many guests. Uninvite one guest by taking them out of the guest list. Then, print out our finalized guest list so we know who’s coming! 
guests.remove("John")
print(guests)

# Now, print only the first name in the list.
print(guests[0])

# To make a finalized guest list, print "My guest list: " and each name on a separate line below. 
print("My guest list: ")
for i in range(len(guests)):
	print(guests[i])

# Let’s try this out with some numbers: using a loop, add the numbers 1 to 20 to a list called nums. Print the list.
nums = []
for i in range(1, 21):
	nums.append(i)

# Now, add add only the even numbers between 1 and 20 to a list called evens. Print the list.
evens = []
for i in range(1, 21):
	if i % 2 == 0:
		evens.append(i)
print(evens)

############################################

# DICTIONARIES

############################################

# What is a dictionary? Why are dictionaries useful?

# Create a dictionary with 3 of your favorite athletes and their corresponding jersey numbers.
players = {"LeBron": 23, "Ramos": 4, "Ronaldo": 7}

# Look up and print out the number of one of the players in your dictionary. 
print(players["Ramos"])

# On a new line, add one more player to the dictionary, without typing directly in our original code to create the dictionary.
players["Messi"] = 10
print(players)

# For all the players in your dictionary, print only the player names. Then, print only the player numbers.
for key in players:
	print(key)
	print(players[key])

# Let’s make sure you added my favorite basketball player to the dictionary. Check if Steph Curry is in the dictionary, and print a message if he is. 
if "Steph Curry" in players:
	print("Yep, Steph is included!")
# add a different message if he’s not in the dictionary.
else:
	print("Oh no! He's not included")

# Now, add to the above code so that if Steph is NOT already in the dictionary, it adds him in.  Print the new dictionary.
if "Steph Curry" in players:
	print("Yep, Steph is included!")
else:
	print("Oh no! Adding him now.")
	players["Steph Curry"] = 30
print(players)

# Create a dictionary with 15 key-value pairs, where the keys are a random number between 0 and 1000, and the values are the number of digits that the key contains. 
import random


digits = {}
for i in range(15):
	key = random.randint(0, 1000)
	digits[key] = len(str(key))
print(digits)

############################################

# SETS

############################################

# What is a set? What qualities does it have?

# Create an empty set called recipe
recipe = set()

# Look up a recipe. Add at least 3 ingredients to your set that you’ll need. 
recipe.add("garlic")
recipe.add("onion")
recipe.add("salt")
print(recipe)

# Oops! You realized you already had one of the ingredients at home. Remove one item from the set. 
recipe.remove("onion")
print(recipe)

# Create another set called recipe2 and add your ingredients there (you can type directly in the set). Now let’s get our final grocery list: create a set called ingredients that contains all ingredients in either or both sets. Print the new set.
recipe2 = {"apple", "cinnamon", "salt"}
ingredients = recipe.union(recipe2)
print(ingredients)

# We’ll want to buy more of the ingredients that the two recipes have in common. Print out the ingredients that appear in both sets.
print(recipe.intersection(recipe2))

# We’re at the grocery store, and want to check if garlic was one of our ingredients we need to buy. Print a message to the user to tell them whether garlic is in both sets, one of the sets, or neither. (Note: Try to do this using conditionals, but try not to use 'and' or 'or'!)
if "garlic" in recipe.intersection(recipe2):
	print("Garlic is in both of our recipes")
elif "garlic" in recipe.union(recipe2):
	print("Garlic is in one of our recipes")
else:
	print("Garlic is not in either recipe")

# Save one of our ingredients, “banana”, in a variable. Add all the letters in the variable into a set. In the case of “banana”, what do you think the set will contain?
fruit = "banana"
letters = set()
for x in fruit:
	letters.add(x)
# before printing: what will the set contain?
print(letters)

# In a recipe, why might we want to use a set for ingredients, but a list for the cooking instructions? Can you think of a way a dictionary could be useful when making a recipe?

# ex: 1. In a case where we just want the full list of all ingredients used, and we don't care if it was used in more than one food. 2. Cooking instructions need to be in order - or else we'd have a mess! 3. It could hold an ingredient, and its corresponding quantity/measurement

############################################

# OPTIONAL ADVANCED PROJECTS

############################################

# Ask the user to write a sentence. Print the set of unique letters used in the sentence, and tell the user the number of different letters contained in the sentence
sentence = input("Write a sentence: ")
letters = set()
for letter in sentence:
	letters.add(letter)
print(letters)
print("There are " + str(len(letters)) + " different letters in your sentence")

# Let’s see how big of a vocabulary our favorite authors (or lyricists) have! Ask the user to copy in a paragraph from their favorite book (or other piece of writing). Create a set of all the unique words, and print a message telling the user the number of different words contained in the paragraph out of the total number of words.
paragraph = input("Copy in a paragraph from your favorite book!")

wordslist = paragraph.split()
words = set(wordslist)
print(words)
print("This text has " + str(len(words)) + " unique words out of " + str(len(wordslist)) + " total words")
