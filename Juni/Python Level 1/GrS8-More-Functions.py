import turtle


t = turtle.Turtle()
t.speed(0)


def drawSquare(sideLength):
	t.pendown()
	for i in range(4):
		t.forward(sideLength)
		t.right(90)
	t.penup()


def drawTriangle(sideLength):
	t.pendown()
	for i in range(3):
		t.forward(sideLength)
		t.right(120)
	t.penup()


drawSquare(100)
drawTriangle(200)

# How would we make the turtle draw ten different squares, starting from a side length of 20 and going up by 5 each time?

sideLength = 20
for i in range(10):
	drawSquare(sideLength)
	sideLength += 5
