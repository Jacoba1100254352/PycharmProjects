import random
import turtle

turtle.colormode(255)

t = turtle.Turtle()
t.speed(10000)

screen = turtle.Screen()
screen.bgcolor("black")

r = random.randint(0, 255)
g = random.randint(0, 255)
b = 0
length = 20
for i in range(40):
    t.color(r, g, b)

    t.begin_fill()
    for j in range(4):
        t.forward(length)
        t.right(90)
    t.end_fill()

    b += 5
    length += 5
    t.right(10)
