#########################################

# PYTHON TURTLE BASICS

#########################################

# When working with Python with Turtle, what do we first need to make sure to import? Can you think of anything else we usually import? 
# Write out both import statements. Why do we need to use these import statements?

import random
import turtle

# Create a Turtle named whale.

whale = turtle.Turtle()
whale.speed(100000)

# Make whale move forward 200 pixels.

whale.forward(200)

# Make whale turn 200 degrees to the right.
whale.right(200)

# Draw a red square with a side length of 50 pixels

whale.color("red")
for i in range(4):
    whale.right(90)
    whale.forward(50)

# Move the turtle to the coordinates (-100, -100) and draw another square which is filled in. Make sure not to draw a line between the two squares.

whale.penup()
whale.goto(-100, -100)
whale.pendown()

whale.color("red")
whale.begin_fill()
for i in range(4):
    whale.right(90)
    whale.forward(50)
whale.end_fill()

#########################################

# LOOPS

#########################################

# Can you explain to me what a loop is? Why are loops useful in programming?


# Write a loop that makes whale move forward 2 pixels, repeating 20 times.

for i in range(20):
    whale.forward(2)

# A dodecagon is a 12-sided shape. Can you draw a dodecagon using a loop?.

for i in range(12):
    whale.left(360 / 12)
    whale.forward(30)

# Loops-4: Draw another dodecagon which is smaller than the first.

for i in range(12):
    whale.left(360 / 12)
    whale.forward(10)

# Program whale to draw a circle using a loop that repeats 36 times.

for i in range(36):
    whale.forward(15)
    whale.right(360 / 36)

#########################################

# VARIABLES AND RANDOM

#########################################

# Create a variable called numPotatoes and set it to a random number between 42 and 90.

numPotatoes = random.randint(42, 90)

# What are the three variables we often use when defining a color? What do they stand for? What happens if we make one of them a larger number than the rest? 

# Ans: r,g,b. They stand for red, green, and blue, which are the base colors we combine to make a specific color in computer graphics; the color would be "more" of the base color you made larger (e.g. a shade closer to red)

# Use these three variables to set the color of whale to a random color. Test it out and see if we get a different color each time!

r = random.randint(0, 255)
g = random.randint(0, 255)
b = random.randint(0, 255)
whale.color(r, g, b)
whale.forward(100)

# Bonus: Try to set the color of whale randomly without creating any r,g,b variables. (Hint: You can do this in one line of code.)

whale.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

#########################################

# CONDITIONALS

#########################################

# What is a conditional statement?
# Ans: A conditional is an if-then statement that tells the program to do something only if the condition is true (else, do something else).

# Create a variable called num and set it to a random number between 0 and 10. If num is less than 5, set it equal to 0. If num is equal to 5, set it to 10. Otherwise, set it to 15.

num = random.randint(0, 10)
if num < 5:
    num = 0
elif num == 5:
    num = 10
else:
    num = 15

# Use a conditional to change whale’s color to blue if whale is in quadrant III. Test your conditional statements by setting the turtle's position to various locations on the canvas.

if whale.xcor() < 0 and whale.ycor() < 0:
    whale.color("blue")

# Write another conditional which turns whale’s color to green if its x-coordinate is over 100 or its y-coordinate is less than -100.

if whale.xcor() > 100 or whale.ycor() < -100:
    whale.color("green")
