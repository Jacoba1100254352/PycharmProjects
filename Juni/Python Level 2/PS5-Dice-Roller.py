import random


def diceRoll():
	return random.randint(1, 6)


numRolls = 1000
numTwos = 0
numThrees = 0
numFours = 0
numFives = 0
numSixes = 0
numSevens = 0
numEights = 0
numNines = 0
numTens = 0
numElevens = 0
numTwelves = 0

for i in range(0, numRolls):
	rollNum = diceRoll() + diceRoll()
	if rollNum == 2:
		numTwos += 1
	elif rollNum == 3:
		numThrees += 1
	elif rollNum == 4:
		numFours += 1
	elif rollNum == 5:
		numFives += 1
	elif rollNum == 6:
		numSixes += 1
	elif rollNum == 7:
		numSevens += 1
	elif rollNum == 8:
		numEights += 1
	elif rollNum == 9:
		numNines += 1
	elif rollNum == 10:
		numTens += 1
	elif rollNum == 11:
		numElevens += 1
	elif rollNum == 12:
		numTwelves += 1

print(str((numTwos / numRolls) * 100) + "% of your rolls were 2.")
print(str((numThrees / numRolls) * 100) + "% of your rolls were 3.")
print(str((numFours / numRolls) * 100) + "% of your rolls were 4.")
print(str((numFives / numRolls) * 100) + "% of your rolls were 5.")
print(str((numSixes / numRolls) * 100) + "% of your rolls were 6.")
print(str((numSevens / numRolls) * 100) + "% of your rolls were 7.")
print(str((numEights / numRolls) * 100) + "% of your rolls were 8.")
print(str((numNines / numRolls) * 100) + "% of your rolls were 9.")
print(str((numTens / numRolls) * 100) + "% of your rolls were 10.")
print(str((numElevens / numRolls) * 100) + "% of your rolls were 11.")
print(str((numTwelves / numRolls) * 100) + "% of your rolls were 12.")
