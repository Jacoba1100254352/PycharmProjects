"""
Ask the user for a secret message. Then, print out the message translated into ASCII, with a space between each character.

Now, we will make the cipher more difficult. This time, ask for another secret message, but print out the message translated into ASCII, with a constant number (a key) added to each number. This is the secret key the recipient would use to decode your message.
"""

# Part 1: Ask the user for a secret message. Then, print out the message translated into ASCII, with a space between each character.
msg = input("Type in your message to encrypt: ")
newMsg = ''

for i in range(0, len(msg)):
	num = ord(msg[i])
	newMsg += str(num) + ' '

print(newMsg)

# Part 2: Now, we will make the cipher more difficult. This time, ask for another secret message, but print out the message translated into ASCII, with a constant number (a key) added to each number. This is the secret key the recipient would use to decode your message.

msg = input("Type in your message to encrypt: ")
key = int(input("Type in the key you wish to use: "))
newMsg = ''
for i in range(0, len(msg)):
	num = ord(msg[i])
	newMsg += str(num + key) + ' '

print(newMsg)
