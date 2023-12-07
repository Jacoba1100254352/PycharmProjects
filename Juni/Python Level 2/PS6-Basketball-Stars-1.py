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
