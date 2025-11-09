"""
Simulation of the classic card game "War".

Runs 1,000 simulated games between two players and tallies the wins.
"""

import random


# Constants for player identifiers
Player1, Player2 = "Player1", "Player2"

# Win counters across all simulations
wins = {Player1: 0, Player2: 0}


def isTooSmall(decks, finalSetIndex):
	"""
	Check if either player does not have enough cards to resolve the current war.

	If a player runs out of cards, transfer whatever remains to the opponent and
	return True to indicate the game is over.

	:param decks: Dict mapping player name to their list of cards (top of deck is index 0)
	:param finalSetIndex: Index of the final face-up card that will decide the war
	:return: True if a player’s deck is too small to continue, else False
	"""
	for player in [Player1, Player2]:
		otherPlayer = Player2 if player == Player1 else Player1
		
		# If the active player cannot reach the required card, they lose
		if len(decks[player]) <= finalSetIndex:
			# Opponent scoops up the remainder of the loser's deck
			decks[otherPlayer].extend(decks[player])
			decks[player] = []
			return True
	
	return False


def war(decks):
	"""
	Resolve a war (tie) until one player’s face-up card outranks the other.

	The procedure follows the common “3 cards face-down, 1 card face-up” rule.
	Each recursive war adds another 4 cards (3 down + 1 up) to the pile.

	:param decks: Dict mapping player name to their list of cards (mutated in place)
	:return: Updated decks dict after the war is resolved
	"""
	finalSetIndex = 3  # First war requires 3 face-down cards + 1 face-up (index 3)
	
	# Continue chaining wars while the deciding cards tie and both decks are large enough
	while (
			not isTooSmall(decks, finalSetIndex)
			and decks[Player1][finalSetIndex] == decks[Player2][finalSetIndex]
	):
		finalSetIndex += 4  # Add another “war set” to the pile
	
	# Stop if someone ran out of cards mid-war
	if isTooSmall(decks, finalSetIndex):
		return decks
	
	# Determine who has the higher face-up card
	wonRound, lostRound = sorted(
		[Player1, Player2],
		key=lambda player: decks[player][finalSetIndex],
		reverse=True,
	)
	
	# Sanity check: at this point the cards must differ
	if decks[wonRound][finalSetIndex] == decks[lostRound][finalSetIndex]:
		print("Unreachable state: war ended in a tie!")
		exit(1)
	
	# Winner collects *all* cards that were part of the war, starting from deck top
	decks[wonRound].extend(
		decks[wonRound][: finalSetIndex + 1] + decks[lostRound][: finalSetIndex + 1]
	)
	# Remove the collected cards from each player’s deck
	decks[wonRound] = decks[wonRound][finalSetIndex + 1:]
	decks[lostRound] = decks[lostRound][finalSetIndex + 1:]
	
	return decks


# ----- Main simulation loop -----
for _ in range(1000):
	# Build a standard 52-card deck: 4 suits × cards 1-13
	dealingDeck = [card for _ in range(4) for card in range(1, 14)]
	random.shuffle(dealingDeck)  # Shuffle in place
	
	# Deal alternating cards to each player (index 0 is the top of the deck)
	playerDecks = {Player1: dealingDeck[::2], Player2: dealingDeck[1::2]}
	
	# Play until one deck is empty
	while playerDecks[Player1] and playerDecks[Player2]:
		# Each player plays their top card
		card1 = playerDecks[Player1].pop(0)
		card2 = playerDecks[Player2].pop(0)
		
		# Determine outcome of the round
		winner, loser = sorted([(card1, Player1), (card2, Player2)], reverse=True)
		
		if winner[0] != loser[0]:
			# Simple win: higher card takes both
			playerDecks[winner[1]].extend([winner[0], loser[0]])
		else:
			# Tie leads to war
			playerDecks = war(playerDecks)
	
	# Record which player still has cards (the winner)
	if playerDecks[Player1] and playerDecks[Player2]:
		print("Error: both players still have cards, game should be over")
	else:
		winner = Player1 if playerDecks[Player1] else Player2
		wins[winner] += 1

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
