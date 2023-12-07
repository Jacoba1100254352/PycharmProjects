# How do we include the ability to use random numbers into our file:

import random
import turtle

turtle.colormode(255)

# What is the difference between an integer and a string? Give an example of both:

# Make a variable which holds a string and another that holds an integer:

string = "hello world"
integer = 3

# Make a new variable called randomNum which holds a random number between 0-100:

num = random.randint(0, 100)

# This is how I draw a triangle with a random color and random size:

r = random.randint(0, 255)
g = random.randint(0, 255)
b = random.randint(0, 255)
size = random.randint(25, 50)

t = turtle.Turtle()
t.color(r, g, b)
for i in range(3):
    t.forward(size)
    t.right(120)

# Explain how the above code works:
#
# Explain how we could also make the triangle we drew appear at random coordinates:
#

# *bonus* How can I double the range of sizes my triangle could be if I start with sideLength = random.randint(0,50):

sideLength = random.randint(0, 50)
for i in range(3):
    t.forward(2 * sideLength)
    t.right(120)
