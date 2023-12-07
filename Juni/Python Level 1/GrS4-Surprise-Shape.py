import random
import turtle

turtle.colormode(255)
t = turtle.Turtle()
t.speed(10000)

r = random.randint(0, 255)
g = random.randint(0, 255)
b = random.randint(0, 255)
t.color(r, g, b)

num = random.randint(0, 3)

t.begin_fill()
if num == 0:
    for i in range(4):
        t.forward(100)
        t.right(90)
elif num == 1:
    for i in range(3):
        t.forward(100)
        t.right(120)
elif num == 2:
    for i in range(6):
        t.forward(100)
        t.right(60)
else:
    for i in range(36):
        t.forward(5)
        t.right(10)
t.end_fill()
