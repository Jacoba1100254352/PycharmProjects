# I have 15 Snickers, 7 Almond Joys, 6 Twix, 9 Kit Kats, 3 Reese's Cups, and 2 Butterfingers
candies = {
    "Snickers": 15,
    "Almond Joy": 7,
    "Twix": 6,
    "Kit Kat": 9,
    "Reese's Cups": 3,
    "Butterfingers": 2
}

# Print how many I have of each type of candy
print("A count of each of my candies:")
for candy in candies:
    print(candy + ": " + str(candies[candy]))

# Oops, I forgot that I ate one of each kind of candy. I need to subtract one from each count!
for candy in candies:
    candies[candy] -= 1

# I traded all of my Twixes to my friend for 4 Junior Mints
candies["Twix"] = 0
candies["Junior Mints"] = 4

print()
print("An updated count of each of my candies:")
for candy in candies:
    print(candy + ": " + str(candies[candy]))

# Bonus: Calculate and print out the total pieces of candy I now own
'''
total = 0
for candy in candies:
  total += candies[candy]
print("I now have " + str(total) + " pieces of candy!")
'''
