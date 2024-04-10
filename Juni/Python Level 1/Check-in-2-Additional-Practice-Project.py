import random
import turtle


t = turtle.Turtle()
t.right(45)
t.speed(0)

screen = turtle.Screen()


def changeColor():
	t.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


def drawDiamond():
	sideLength = 10
	for i in range(3 * 4):
		changeColor()
		t.forward(sideLength)
		t.right(90)
		sideLength += 2


def changeLocation():
	t.penup()
	t.goto(random.randint(-200, 200), random.randint(-200, 200))
	t.pendown()


def drawCircle():
	sideLength = 1
	for i in range(3 * 36):
		sideLength += 1
		changeColor()
		t.forward(sideLength)
		t.right(10)


def drawPyramid():
	sideLength = 20
	for i in range(3 * 3):
		sideLength += 5
		changeColor()
		t.forward(sideLength)
		t.right(120)


screen.onkey(drawDiamond, "d")
screen.onkey(drawCircle, "c")
screen.onkey(drawPyramid, "p")
screen.onkey(changeLocation, "space")
screen.listen()
