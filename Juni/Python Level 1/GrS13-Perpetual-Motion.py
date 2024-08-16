import turtle


t = turtle.Turtle()
screen = turtle.Screen()

t.shape("turtle")
t.penup()


def turnLeft():
	t.left(5)


def turnRight():
	t.right(5)


screen.onkey(turnLeft, "Left")
screen.onkey(turnRight, "Right")
screen.listen()

while True:
	t.forward(1)
