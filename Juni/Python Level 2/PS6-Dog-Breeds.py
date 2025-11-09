"""
Create a list of all the dog breeds you can think of! Then, loop through the list, and for each breed, print out "A _____ is a dog breed. Its name starts with the letter __, and its name has __ letters in it."
"""

dogs = ["beagle", "collie", "greyhound", "komondor", "mastiff", "pug", "terrier"]

for dog in dogs:
	firstLetter = dog[0]
	numLetters = str(len(dog))
	print(
		"A " + dog + " is a dog breed. Its name starts with the letter " + firstLetter + ", and its name has " + numLetters + " letters in it.\n")
