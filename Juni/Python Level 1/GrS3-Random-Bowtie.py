import random
import turtle


turtle.colormode(255)

t = turtle.Turtle()
t.speed(10000)
screen = turtle.Screen()

# set random background color
r = random.randint(0, 255)
g = random.randint(0, 255)
b = random.randint(0, 255)
screen.bgcolor(r, g, b)

# draw right half of bowtie
t.left(30)
r = random.randint(0, 255)
g = random.randint(0, 255)
b = random.randint(0, 255)
t.color(r, g, b)
t.begin_fill()
for i in range(3):
	t.forward(80)
	t.right(120)
t.end_fill()

# draw left half of bowtie
t.right(180)
r = random.randint(0, 255)
g = random.randint(0, 255)
b = random.randint(0, 255)
t.color(r, g, b)
t.begin_fill()
for i in range(3):
	t.forward(80)
	t.right(120)
t.end_fill()
