import random
import turtle


turtle.colormode(255)

juni = turtle.Turtle()

for i in range(4):
	r = random.randint(0, 255)
	g = random.randint(0, 255)
	b = random.randint(0, 255)
	juni.color(r, g, b)
	
	sideLength = 30
	
	for i in range(3):
		for i in range(4):
			juni.forward(sideLength)
			juni.right(90)
		
		sideLength += 20
	
	juni.right(90)
