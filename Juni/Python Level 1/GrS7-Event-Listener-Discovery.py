import turtle


juni = turtle.Turtle()
screen = turtle.Screen()

juni.goto(0, 0)


def square():
	for i in range(4):
		juni.forward(40)
		juni.right(90)


screen.onkey(square, 's')
screen.listen()
