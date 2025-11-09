"""
You're given an encrypted string for a secret password: tavaenryvahwribyv. You know that in order to get to this encrypted version of the password, the original password was run through a Caesar cipher and then reversed. Without knowing the key for the Caesar cipher, write a program to undo this encryption by printing out all 26 possibilities of the original password, and then take a guess at which of the possibilities is most likely to have been somebody's password.
"""

password = "tavaenryvahwribyv"

# reverse the string
reversedStr = ""
for i in range(len(password) - 1, -1, -1):
	reversedStr += password[i]

# run through all possible keys from a to z and print out what the original password could have been

for key in range(ord('a'), ord('z') + 1):
	guess = ""
	for i in range(0, len(reversedStr)):
		num = ord(reversedStr[i]) - key
		while num < ord('a'):
			num += 26
		guess += chr(num)
	print(guess)
