import random
import time

player1 = input("Enter player 1's name: ")
player2 = input("Enter player 2's name: ")

numRounds = 10
score1 = 0
score2 = 0

for i in range(1, numRounds + 1):
    print("Round " + str(i) + ":")

    card1 = random.randint(2, 10)
    card2 = random.randint(2, 10)

    time.sleep(0.2)
    print(player1 + "'s card: " + str(card1))
    time.sleep(0.2)
    print(player2 + "'s card: " + str(card2))
    time.sleep(0.5)

    if card1 > card2:
        print(player1 + " wins this hand!\n")
        score1 += 1
    elif card2 > card1:
        print(player2 + " wins this hand!\n")
        score2 += 1
    else:
        print("This round is a tie!\n")

    time.sleep(1)

print("Final scores:")
print(player1 + ": " + str(score1))
print(player2 + ": " + str(score2))

if score1 > score2:
    print(player1 + " wins this game!")
elif score1 < score2:
    print(player2 + " wins this game!")
else:
    print("The game was a tie!")
