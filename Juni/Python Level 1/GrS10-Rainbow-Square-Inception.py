import random
import turtle

turtle.colormode(255)

t = turtle.Turtle()
t.speed(100000)

r = random.randint(0, 255)
g = random.randint(0, 255)
b = 0

for i in range(36):
    b += 20
    t.color(r, g, b)
    length = 20

    for j in range(15):
        length += 10

        for k in range(4):
            t.forward(length)
            t.right(90)

    t.right(10)
