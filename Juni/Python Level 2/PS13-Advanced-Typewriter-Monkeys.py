"""
The 100 monkeys are again wreaking havoc on your keyboard! This time, you would like to measure how long they will need to type before they accidentally type out a valid n-letter word. Write a function that takes in n and continuously prints out what they have typed so far and checks for whether the last n letters they've typed form a valid n-letter word. Try calling this function for different values of n and observe what happens as n increases.
"""

import random


# reads words into list
f = open("valid_words.txt")
validWords = f.readlines()
validWords = [x.strip() for x in validWords]
f.close()


def findValidWord(n):
	monkeyStr = ""
	print("Here's what the monkeys are typing on the typewriter:")
	while True:
		# add a random character to the end of the monkeys' typing
		monkeyStr += chr(random.randint(ord('a'), ord('z')))
		print(monkeyStr)
		
		# check if last n letters are a valid word
		if len(monkeyStr) >= n:
			
			# get the last n letters of what has been typed
			# Pythonic shortcut: lastThreeLetters = monkeyStr[len(monkeyStr)-n:len(monkeyStr)]
			lastNLetters = ""
			for i in range(len(monkeyStr) - n, len(monkeyStr)):
				lastNLetters += monkeyStr[i]
			
			if lastNLetters in validWords:
				print("The monkeys did it! " + lastNLetters + " is a word!")
				break


while True:
	length = int(input("How long should the word be? "))
	findValidWord(length)
