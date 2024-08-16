# Start the game with all of the players free (i.e. no one has been captured yet)
team1free = set()
team1free.add("Jared")
team1free.add("Rachel")
team1free.add("Khalif")
team1free.add("Claudia")
team2free = set()
team2free.add("Zeinab")
team2free.add("Michael")
team2free.add("Matthew")
team2free.add("Valerie")

team1captured = set()
team2captured = set()

# Keep playing until either someone steals the flag or an entire team gets captured
while True:
	capturedFlag = input("Did someone capture the flag? (Y/N): ")
	if capturedFlag.lower() == "y":
		print("Game over, someone captured the flag!")
		break
	else:
		captured = input("Did someone get captured? (Y/N): ")
		if captured.lower() == "y":
			name = input("Who got captured? ")
			# Check which team the player was on
			if name in team1free:
				# Move captured player from free to captured set
				team1free.remove(name)
				team1captured.add(name)
			elif name in team2free:
				# Move captured player from free to captured set
				team2free.remove(name)
				team2captured.add(name)
			else:
				print("I don't see that player out on the field!")
		
		# Print everyone who is free on each team
		print("Here are the players who are still on the field for team 1:")
		for name in team1free:
			print(name)
		print("Here are the players who are still on the field for team 2:")
		for name in team2free:
			print(name)
			
			# Print everyone who is in jail
		print("Here are the players who are in jail:")
		totalCaptured = team1captured.union(team2captured)
		for name in totalCaptured:
			print(name)
		
		# Check if an entire team has been captured
		if len(team1free) == 0:
			print("All of team 1 is in jail, so team 2 wins!")
			break
		elif len(team2free) == 0:
			print("All of team 2 is in jail, so team 1 wins!")
			break
