print("Let's see how your team did in the 4x400 relay!")

player1 = float(input("Runner 1, enter your time in seconds: "))
player2 = float(input("Runner 2, enter your time in seconds: "))
player3 = float(input("Runner 3, enter your time in seconds: "))
player4 = float(input("Runner 4, enter your time in seconds: "))

totalTime = player1 + player2 + player3 + player4
print("Your team's time was " + str(totalTime) + " seconds")
print("The average time of each lap was " + str(totalTime / 4) + " seconds")
