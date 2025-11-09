"""
Program the game of Blackjack, as shown in the graphic below! Write out pseudocode in your code comments to plan out the program flow and data structures you'll need to set up.
"""

import random
import time


input(
	"Welcome to the game of Blackjack! In this game, you will be dealt two cards to start. Your goal is to get as close to 21 as possible without going over - or busting! In this simple version of Blackjack, we only use the cards 2 through 11 (Ace).\n\nThe dealer will first ask you to hit (take another card) or stay. As long as you don't bust, once you decide to stay, the dealer will then play his hand. The dealer always has to hit until his hand is at least 17. Whoever has the better hand at the end wins!\n\nPress Enter to start playing.\n")

while True:
	playerHand = []
	
	# deal first two cards to player
	for _ in range(2):
		playerHand.append(random.randint(2, 11))
	
	# print out player's cards
	print("Here is your hand: ")
	print(playerHand)
	
	# use this variable to track when the game should end immediately
	continueGame = True
	
	# check for blackjack
	if sum(playerHand) == 21:
		print("Blackjack! You win! :D")
		continueGame = False
	
	if continueGame:
		# ask to Hit or Stay
		hitOrStay = "H"
		continueGame = True  # use this variable to track whether the game ends immediately after this
		while hitOrStay == "H":
			while True:
				hitOrStay = input("Type in H to hit or S to stay:")
				if hitOrStay == "H" or hitOrStay == "S":
					break
				else:
					print("Invalid input.\n")
			
			# if Hit, add new card and check if busted
			if hitOrStay == "H":
				playerHand.append(random.randint(2, 11))
				print("Here is your hand: ")
				print(playerHand)
				
				if sum(playerHand) > 21:
					print("You busted! :(\n")
					continueGame = False
					break
				elif sum(playerHand) == 21:
					print("Blackjack! You win! :D")
					continueGame = False
					break
		
		if continueGame:
			print("Dealer's turn!\n")
			
			# deal first two cards to dealer
			dealerHand = []
			for i in range(2):
				dealerHand.append(random.randint(2, 11))
			
			# print out dealer's cards
			print("Here is the dealer's hand: ")
			print(dealerHand)
			
			# the dealer continues to hit until his hand is at least 17
			while True:
				time.sleep(1)  # make game more realistic
				if sum(dealerHand) < 17:
					dealerHand.append(random.randint(2, 11))
					print("The dealer hit. Here is the dealer's new hand:")
					print(dealerHand)
				elif sum(dealerHand) == 21:
					print("The dealer got blackjack!")
					break
				elif sum(dealerHand) > 21:
					print("The dealer busted! You win! :)")
					break
				else:
					print("The dealer has finalized his hand.")
					# if the game is still going, see whose hand wins
					time.sleep(1)
					if sum(playerHand) > sum(dealerHand):
						print("You win! :)\n")
					elif sum(playerHand) < sum(dealerHand):
						print("The dealer won. :(\n")
					else:
						print("It's a tie!\n")
					break
	
	input("Press Enter to play again!\n")
