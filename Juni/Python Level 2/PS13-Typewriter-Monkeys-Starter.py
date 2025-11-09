"""
100 monkeys are wreaking havoc on your keyboard by mashing the keys randomly! Magically, they are only hitting the keys with letters on the keyboard. You become interested in measuring how long they will need to type for before they accidentally type out a valid three-letter word. Write a program that keeps track of the string they have typed out and continuously checks for whether the last three letters they've typed form a valid three-letter word. Print out this word once they do so!
"""

# reads words into list
f = open("valid_words.txt")
validWords = f.readlines()
validWords = [x.strip() for x in validWords]
f.close()
