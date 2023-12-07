import random
import turtle

turtle.colormode(255)

t = turtle.Turtle()
t.speed(10000)


def drawShape(sideLength, numSides):
    for i in range(numSides):
        t.forward(sideLength)
        t.right(360 / numSides)


r = 0
g = random.randint(0, 255)
b = random.randint(0, 255)
t.color(r, g, b)

sideLength = random.randint(10, 30)
numSides = random.randint(2, 12)

for i in range(100):
    drawShape(sideLength, numSides)
    t.right(10)
    sideLength += 1
    r += 1
    t.color(r, g, b)
