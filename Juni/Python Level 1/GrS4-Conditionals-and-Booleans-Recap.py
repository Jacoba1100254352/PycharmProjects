# What are the two booleans?


# Write an if statement with a True condition that moves the turtle forward 50 steps.

import random
import turtle


t = turtle.Turtle()

if True:
	t.forward(50)

# Change your condition to compare 3 and 1 with a comparison operator.

if 3 > 1:
	t.forward(50)

# Change your condition to use 2 comparison operators and either an and or an or.

if 3 > 1 and 1 < 2:
	t.forward(50)

# This is the code that moves the turtle to a random place and then makes it turn 360 degrees if it is in Qudrant I or II

t.penup()
t.goto(random.randint(-200, 200), random.randint(-200, 200))
if t.ycor() > 0:
	t.right(360)

# Explain how the above code works:
# 
# Explain how we use an or statement to check if it is in Qudrant I, II, or III
#
