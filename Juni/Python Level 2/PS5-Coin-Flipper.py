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
