# This code is needed at the beginning of every project:

import turtle

t = turtle.Turtle()

# This is how I write a loop that draws a square:

for i in range(4):
    t.forward(50)
    t.right(90)

# Explain how the computer knows how many times to repeat the loop:
# 

# Here I added code that will move the turtle to a new spot:

t.penup()
t.goto(100, 100)
t.pendown()

# This is how I write a loop that draws a circle:

for i in range(36):
    t.forward(3)
    t.right(10)

# Explain how the above code works:
# 
# Explain how I could draw  a half circle:
# 

# Here I added code that will move the turtle to a new spot:

t.penup()
t.goto(-100, -100)
t.pendown()

# This is how I write a loop that draws a rectangle:

for i in range(2):
    t.forward(100)
    t.right(90)
    t.forward(30)
    t.right(90)
