import random

# reads words into list
f = open("valid_words.txt")
validWords = f.readlines()
validWords = [x.strip() for x in validWords]
f.close()

monkeyStr = ""
print("Here's what the monkeys are typing on the typewriter:")
while True:
    # add a random character to the end of the monkeys' typing
    monkeyStr += chr(random.randint(ord('a'), ord('z')))
    print(monkeyStr)

    # check if last three letters are a valid word
    if len(monkeyStr) >= 3:

        # get the last three letters of what has been typed
        # Pythonic shortcut: lastThreeLetters = monkeyStr[len(monkeyStr)-3:len(monkeyStr)]
        lastThreeLetters = ""
        for i in range(len(monkeyStr) - 3, len(monkeyStr)):
            lastThreeLetters += monkeyStr[i]

        if lastThreeLetters in validWords:
            print("The monkeys did it! " + lastThreeLetters + " is a word!")
            break
