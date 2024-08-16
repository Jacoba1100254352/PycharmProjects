import random
import turtle


turtle.colormode(255)

t = turtle.Turtle()
screen = turtle.Screen()
t.speed(10000)
t.penup()


def randColor():
	r = random.randint(0, 255)
	g = random.randint(0, 255)
	b = random.randint(0, 255)
	t.color(r, g, b)


def randSpot():
	x = random.randint(-300, 300)
	y = random.randint(-300, 300)
	t.goto(x, y)


def drawSquare():
	randColor()
	randSpot()
	
	sideLength = random.randint(20, 100)
	
	t.pendown()
	t.begin_fill()
	for i in range(4):
		t.forward(sideLength)
		t.right(90)
	t.end_fill()
	t.penup()


def drawOctagon():
	randColor()
	randSpot()
	
	sideLength = random.randint(20, 100)
	
	t.pendown()
	t.begin_fill()
	for i in range(8):
		t.forward(sideLength)
		t.right(315)
	t.end_fill()
	t.penup()


def drawFirework():
	randColor()
	
	x = random.randint(-300, 300)
	y = random.randint(-300, 300)
	
	for i in range(36):
		t.goto(x, y)
		t.pendown()
		t.forward(20)
		t.right(10)
		t.penup()


def drawCircle():
	randColor()
	randSpot()
	
	sideLength = random.randint(5, 20)
	
	t.pendown()
	t.begin_fill()
	for i in range(36):
		t.forward(sideLength)
		t.right(10)
	t.end_fill()
	t.penup()


t.goto(0, 0)

screen.onkey(drawSquare, "Up")
screen.onkey(drawOctagon, "Down")
screen.onkey(drawFirework, "Left")
screen.onkey(drawCircle, "Right")
screen.listen()
