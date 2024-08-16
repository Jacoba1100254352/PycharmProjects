import random
import turtle


juni = turtle.Turtle()

# Use a commonplace example to explain how if and else work together?
#


# Make a random number between 1 and 10. If the number is less than or equal to 5, make a turtle do a leftword spin. Otherwise, make a turtle do a rightword spin.

num = random.randint(1, 10)
if num <= 5:
	juni.left(360)
else:
	juni.right(360)

# Explain how you use elif.
#


# What will be checked first, the if condition or the elif condition?
#


# Edit your code so that if the random number is less than or equal to 7 or greater than 5 that the turtle draws a triangle.

if num <= 5:
	juni.left(360)
elif num <= 7:
	for i in range(36):
		juni.forward(1)
		juni.right(10)
else:
	juni.right(360)

# Change your code so that your random number is between 1 and 20. Next, add 2 more elifs which draw a triangle and rectangle if other possible numbers occur.

num = random.randint(1, 20)
if num <= 5:
	juni.left(360)
elif num <= 7:
	for i in range(36):
		juni.forward(1)
		juni.right(10)
elif num <= 10:
	for i in range(2):
		juni.forward(50)
		juni.right(90)
		juni.forward(100)
		juni.right(90)
elif num <= 15:
	for i in range(3):
		juni.forward(100)
		juni.right(120)
else:
	juni.right(360)
