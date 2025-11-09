"""
Write a function flipCoin() that returns either "heads" or "tails" randomly to represent heads or tails. Using the function, flip the coin 1000 times and tally up the number of heads and the number of tails. Finally, let's print out the percentage of heads and the percentage of tails we got.
"""

import random


def flipCoin():
	if random.randint(0, 1) == 0:
		return "heads"
	else:
		return "tails"


numFlips = 1000
numHeads = 0
numTails = 0

for i in range(0, numFlips):
	headsOrTails = flipCoin()
	if headsOrTails == "heads":
		numHeads += 1
	else:
		numTails += 1
print(str((numHeads / numFlips) * 100) + "% of your flips were heads.")
print(str((numTails / numFlips) * 100) + "% of your flips were tails.")
