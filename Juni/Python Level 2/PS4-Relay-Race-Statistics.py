print("Let's see how your team did in the 4x400 relay!")

player1 = float(input("Runner 1, enter your time in seconds: "))
player2 = float(input("Runner 2, enter your time in seconds: "))
player3 = float(input("Runner 3, enter your time in seconds: "))
player4 = float(input("Runner 4, enter your time in seconds: "))

totalTime = player1 + player2 + player3 + player4

if player1 < player2 and player1 < player3 and player1 < player4:
    print("Runner 1 had the fastest time!")
elif player2 < player1 and player2 < player3 and player2 < player4:
    print("Runner 2 had the fastest time!")
elif player3 < player1 and player3 < player2 and player3 < player4:
    print("Runner 3 had the fastest time!")
elif player4 < player1 and player4 < player2 and player4 < player3:
    print("Runner 4 had the fastest time!")
else:
    print("There was a tie for the fastest runner!")

averageTime = totalTime / 4
print("The average time of each lap " + str(averageTime) + " seconds")

if player1 < averageTime:
    print("Runner 1 was faster than average")
elif player1 == averageTime:
    print("Player 1 ran the average pace")
else:
    print("Player 1 was slower than average")

if player2 < averageTime:
    print("Player 2 was faster than average")
elif player2 == averageTime:
    print("Player 2 ran the average pace")
else:
    print("Player 2 was slower than average")

if player3 < averageTime:
    print("Player 3 was faster than average")
elif player3 == averageTime:
    print("Player 3 ran the average pace")
else:
    print("Player 3 was slower than average")

if player4 < averageTime:
    print("Player 4 was faster than average")
elif player4 == averageTime:
    print("Player 4 ran the average pace")
else:
    print("Player 4 was slower than average")
