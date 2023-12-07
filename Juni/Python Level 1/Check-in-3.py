#########################################

# Nested Loops

#########################################

import random
import turtle

turtle.colormode(255)
lion = turtle.Turtle()
lion.speed(0)

# What is a nested loop and why do we use them in python?
# Write code which will move lion to a random place on the screen 5 times, drawing a square each time it moves, using a nested loop.

for i in range(5):
    lion.penup()
    lion.goto(random.randint(-200, 200), random.randint(-200, 200))
    lion.pendown()
    for i in range(4):
        lion.forward(50)
        lion.right(90)

# Alter your code to draw 3 triangles instead.

for i in range(3):
    lion.penup()
    lion.goto(random.randint(-200, 200), random.randint(-200, 200))
    lion.pendown()
    for i in range(3):
        lion.forward(50)
        lion.right(120)

# How many lines does our turtle make in our new code?
# Make a while true loop which breaks after its fifth iteration.

counter = 0
while True:
    counter += 1
    if counter >= 5:
        break

#########################################

# Conditionals

#########################################

# What is the difference between elif and else? When do we use one or the other in Python?
# Create a variable called num which holds a random number between 0 and 60. If the number is between 0 and 20, change lion’s color to red. If the number is between 21 and 40, change lion’s color to yellow. Otherwise, change lion’s color to green.

num = random.randint(0, 60)
if num <= 20:
    lion.color("red")
elif num <= 40:
    lion.color("yellow")
else:
    lion.color("green")

#########################################

# Lists

#########################################

# What is a list? Why do we use lists in Python?
# Create an empty list called whales.

whales = []

# Create three more turtles (name them anything) and add them to the list.

for i in range(3):
    whales.append(turtle.Turtle())

# Use a loop to move each turtle in our list backward by 30 pixels.

for whale in whales:
    whale.backward(30)
