import random

money = 10

while True:
    playAgain = input("You currently have $" + str(
        money) + ". Type q to walk away and keep the money you have, or press Enter to continue: ")

    if playAgain == 'q':
        break
    else:
        # pick a random number: 0 = heads, 1 = tails
        coin = random.randint(0, 1)

        if coin == 0:
            money *= 2
            print("Nice! The coin was heads. You now have: $" + str(money))
        elif coin == 1:
            money = 0
            print("Oh no! The coin was tails. You lost everything.")
            break

print("You ended Double or Nothing with: $" + str(money))
