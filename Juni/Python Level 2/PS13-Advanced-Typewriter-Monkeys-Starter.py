"""
The 100 monkeys are again wreaking havoc on your keyboard! This time, you would like to measure how long they will need to type before they accidentally type out a valid n-letter word. Write a function that takes in n and continuously prints out what they have typed so far and checks for whether the last n letters they've typed form a valid n-letter word. Try calling this function for different values of n and observe what happens as n increases.
"""

# reads words into list
f = open("valid_words.txt")
validWords = f.readlines()
validWords = [x.strip() for x in validWords]
f.close()
