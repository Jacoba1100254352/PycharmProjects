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
