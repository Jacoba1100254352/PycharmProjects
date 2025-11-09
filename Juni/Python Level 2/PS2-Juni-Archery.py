"""
Welcome to Juni’s premier archery competition! You will be competing to see how many bullseyes you can hit, across 5 rounds of bowmanship. In each of these 5 rounds, you will fire 3 arrows. With every shot, you have a 1 in 3 chance to hit the bullseye; use the “random” module to determine whether or not you hit the bullseye.

For each shot, print out the round number and the shot within that round, followed by an “X” if you made the shot or an “O” if you missed. For example, if you missed your first two shots, the program should print out:
Round 1, arrow 1: O
Round 1, arrow 2: O

Lastly, count the total number of bullseyes you hit and display this number at the end.
"""

import random


print("Welcome to Juni Archery, prepare your bow!")

numHits = 0
for i in range(1, 6):
	for j in range(1, 4):
		if random.randint(1, 3) == 1:
			print("Round", str(i) + ", arrow", str(j) + ": X")
			numHits += 1
		else:
			print("Round", str(i) + ", arrow", str(j) + ": O")

print("You hit the bullseye " + str(numHits) + " times!")
