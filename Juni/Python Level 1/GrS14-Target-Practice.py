import random
import turtle


t = turtle.Turtle()
t.shape("turtle")
t.color("white")
t.goto(0, 0)

screen = turtle.Screen()
screen.bgcolor("black")

# set up target
target = turtle.Turtle()
target.speed(1000)
target.color("aquamarine")
target.shape("circle")
target.penup()
target.goto(random.randint(-200, 200), random.randint(-200, 200))


# set up turn controls for player turtle (left/right)
def turnLeft():
	t.left(10)


def turnRight():
	t.right(10)


# set up shoot function, which shoots yellow bullet (pointing in direction of the turtle) and detects if there's a hit
def shoot():
	bullet = turtle.Turtle()
	bullet.penup()
	bullet.color("yellow")
	bullet.speed(1000)
	bullet.setheading(t.heading())
	
	for i in range(300):
		bullet.forward(10)
		if bullet.xcor() > target.xcor() - 10 and bullet.xcor() < target.xcor() + 10 and bullet.ycor() > target.ycor() - 10 and bullet.ycor() < target.ycor() + 10:
			bullet.ht()
			target.goto(random.randint(-200, 200), random.randint(-200, 200))


screen.onkey(turnLeft, "Left")
screen.onkey(turnRight, "Right")
screen.onkey(shoot, "space")
screen.listen()
