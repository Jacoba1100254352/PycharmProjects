import random


players = ['Alex', 'Barbara', 'Cole', 'Devyn', 'Eric', 'Fanny', 'George', 'Harsha', "Ignacio", "Julia"]

teamRed = []
teamBlue = []

while len(players) > 0:
	# choose player for Team Red
	randInd = random.randint(0, len(players) - 1)
	redPlayer = players[randInd]
	teamRed.append(redPlayer)
	players.remove(redPlayer)
	print("Team Red: " + str(teamRed))
	
	# choose player for Team Blue
	randInd = random.randint(0, len(players) - 1)
	bluePlayer = players[randInd]
	teamBlue.append(bluePlayer)
	players.remove(bluePlayer)
	print("Team Blue: " + str(teamBlue))
	
	print("Players left: " + str(players) + "\n")
