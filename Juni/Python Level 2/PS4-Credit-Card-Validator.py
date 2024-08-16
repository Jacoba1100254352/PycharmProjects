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
