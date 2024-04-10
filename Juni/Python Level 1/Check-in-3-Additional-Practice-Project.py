import random
import turtle


ball = turtle.Turtle()
ball.penup()
ball.goto(random.randint(-300, 300), random.randint(-300, 300))
ball.shape("circle")
ball.color("red")

t = turtle.Turtle()
t.penup()
t.goto(0, 0)
t.shape("turtle")
t.color("blue")


def aim():
	t.pendown()
	t.forward(300)


screen = turtle.Screen()
screen.onkey(aim, "space")
screen.listen()

while True:
	# only spins when the turtle hasn't moved
	if t.xcor() == 0 and t.ycor() == 0:
		t.left(10)
	else:
		break
