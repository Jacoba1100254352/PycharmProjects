import random
import turtle


turtle.colormode(255)

t = turtle.Turtle()
t.speed(10)


def drawSquare(sideLength, r, g, b):
	t.color(r, g, b)
	
	for i in range(4):
		t.forward(sideLength)
		t.right(90)


for i in range(4):
	r = random.randint(0, 255)
	g = random.randint(0, 255)
	b = random.randint(0, 255)
	
	length = 20
	
	for j in range(3):
		length += 20
		drawSquare(length, r, g, b)
	
	t.right(90)
