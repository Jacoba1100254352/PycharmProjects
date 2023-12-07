import random
import turtle

turtle.colormode(255)
t = turtle.Turtle()
t.penup()

# set random color
r = random.randint(0, 255)
g = random.randint(0, 255)
b = random.randint(0, 255)
t.color(r, g, b)

# set random side length
sideLength = random.randint(0, 200)

# set random starting position
x = random.randint(-300, 300)
y = random.randint(-300, 300)
t.goto(x, y)

# draw square
t.pendown()
t.begin_fill()
for i in range(4):
    t.forward(sideLength)
    t.right(90)
t.end_fill()

t.penup()
