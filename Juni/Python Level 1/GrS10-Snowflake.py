import random
import turtle


turtle.colormode(255)

t = turtle.Turtle()
t.speed(1000)

r = random.randint(0, 255)
g = random.randint(0, 255)
b = random.randint(0, 255)
t.color(r, g, b)
t.pensize(5)
t.pendown()

for i in range(6):
	t.goto(0, 0)
	
	for j in range(10):
		# draw part of the branch
		t.forward(10)
		
		# draw a little side branch
		t.right(45)
		t.forward(20)
		t.backward(20)
		
		# draw the symmetrical little side branch
		t.left(90)
		t.forward(20)
		t.backward(20)
		
		# reset positioning
		t.right(45)
	
	# turn to start drawing the next branch
	t.right(60)
