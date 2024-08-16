import random
import turtle


turtle.colormode(255)

t = turtle.Turtle()
t.speed(1000)

r = random.randint(0, 255)
g = random.randint(0, 255)
b = 0

for i in range(180):
	t.color(r, g, b)
	
	t.forward(100)
	t.right(30)
	t.forward(20)
	t.left(60)
	t.forward(50)
	t.right(30)
	
	t.penup()
	t.goto(0, 0)
	t.pendown()
	
	t.right(2)
	
	b = b + 2
