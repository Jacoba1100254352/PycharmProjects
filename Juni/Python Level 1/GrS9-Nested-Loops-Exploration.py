import turtle


juni = turtle.Turtle()

sideLength = 30

for i in range(3):
	for i in range(4):
		juni.forward(sideLength)
		juni.right(90)
	
	sideLength += 20
