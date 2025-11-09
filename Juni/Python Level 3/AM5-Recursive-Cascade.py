"""
Write a recursive function that takes in a string, and then creates a “staircase” out of the input. This means that the function should print the first character of the input on one line, the first two characters on the next line, and the first three on the next, and so on until finally the whole word is printed out. Once you have done that, make a recursive function that does the opposite (prints an upside-down staircase).
"""


# Make a cascade function: cascade takes in a string, s, and prints out first the first char, then the first 2, then the first 3 … until all of s is printed
def cascade(s):
	if len(s) > 1:
		cascade(s[:-1])
	print(s)


word = "lemmings"
cascade(word)


# Now, make the inverse cascade: first “dog”, then “do”, then “d”
def inverse_cascade(s):
	print(s)
	if len(s) > 1:
		inverse_cascade(s[:-1])


inverse_cascade(word)
