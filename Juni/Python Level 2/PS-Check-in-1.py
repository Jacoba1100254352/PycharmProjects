# STRINGS AND VARIABLES

############################################

# What is a variable? Store the string “animal” in a variable called word. Store the number 42 in a variable called num. 
word = "animal"
num = 42

# Print one of the variables
print(word)

# What type of data is stored in num? Can you turn it into a string?
# Answer: integer (number ok as well)
str(num)

# Ask the user to guess an animal, and then to guess the color of that animal.
animal = input("Guess a type of animal: ")
color = input("Guess what color the animal is: ")

# Print the number of letters in the animal the user guessed (so that it works no matter what animal the user chose!)
print(len(animal))

# Print only the third letter in the color that the user guessed
print(color[2])

# Print a statement that tells the user what animal and color they guessed (make sure there’s a space between the color and animal!)
print("You guessed a " + color + " " + animal)

# Write a comment describing what the line you wrote for number 7 does
# ex: This tells the user what color and animal they guessed, by using the color and animal variables we got from the user input above, and adding it to a string that says "You guessed a "

#############################################

# LOOPS

#############################################

# What is a loop? What do we use it for?
# ex: We use it when we want to repeat some code over and over / when we want to do something multiple times!

# What is the difference between a for loop and a while loop? 
# ex: We use a for loop when we want to repeat a certain number of times, and a while loop if we want to repeat until a condition is met

# Print the numbers 0 to 10 using a for loop
for i in range(0, 11):
	print(i)

# Print each individual letter of the color from the user input above, using a for loop
for i in range(0, len(color)):
	print(color[i])

# Print every third number from 6 to 15 using a for loop
for i in range(6, 16, 3):
	print(i)

# Using a while loop, print the numbers 0 to 15
x = 0
while x < 16:
	print(x)
	x += 1

# Using a while loop, print every other letter of the animal that the user inputted, starting from the second letter.
i = 1
while i < len(animal):
	print(animal[i])
	i += 2

# Bonus Question: Print the numbers 1 to 10 using a while True loop
x = 1
while True:
	print(x)
	x += 1
	if x == 11:
		break

############################################

# CONDITIONALS

###########################################

# What is a conditional statement is? Can you think of an example of a conditional in real life?
# ex: An if-then statement; where we check if something is true; tells program to do something only if the condition is true..etc
# ex: If it's raining, I take an umbrella; if the light is red, then stop, etc

# Using the guesses that we asked the user for above, we want to check if the user guessed correctly! First things first, let’s just check if they guessed a cat. If the animal they guessed was a cat, tell the user “we love cats!”
if animal == "cat":
	print("we love cats!")

# Next, let’s tell the user whether they got the right answer of a black dog! Print “Correct answer!” if the animal is a black dog, print “Almost there!” if the animal is either black or a dog, and print “Incorrect answer :( ” if the user guessed neither.

if animal == "dog" and color == "black":
	print("Correct answer!")
elif animal == "dog" or color == "black":
	print("Almost there!")
else:
	print("Incorrect answer :(")

#  Do you remember what a nested if statement is? How would you change part of the above problem to include a nested if statement?
if animal == "dog":
	if color == "black":
		print("You're right!")
	else:
		print("You have the right animal! Try a different color")
else:
	print("Incorrect answer :(")

############################################

# OPTIONAL ADVANCED PROJECTS

############################################

# Ask the user for a word. If the word has an even number of letters,shift all the letters up one to the next letter in the alphabet. If the word has an odd number of letters, shift all the letters back one to the previous letter in the alphabet.
word = input("Enter a word: ")
newWord = ''
for i in range(0, len(word)):
	if len(word) % 2 == 0:
		newWord += chr(ord(word[i]) + 1)
	else:
		newWord += chr(ord(word[i]) - 1)
print(newWord)

# Ask the user for a word. For all even-numbered letters (e.g. index 0,2,4) in the word, shift the letter up one, and for all the odd-numbered letters (e.g. index 1,3) in the word, shift the letter down one.
word = input("enter a word: ")
newWord = ''
for i in range(0, len(word)):
	if i % 2 == 0:
		newWord += chr(ord(word[i]) + 1)
	else:
		newWord += chr(ord(word[i]) - 1)
print(newWord)
