interestRate = 0.01

balance = float(input("How much money do you currently have in your account? "))

print("Your starting balance is: " + str(balance))

for i in range(20):
	balance *= (1 + interestRate)
	print("Your balance after " + str(1 + i) + " years is $" + "%.2f" % balance)
