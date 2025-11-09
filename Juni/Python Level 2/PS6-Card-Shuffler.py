"""
Write a function shuffle(numShuffles) which first generates an ordered list of 52 playing cards, as such: [1,1,1,1,2,2,2,2,...,13,13,13,13]. Then, randomly choose two positions within the deck and swap the two cards at these two position. Do this numShuffles number of times, and then print out the resulting shuffled deck. Call this function with 10, 50, 100, and 500 shuffles and notice at what point the deck seems randomly shuffled!
"""

import random
import time


def createDeck():
	deck = []
	for i in range(1, 14):
		for j in range(4):
			deck.append(i)
	return deck


def shuffle(numShuffles):
	deck = createDeck()
	
	for i in range(numShuffles):
		index1 = random.randint(0, len(deck) - 1)
		index2 = random.randint(0, len(deck) - 1)
		
		temp = deck[index1]
		deck[index1] = deck[index2]
		deck[index2] = temp
	
	print("\nShuffled deck after " + str(numShuffles) + " swaps: ")
	print(deck)


print("Sorted deck: ")
print(createDeck())
time.sleep(2)

shuffle(10)
time.sleep(3)

shuffle(50)
time.sleep(3)

shuffle(100)
time.sleep(3)

shuffle(500)
