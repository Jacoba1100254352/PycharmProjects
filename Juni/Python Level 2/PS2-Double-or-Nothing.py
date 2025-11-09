"""
Program the game Double or Nothing! The user should start with $10 and be given the option to walk away or play double or nothing with all of their money. If they play, then simulate a coin flip, where heads doubles their money and tails means they lose it all. Keep playing until the player either walks away or loses!

Note: To have the computer simulate a coin flip, have it pick a random number, either 0 or 1. To do this, import the random module at the beginning of your program, and then randNum = random.randint(0,1) will save a random number, either 0 or 1, in randNum.
"""

import random


money = 10

while True:
	playAgain = input("You currently have $" + str(
		money) + ". Type q to walk away and keep the money you have, or press Enter to continue: ")
	
	if playAgain == 'q':
		break
	else:
		# pick a random number: 0 = heads, 1 = tails
		coin = random.randint(0, 1)
		
		if coin == 0:
			money *= 2
			print("Nice! The coin was heads. You now have: $" + str(money))
		elif coin == 1:
			money = 0
			print("Oh no! The coin was tails. You lost everything.")
			break

print("You ended Double or Nothing with: $" + str(money))
