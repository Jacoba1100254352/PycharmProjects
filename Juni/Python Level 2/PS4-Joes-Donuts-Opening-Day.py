print("Welcome to Opening Day at Joe's Donuts! We're so glad you're here, and we have some special surprises for you!")

customerNumber = int(input("Which number customer were you? "))
print()

if customerNumber == 1:
    print("As the first customer, you win free donuts for a year!")
if customerNumber <= 12:
    print("You receive a dozen free donuts!")
elif customerNumber <= 200:
    if customerNumber == 144:
        print("Congratulations, 144 is Joe's favorite number, so you win free donuts for a month!")
    else:
        print("You may purchase your first dozen donuts for $1!")
elif customerNumber <= 500:
    print("You'll receive 50% off your purchase!")
else:
    print("You can take advantage of our special offer today: buy two donuts, get the third free!")

print()
print(
    "And just so you can tell all of your friends, Joe's Donuts also has a special deal that will last all year: buy a dozen donuts, get the 13th free!")
