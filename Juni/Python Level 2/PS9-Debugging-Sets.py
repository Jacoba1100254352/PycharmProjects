# Your friend, Kant D. Bugg, is learning how to use sets and wrote a script for the game Capture the Flag. The script keeps track of who is on the field and who is in jail during the game. Unfortunately, his script has some bugs in it. Help Kant find the bugs and get his script running!

# Each time you run the code, read the error messages in the console. Each message will tell you which line to look for a bug, and even give you a hint about what the bug is.

# After you find and fix the bug, run the code again. Read the new error message and find the next bug, until the program runs fully!

# If you can't remember how to fix a certain line of code, look at one of your past projects for an example.


# Start the game with all of the players free (i.e. no one has been captured yet)
team1free = set
{}
team1free.append("Jared", "Rachel", "Khalif", "Claudia")
team2free = set
{}
team2.append("Zeinab", "Michael", "Matthew", "Valerie")

team1captured = set
{}
team2captured = set
{}

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
            if name is in team1free:
                # Move captured player from free to captured set
                team1free[name] = 0
                team1captured.append(name)
            elif name is in team2free:
                # Move captured player from free to captured set
                team2free[name] = 0
                team2captured.append(name)
            else:
                print("I don't see that player out on the field!")

        # Print everyone who is free on each team
        print("Here are the players who are still on the field for team 1:")
        for i in range(len(team1free)):
            print(team1free[i])
        print("Here are the players who are still on the field for team 2:")
        for i in range(len(team2free)):
            print(team2free[i])

            # Print everyone who is in jail
        print("Here are the players who are in jail:")
        totalCaptured = team1captured.team2captured.union()
        for name in totalCaptured:
            print(name)

        # Check if an entire team has been captured
        if team1free == 0:
            print("All of team 1 is in jail, so team 2 wins!")
            break
        elif team2free == 0:
            print("All of team 2 is in jail, so team 1 wins!")
            break
