money = input("Tell me how much money you have (in cents), and I'll tell you how many quarters you can have. ")

money = int(money)
numQtrs = 0
while money - 25 >= 0:
	money -= 25
	numQtrs += 1

print("You can have " + str(numQtrs) + " quarters.\n\n")

money = input("Tell me how much money you have (in cents), and I'll tell you how many quarters and how many dimes you can have. ")

money = int(money)
numQtrs = 0
numDimes = 0
while money - 25 >= 0:
	money -= 25
	numQtrs += 1
while money - 10 >= 0:
	money -= 10
	numDimes += 1

print("You can have " + str(numQtrs) + " quarters and " + str(numDimes) + " dimes.\n\n")

money = input("Tell me how much money you have (in cents), and I'll tell you the amount of change you can have. ")

money = int(money)
numQtrs = 0
numDimes = 0
numNickels = 0
numPennies = 0
while money - 25 >= 0:
	money -= 25
	numQtrs += 1
while money - 10 >= 0:
	money -= 10
	numDimes += 1
while money - 5 >= 0:
	money -= 5
	numNickels += 1
while money - 1 >= 0:
	money -= 1
	numPennies += 1

print("You can have " + str(numQtrs) + " quarters, " + str(numDimes) + " dimes, " + str(numNickels) + " nickels, and " + str(numPennies) + " pennies.")
