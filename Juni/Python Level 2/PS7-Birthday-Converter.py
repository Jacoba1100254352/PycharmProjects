"""
Ask the user to enter their birthday in the form mm/dd/yyyy. Your program should print out their full birthday - for example, 01/01/1995 would convert to January 1st, 1995. The starter code provides two dictionaries: monthToString, which maps month numbers to their name, and daySuffix, which maps the last digit of day numbers to their corresponding suffix (i.e. "th," "st," or "nd"). However, note that there are exceptions for the 11th, 12th, and 13th of the month that you will need to account for!
"""

monthToString = {
	1: "January",
	2: "February",
	3: "March",
	4: "April",
	5: "May",
	6: "June",
	7: "July",
	8: "August",
	9: "September",
	10: "October",
	11: "November",
	12: "December"
}

daySuffix = {
	0: "th",
	1: "st",
	2: "nd",
	3: "rd",
	4: "th",
	5: "th",
	6: "th",
	7: "th",
	8: "th",
	9: "th"
}

date = input("Enter your birthday in the form \"mm/dd/yyyy\": ")

month = 10 * int(date[0]) + int(date[1])
day = 10 * int(date[3]) + int(date[4])
year = 1000 * int(date[6]) + 100 * int(date[7]) + 10 * int(date[8]) + int(date[9])

monthString = monthToString[month]
dayString = str(day) + daySuffix[day % 10]

# special cases for 11th, 12th, 13th
if day == 11 or day == 12 or day == 13:
	dayString = str(day) + "th"

print("You were born on " + monthString + " " + dayString + ", " + str(year))
