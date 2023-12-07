import random
import turtle

turtle.colormode(255)
t = turtle.Turtle()
t.speed(1000)

lineLength = 1

for i in range(360):
    # set random color
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    t.color(r, g, b)

    # draw line
    t.goto(0, 0)
    t.forward(lineLength)
    t.right(5)

    # increase length of line
    lineLength = lineLength + 1
