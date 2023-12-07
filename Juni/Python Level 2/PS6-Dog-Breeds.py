dogs = ["beagle", "collie", "greyhound", "komondor", "mastiff", "pug", "terrier"]

for dog in dogs:
    firstLetter = dog[0]
    numLetters = str(len(dog))
    print(
        "A " + dog + " is a dog breed. Its name starts with the letter " + firstLetter + ", and its name has " + numLetters + " letters in it.\n")
