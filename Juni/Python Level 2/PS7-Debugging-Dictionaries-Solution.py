"""
Your friend, Kant D. Bugg, is learning how to use dictionaries. Kant wants to use a dictionary to keep track of all his Halloween candy - he has several different types of candy, and wants to keep a count of each type. Unfortunately, his script has some bugs in it. Help Kant find the bugs and get his script running!

Each time you run the code, read the error messages in the console. Each message will tell you which line to look for a bug, and even give you a hint about what the bug is. After you find and fix the bug, run the code again. Read the new error message and find the next bug, until the program runs fully! If you can't remember how to fix a certain line of code, look at one of your past projects for an example. You can copy and paste Kant's buggy code into your file from here: https://repl.it/@JuniLearning/PS7-Debugging-Dictionaries.
"""

# I have 15 Snickers, 7 Almond Joys, 6 Twix, 9 Kit Kats, 3 Reese's Cups, and 2 Butterfingers
candies = {
	"Snickers": 15,
	"Almond Joy": 7,
	"Twix": 6,
	"Kit Kat": 9,
	"Reese's Cups": 3,
	"Butterfingers": 2
}

# Print how many I have of each type of candy
print("A count of each of my candies:")
for candy in candies:
	print(candy + ": " + str(candies[candy]))

# Oops, I forgot that I ate one of each kind of candy. I need to subtract one from each count!
for candy in candies:
	candies[candy] -= 1

# I traded all of my Twixes to my friend for 4 Junior Mints
candies["Twix"] = 0
candies["Junior Mints"] = 4

print()
print("An updated count of each of my candies:")
for candy in candies:
	print(candy + ": " + str(candies[candy]))

# Bonus: Calculate and print out the total pieces of candy I now own
'''
total = 0
for candy in candies:
  total += candies[candy]
print("I now have " + str(total) + " pieces of candy!")
'''
