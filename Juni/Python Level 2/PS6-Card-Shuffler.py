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
