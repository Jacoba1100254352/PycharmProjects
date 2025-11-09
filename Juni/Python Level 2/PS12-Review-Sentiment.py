"""
Ask the user to enter in a review (of a book, product, movie, etc). Calculate the percentage of positive words and the percentage of negative words in the review. Based on this, decide whether the review is overall positive or negative!

Note: To split up a string review into its words, use review.split(), which will create a list of the words in the string.
"""

posWords = ["good", "great", "excellent", "awesome", "beautiful", "amazing", "glad", "joy", "happy", "positive", "cool"]

negWords = ["bad", "mediocre", "poor", "lousy", "sad", "unacceptable", "awful", "negative", "inferior", "lame",
            "disappointing"]

review = input("Enter your review here: ")

words = review.split()
numPosWords = 0
numNegWords = 0

for word in words:
	if word in posWords:
		numPosWords += 1
	elif word in negWords:
		numNegWords += 1

numWordsTotal = len(words)
percPos = (numPosWords / numWordsTotal) * 100
percNeg = (numNegWords / numWordsTotal) * 100

print("The review has " + str(percPos) + " percent positive words and " + str(percNeg) + " percent negative words.")

if percPos > percNeg:
	print("I've detected that this review is mostly positive!")
elif percNeg > percPos:
	print("I've detected that this review is mostly negative!")
else:
	print("This review seems to be neutral!")
