import random
import turtle


turtle.colormode(255)

t = turtle.Turtle()
t.speed(1000)

numShapes = random.randint(10, 50)

for i in range(numShapes):
	# Go to random position
	t.penup()
	x = random.randint(-200, 200)
	y = random.randint(-200, 200)
	t.goto(x, y)
	t.pendown()
	
	# Turn in random direction
	turnAmount = random.randint(0, 360)
	t.right(turnAmount)
	
	# Make turtle random color
	r = random.randint(0, 255)
	g = random.randint(0, 255)
	b = random.randint(0, 255)
	t.color(r, g, b)
	
	numSides = random.randint(3, 9)
	turnAngle = 360.0 / numSides
	sideLength = random.randint(5, 60)
	
	# Draw the shape!
	t.begin_fill()
	for i in range(numSides):
		t.forward(sideLength)
		t.right(turnAngle)
	t.end_fill()
