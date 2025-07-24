import random
import turtle

# Set up turtle color mode
turtle.colormode(255)

# Set up turtle
t = turtle.Turtle()
t.speed(0)

# Set up screen
screen = turtle.Screen()
screen.tracer(0)

# Pick random colors for image gradiant
r = random.randint(0, 255)
g = random.randint(0, 255)
b = 0

# Draw squares
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
	screen.update()
