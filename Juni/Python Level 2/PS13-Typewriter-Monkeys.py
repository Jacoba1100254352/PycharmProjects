"""
100 monkeys are wreaking havoc on your keyboard by mashing the keys randomly! Magically, they are only hitting the keys with letters on the keyboard. You become interested in measuring how long they will need to type for before they accidentally type out a valid three-letter word. Write a program that keeps track of the string they have typed out and continuously checks for whether the last three letters they've typed form a valid three-letter word. Print out this word once they do so!
"""

import random


# reads words into list
f = open("valid_words.txt")
validWords = f.readlines()
validWords = [x.strip() for x in validWords]
f.close()

monkeyStr = ""
print("Here's what the monkeys are typing on the typewriter:")
while True:
	# add a random character to the end of the monkeys' typing
	monkeyStr += chr(random.randint(ord('a'), ord('z')))
	print(monkeyStr)
	
	# check if last three letters are a valid word
	if len(monkeyStr) >= 3:
		
		# get the last three letters of what has been typed
		# Pythonic shortcut: lastThreeLetters = monkeyStr[len(monkeyStr)-3:len(monkeyStr)]
		lastThreeLetters = ""
		for i in range(len(monkeyStr) - 3, len(monkeyStr)):
			lastThreeLetters += monkeyStr[i]
		
		if lastThreeLetters in validWords:
			print("The monkeys did it! " + lastThreeLetters + " is a word!")
			break
