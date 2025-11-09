"""
A team just ran a 4x400 relay race, in which each of 4 runners ran one 400m lap around the track, and they recorded their individual times. They want to know their total time as a team, as well as their average time for one lap. Write a program that prompts each member of the team for their time (in seconds), and then prints out both the total time and the average time for each lap.

Note: To convert a string into a decimal value, use the function float().
"""

print("Let's see how your team did in the 4x400 relay!")

player1 = float(input("Runner 1, enter your time in seconds: "))
player2 = float(input("Runner 2, enter your time in seconds: "))
player3 = float(input("Runner 3, enter your time in seconds: "))
player4 = float(input("Runner 4, enter your time in seconds: "))

totalTime = player1 + player2 + player3 + player4
print("Your team's time was " + str(totalTime) + " seconds")
print("The average time of each lap was " + str(totalTime / 4) + " seconds")
