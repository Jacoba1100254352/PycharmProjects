upper = input("Enter a word in all uppercase: ")
lower = ""

# calculate the numerical difference between the ASCII representation of A and a
difference = ord('A') - ord('a')

# iterate through the inputted string and apply this different to each character
for i in range(0, len(upper)):
    char = upper[i]
    lower += chr(ord(char) - difference)

print("The word in all lowercase is: " + lower)
