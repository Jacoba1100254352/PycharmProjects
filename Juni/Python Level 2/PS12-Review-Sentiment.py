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
