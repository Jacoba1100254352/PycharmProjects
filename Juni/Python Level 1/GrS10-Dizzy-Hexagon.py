import turtle
from random import randint


turtle.colormode(255)

t = turtle.Turtle()
t.speed(1000)

for _ in range(100):
	r = randint(0, 255)
	g = randint(0, 255)
	b = randint(0, 255)
	t.color(r, g, b)
	
	t.begin_fill()
	for _ in range(6):
		t.right(60)
		t.forward(50)
	t.end_fill()
	
	t.right(10)
