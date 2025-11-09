"""
Make a quiz game that tests the user on their US capitals! The starter code reads in a list of states stored in the variable states and their corresponding capitals stored in capitals. Make the game continuously quiz the user on the capital of a random state until they answer incorrectly, and at the end print out their score! As a bonus, you can add in a reverse option to guess the state, given the capital.
"""

import random


# read in states
f = open("states.txt")
data = f.readlines()
states = [line.strip() for line in data]
f.close()

# read in capitals
f = open("capitals.txt")
data = f.readlines()
capitals = [line.strip() for line in data]
f.close()

# construct dictionary of state-capital pairs
d = {}
for i in range(len(states)):
	d[states[i]] = capitals[i]

# ask the user for random capitals until they answer incorrectly

score = 0

while True:
	randInd = random.randint(0, len(states) - 1)
	state = states[randInd]
	
	guess = input("What is the capital of " + state + "? ")
	
	if guess == d[state]:
		print("Correct!")
		score += 1
	
	else:
		print("Incorrect! Game over :(")
		break

print("Your total score was: " + str(score))
