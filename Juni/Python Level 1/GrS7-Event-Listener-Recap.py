import random
import turtle


juni = turtle.Turtle()

# What else do we need to create to make an event listener:

screen = turtle.Screen()


# Explain what an event listener is:
#

# List out the three parts of an event listener:
# 

# Write a function that moves the turtle to a random location

def move():
	juni.penup()
	juni.goto(random.randint(-200, 200), random.randint(-200, 200))
	juni.pendown()


# Write a function that draws something, such as a flower or an octogon

def draw():
	for i in range(8):
		juni.forward(30)
		juni.right(360 / 8)


# Make it so the turtle moves to a random place when you press the 'r' key, and so it draws your object when you press the 'd' key

screen.onkey(move, "r")
screen.onkey(draw, "d")

# Add the last command you need for event listeners?

screen.listen()
