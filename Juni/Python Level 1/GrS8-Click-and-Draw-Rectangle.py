import random
import turtle


turtle.colormode(255)

juni = turtle.Turtle()
juni.speed(0)
juni.goto(0, 0)

screen = turtle.Screen()


def drawRectangle(x, y):
	r = random.randint(0, 255)
	g = random.randint(0, 255)
	b = random.randint(0, 255)
	
	juni.color(r, g, b)
	
	for i in range(2):
		juni.forward(x)
		juni.left(90)
		juni.forward(y)
		juni.left(90)


screen.onclick(drawRectangle)
screen.listen()
