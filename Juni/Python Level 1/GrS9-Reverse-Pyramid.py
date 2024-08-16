import random
import turtle


turtle.colormode(255)
t = turtle.Turtle()
t.penup()
t.speed(10000)

sideLength = 500

for i in range(50):
	r = random.randint(0, 255)
	g = random.randint(0, 255)
	b = random.randint(0, 255)
	t.color(r, g, b)
	
	t.goto(0, 200)
	t.setheading(300)
	t.pendown()
	
	t.begin_fill()
	for j in range(3):
		t.forward(sideLength)
		t.right(120)
	t.end_fill()
	
	sideLength = sideLength - 10
	t.penup()
