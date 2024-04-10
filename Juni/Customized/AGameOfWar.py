import random


Player1, Player2 = "Player1", "Player2"
wins = {Player1: 0, Player2: 0}


def isTooSmall(decks, finalSetIndex):
	for player in [Player1, Player2]:
		otherPlayer = Player2 if player == Player1 else Player1
		if len(decks[player]) <= finalSetIndex:
			decks[otherPlayer].extend(decks[player])
			decks[player] = []
			return True
	return False


def war(decks):
	finalSetIndex = 3
	while not isTooSmall(decks, finalSetIndex) and decks[Player1][finalSetIndex] == decks[Player2][finalSetIndex]:
		finalSetIndex += 4
	
	if isTooSmall(decks, finalSetIndex):  # add a condition to exit the function if the deck size is too small
		return decks
	
	wonRound, lostRound = sorted([Player1, Player2], key=lambda player: decks[player][finalSetIndex], reverse=True)
	
	if decks[wonRound][finalSetIndex] == decks[lostRound][finalSetIndex]:
		print("This should not have been reached")
		exit(1)
	
	decks[wonRound].extend(decks[wonRound][:finalSetIndex + 1] + decks[lostRound][:finalSetIndex + 1])
	decks[wonRound] = decks[wonRound][finalSetIndex + 1:]
	decks[lostRound] = decks[lostRound][finalSetIndex + 1:]
	
	return decks


for _ in range(1000):
	dealingDeck = [j for _ in range(4) for j in range(1, 14)]
	random.shuffle(dealingDeck)
	
	playerDecks = {Player1: dealingDeck[::2], Player2: dealingDeck[1::2]}
	
	while playerDecks[Player1] and playerDecks[Player2]:
		card1, card2 = playerDecks[Player1].pop(0), playerDecks[Player2].pop(0)
		winner, loser = sorted([(card1, Player1), (card2, Player2)], reverse=True)
		
		if winner[0] != loser[0]:
			playerDecks[winner[1]].extend([winner[0], loser[0]])
		else:
			playerDecks = war(playerDecks)
	
	if len(playerDecks[Player1]) > 0 and len(playerDecks[Player2]) > 0:
		print("Something fishy has occurred")
	else:
		winner = Player1 if len(playerDecks[Player1]) > 0 else Player2
		wins[winner] += 1
		# print(f"{winner} won!")

print(wins)

"""
# Previous code
import random

FULL_DECK = 52

def isTooSmall(decks, finalSetIndex):
    if len(decks[Player1]) < finalSetIndex + 1:
        decks[Player2].extend(decks[Player1])
        decks[Player1].clear()
    elif len(decks[Player2]) < finalSetIndex + 1:
        decks[Player1].extend(decks[Player2])
        decks[Player2].clear()
    else:
        return False
    return True


def war(decks):
    global wonRound, lostRound

    # Find the last iteration of the war
    finalSetIndex = 3
    while True:
        if isTooSmall(decks, finalSetIndex):
            return decks
        elif decks[Player1][finalSetIndex] == decks[Player2][finalSetIndex]:
            finalSetIndex += 4
            if isTooSmall(decks, finalSetIndex):
                return decks
        else:
            break

    # Determine winner of the "war"
    if decks[Player1][finalSetIndex] > decks[Player2][finalSetIndex]:
        wonRound = Player1
        lostRound = Player2
    elif decks[Player1][finalSetIndex] < decks[Player2][finalSetIndex]:
        wonRound = Player2
        lostRound = Player1
    else:
        print("This should not have been reached")
        exit(1)

    # Adjust the decks accordingly
    decks[wonRound].extend(
        decks[wonRound][:finalSetIndex] + decks[lostRound][:finalSetIndex])  # is it faster to extend them separately?
    del decks[wonRound][:finalSetIndex], decks[lostRound][:finalSetIndex]

    return decks


Player1 = "Player1"
Player2 = "Player2"
wonRound = "wonRound: Undefined"
lostRound = "lostRound: Undefined"
wins = {Player1: 0, Player2: 0}

for _ in range(1000):
    #   Fill player's decks   #
    # Prepare deck
    dealingDeck = []
    for _ in range(4):
        for j in range(1, 14):
            dealingDeck.append(j)

    # Deal to players
    playerDecks = {Player1: [], Player2: []}
    random.shuffle(dealingDeck)
    for i in range(len(dealingDeck.copy())):
        if i % 2:
            playerDecks[Player1].append(dealingDeck.pop())
        else:
            playerDecks[Player2].append(dealingDeck.pop())

    # Play game
    while playerDecks[Player1] and playerDecks[Player2]:
        card1 = playerDecks[Player1].pop(0)
        card2 = playerDecks[Player2].pop(0)
        if card1 > card2:
            playerDecks[Player2].extend([card2, card1])  # Also, is it faster to do this or append them separately?
        elif card1 < card2:
            playerDecks[Player1].extend([card1, card2])
        else:
            playerDecks = war(playerDecks)

    # Determine Winner
    if len(playerDecks[Player1]) != FULL_DECK and len(playerDecks[Player2]) != FULL_DECK:
        print("Something fishy has occurred")
    elif playerDecks[Player1]:
        wins[Player1] += 1
        # print("Player 1 won!")
    else:
        wins[Player2] += 1
        # print("Player 2 won!")

print(wins)
"""
