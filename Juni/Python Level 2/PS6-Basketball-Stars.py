"""
A common benchmark for a standout performance in a basketball game is a "triple double." In this program, we define a triple double as when a player achieves at least 10 points, rebounds, and assists in a single game. (In reality, this statistic also includes steals and blocks.) Write a program that stores the number of points, rebounds, and assists five players accumulated in a game, and print out which players achieved a triple double.

Hint: Lists can contain more lists! In this program, you should have one list that holds five sublists. Each sublist should be initialized with three zeros (essentially open slots), to represent each stat. The slots will be filled in as the user inputs the game-related data.
"""

players = []
numPlayers = 5

# Add one list for each player into players
for i in range(numPlayers):
	players.append([])

# For each player's list, fill it with three 0s: points, rebounds, and assists
for player in players:
	for i in range(3):
		player.append(0)

print("The starting data: ")
print(players)
print()

# Ask the user to fill in the data
for i in range(numPlayers):
	players[i][0] = int(input("Enter player " + str(1 + i) + "'s points: "))
	players[i][1] = int(input("Enter player " + str(1 + i) + "'s rebounds: "))
	players[i][2] = int(input("Enter player " + str(1 + i) + "'s assists: "))
	
	print("Updated list: ")
	print(players)
	print()

print("The final data: ")
print(players)

# Check who had a triple double (i.e. double digits for all three stats)
for i in range(numPlayers):
	if players[i][0] >= 10 and players[i][1] >= 10 and players[i][2] >= 10:
		print("Player " + str(i + 1) + " had a triple double!")
