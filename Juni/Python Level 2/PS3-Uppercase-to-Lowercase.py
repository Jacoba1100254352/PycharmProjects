"""
Ask the user for a word in all uppercase. Convert this word to all lowercase, using the ord() and chr() functions. Do not use the lower() function!

Hint: You will need to calculate the numerical ASCII difference between a capital letter and its lowercase version.
"""

upper = input("Enter a word in all uppercase: ")
lower = ""

# calculate the numerical difference between the ASCII representation of A and a
difference = ord('A') - ord('a')

# iterate through the inputted string and apply this different to each character
for i in range(0, len(upper)):
	char = upper[i]
	lower += chr(ord(char) - difference)

print("The word in all lowercase is: " + lower)
