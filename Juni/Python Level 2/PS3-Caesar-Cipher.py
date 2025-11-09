"""
This time, our secret message will be encoded with letters. First, ask the user for a secret message and a key (a number). The program should print out the message with each letter shifted forward in the alphabet by the key amount. Keep in mind: what happens if the letter goes past the end of the alphabet? How can we make sure to start over at the beginning of the alphabet?

Now, ask the user for a message to decrypt and the correct decryption key. The program should print out the correct message with each letter shifted backward in the alphabet by the key amount. This time, what happens if the letter goes past the beginning of the alphabet How can we make sure to wrap to the end of the alphabet?
"""

msg = input("Type in your message to encrypt: ")
key = int(input("Type in the key you wish to use: "))
newMsg = ''

for i in range(0, len(msg)):
	num = ord(msg[i]) + key
	while num > ord('z'):
		num -= 26
	newMsg += chr(num)

print(newMsg)

msg = input("Type in your message to decrypt: ")
key = int(input("Type in the decryption key: "))
newMsg = ''

for i in range(0, len(msg)):
	num = ord(msg[i]) - key
	while num < ord('a'):
		num += 26
	newMsg += chr(num)

print(newMsg)
