"""
Program this Wordsmith game, as shown in the graphic below! Write out pseudocode in your code comments to plan out the program flow and data structures you'll need to set up. (Note: For this project, starter code should be automatically loaded in your portal. The starter code provided reads in a list of about 37,000 valid English words into the validWords list.)
"""

# reads words into list
f = open("valid_words.txt")
validWords = f.readlines()
validWords = [x.strip() for x in validWords]
f.close()
