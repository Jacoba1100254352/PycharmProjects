from random import shuffle

deck = sum([[i]*4 for i in range(1, 14)], [])
shuffle(deck)
print(deck)
