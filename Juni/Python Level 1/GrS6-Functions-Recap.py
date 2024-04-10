# Explain what a function is:
#
# What are the two parts of a function? What do they each do?
#
# Define a function that draws a square with a side length of 50

import turtle


turtle.colormode(255)
t = turtle.Turtle()


def drawSquare():
	for i in range(4):
		t.forward(50)
		t.right(90)


# Call your function

drawSquare()

# Call your function 2 more times in different locations

t.penup()
t.goto(-100, 100)
t.pendown()
drawSquare()

t.penup()
t.goto(100, -100)
t.pendown()
drawSquare()
