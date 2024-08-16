import random
import turtle


turtle.colormode(255)

t = turtle.Turtle()
t.speed(1000)

side = 10

counter = 0
while counter < 50:
	r = random.randint(0, 255)
	g = random.randint(0, 255)
	b = random.randint(0, 255)
	t.color(r, g, b)
	
	t.forward(side)
	t.right(90)
	
	side = side + 5
	counter += 1
