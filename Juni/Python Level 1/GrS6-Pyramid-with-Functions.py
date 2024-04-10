import turtle


turtle.colormode(255)

t = turtle.Turtle()
t.speed(10000)


def drawTriangle(sideLength):
	for i in range(3):
		t.forward(sideLength)
		t.right(120)


sideLength = 10

for i in range(50):
	t.penup()
	t.goto(0, 200)
	t.setheading(300)
	t.pendown()
	
	drawTriangle(sideLength)
	sideLength = sideLength + 10
