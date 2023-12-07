# Code I need at the top of every project is:

import turtle

# I create a turtle with this line:

t = turtle.Turtle()

# I move that turtle forward with this command:

t.forward(10)

# I turn the turtle with these commands:

t.right(90)
t.left(90)

# I change the turtles color with this command:

t.color("yellow")

# I move the turtle to a new place without leaving a line with these commands:

t.penup()
t.goto(50, 50)
t.pendown()

# Explain how the above commands work:
# 

# I draw a filled in square with these commands:

t.begin_fill()
for i in range(4):
    t.forward(100)
    t.right(90)
t.end_fill()
