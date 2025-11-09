"""
Program this Type Racer game, as shown in the graphic below! Write out pseudocode in your code comments to plan out the program flow and data structures you'll need to set up.
"""

import random
import time


sentences = ["Peter Piper picked a peck of pickled peppers", "She sells seashells by the sea shore",
             "How much wood could a woodchuck chuck if a woodchuck could chuck wood?",
             "If a dog chews shoes, whose shoes does he choose?",
             "If you notice this notice, you will notice that this notice is not worth noticing",
             "I saw Susie sitting in a shoe shine shop"]

input("Welcome to Type Racer. Press Enter to play.")
print("Ready....")
time.sleep(1)
print("Set....")
time.sleep(1)
print("Type!")

sentence = sentences[random.randint(0, 5)]
print(sentence)
startTime = time.time()
typedInput = input("Type: ")
while typedInput != sentence:
	print("The sentences do not match! Please try again.")
	typedInput = input("Type: ")
endTime = time.time()

print("You finished typing in " + str(endTime - startTime) + " seconds!")
