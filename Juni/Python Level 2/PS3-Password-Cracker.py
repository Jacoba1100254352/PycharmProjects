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
