"""
You are given a dictionary of some of the players on the soccer team FC Barcelona and their nationalities. Use the information in the dictionary to print out the number of different countries the players on the team come from. Then, print out these countries.
"""

players = {"Suarez": "Uruguay", "Messi": "Argentina", "Coutinho": "Brazil", "Vidal": "Chile", "Rakitic": "Croatia", "Busquets": "Spain",
           "Roberto": "Spain", "Pique": "Spain", "Lenglet": "France", "Alba": "Spain", "Ter Stegen": "Germany"}

playersSet = set()
for player in players:
	playersSet.add(players[player])

print("FC Barcelona has players from " + str(len(playersSet)) + " different countries.")

print("FC Barcelona's players come from:")
for nation in playersSet:
	print(nation)
