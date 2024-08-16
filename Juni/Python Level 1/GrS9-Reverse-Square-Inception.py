import random
import turtle


turtle.colormode(255)

t = turtle.Turtle()
t.speed(10)

for i in range(4):
	length = 80
	
	for j in range(3):
		length -= 20
		
		r = random.randint(0, 255)
		g = random.randint(0, 255)
		b = random.randint(0, 255)
		t.color(r, g, b)
		
		t.begin_fill()
		for k in range(4):
			t.forward(length)
			t.right(90)
		t.end_fill()
	
	t.right(90)
