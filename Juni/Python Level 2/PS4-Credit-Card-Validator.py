"""
Every time a credit card is used, an algorithm is used to make sure that the credit card number is valid. A simplified version of this algorithm is as follows: add up all of the digits of the card number, but add every other digit twice (for example, with the number 6386, we would get 6*2 + 3 + 8*2 + 6 = 37). If that sum is a multiple of 10, the credit card is valid! Write a program that asks the user for a credit card number, and then uses the described process to determine if the inputted number is valid or not.
"""

card = input("Enter a credit card number: ")

sumDigits = 0
for i in range(0, len(card)):
	sumDigits += int(card[i])
print("The sum of the digits is " + str(sumDigits))

sumDigits = 0
for i in range(0, len(card)):
	if i % 2 == 0:
		sumDigits += int(card[i]) * 2
	else:
		sumDigits += int(card[i])
print("The sum of the digits, with every other digit multipled by 2, is " + str(sumDigits))

if sumDigits % 10 == 0:
	print("Valid card!")
else:
	print("Invalid card!")
