"""
To show the power of compounding interest, write a program that asks the user for the balance in their bank account, and then print out their starting balance, in addition to what their balance will be after 1 year, 2 years, up to 20 years. The program should store the interest rate in a variable - start with the interest rate set to 1%, and experiment with changing it to see how it affects the balance over time.

Note: To print out a float (decimal) rounded to two decimal points, use str("%.2f" % num), where num is the variable that stores the float.
"""

interestRate = 0.01

balance = float(input("How much money do you currently have in your account? "))

print("Your starting balance is: " + str(balance))

for i in range(20):
	balance *= (1 + interestRate)
	print("Your balance after " + str(1 + i) + " years is $" + "%.2f" % balance)
