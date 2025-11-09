"""
It’s Opening Day at Joe’s Donuts, and Joe has some special deals for his first customers. Your program should ask the user which number customer they were and then notify them of which deals they're being offered. Here are the rules for today:
His first customer will receive free donuts for a year
His first 12 customers will receive a dozen free donuts today (the first customer gets both free donuts for a year and an immediate dozen, so they should be notified of both)
His first 200 customers can purchase their first dozen donuts for $1, but because customers #1-12 already received the first dozen for free, they should not be notified of this deal (it’s really for customers #13-200)
Customer #144 wins free donuts for a month (144 is Joe’s favorite number) and should not be notified of the dozen donuts for $1 either
Customers #201-500 can purchase their donuts for half price
Everyone else can take advantage of Joe’s last opening day offer: buy two donuts, get the third free - only show this notification to people who haven’t received any other offers
Every single customer should be notified of a year-round deal they can share with their friends: buy a dozen donuts, get the 13th free!
"""

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
