"""
This time, for field day, we have the names of 10 classmates stored in a list. We are going to randomly allocate 5 players into Team Red and 5 players into Team Blue. Write a program that randomly chooses one player from the remaining players to Team Red, and then one to Team Blue. Print out the roster for each time after each round of picking, and then print out the number of players remaining.
"""

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
