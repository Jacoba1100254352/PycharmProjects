"""
Evil Wheel of Fortune is just like regular Wheel of Fortune, but with a twist: the computer cheats to make the game as hard as possible! Instead of picking a single secret word, the computer maintains a list of every word in the English dictionary. Then it removes words to dodge the user’s guesses for as long as possible! When the player guesses a letter, it divides the list into different “word families” based on the positions of the guessed letters. Then it picks the largest word family and uses that as the remaining list.

For example, if the word list contained PEACH, GRAPE, GUAVA, and LEMON, and the player guesses the letter A, then there would be three word families:
--A--, containing PEACH and GRAPE
--A-A, containing GUAVA
-----, containing LEMON
The computer would then choose the --A-- word family since it is the largest, and display --A-- on the screen.
Hint: Use a dictionary to store different word families.
"""

with open("dictionary.txt") as f:
	words = set(f.read().strip().split("\n"))
