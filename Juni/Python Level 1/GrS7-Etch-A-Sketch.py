import turtle


t = turtle.Turtle()
screen = turtle.Screen()

move_speed = 10
turn_speed = 10


def moveForward():
	t.pendown()
	t.forward(move_speed)


def moveBackward():
	t.pendown()
	t.backward(move_speed)


def turnLeft():
	t.left(turn_speed)


def turnRight():
	t.right(turn_speed)


t.goto(0, 0)

# associating event listeners with functions
screen.onkey(moveForward, "Up")
screen.onkey(moveBackward, "Down")
screen.onkey(turnLeft, "Left")
screen.onkey(turnRight, "Right")
screen.listen()
