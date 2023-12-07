# Create a list to store the flavors
flavors = []

# Ask my 5 best friends for ice cream recommendations
for i in range(5):
    suggestion = input("Friend " + str(i + 1) + ", what kind of ice cream should I get? ")
    flavors.append(suggestion)

# Print out all of the suggestions
print("\nMy friends' suggestions:")
for flavor in flavors:
    print(flavor)

# Check if any of my friends recommended chocolate mudslide (my favorite flavor) or pistachio (my least favorite flavor)
numChocolateMudslide = 0
numPistachio = 0
for i in range(len(flavors)):
    if flavors[i] == "chocolate mudslide":
        numChocolateMudslide += 1
    elif flavors[i] == "pistachio":
        numPistachio += 1

print()
print(str(numChocolateMudslide) + " of my friends wanted chocolate mudslide, one of my favorite flavors!")
print(str(numPistachio) + " of my friends wanted pistachio, my least favorite flavor!")
