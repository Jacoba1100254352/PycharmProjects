"""
Ask the user to type in a number of days. The program should print out the number of years, months, weeks, and days this is equal to.
"""

days = int(input(
	"Enter in a number of days, and I will tell you how many years, months (assuming 30 days), weeks, and days this is: "))

years = 0
months = 0
weeks = 0

while days >= 365:
	days -= 365
	years += 1

while days >= 30:
	days -= 30
	months += 1

while days >= 7:
	days -= 7
	weeks += 1

print("This is " + str(years) + " years, " + str(months) + " months, " + str(weeks) + " weeks, and " + str(
	days) + " days.")
