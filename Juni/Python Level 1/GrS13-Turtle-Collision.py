 import random
import turtle


turtle.colormode(255)

t = turtle.Turtle()
t2 = turtle.Turtle()
screen = turtle.Screen()


def turnLeft1():
	t.left(10)


def turnRight1():
	t.right(10)


def turnLeft2():
	t2.left(10)


def turnRight2():
	t2.right(10)


def checkCollision():
	if abs(t.xcor() - t2.xcor()) < 10 and abs(t.ycor() - t2.ycor()) < 10:
		t.write("Collision!")
		t.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
		t2.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


screen.onkey(turnLeft1, "Left")
screen.onkey(turnRight1, "Right")
screen.onkey(turnLeft2, "a")
screen.onkey(turnRight2, "d")
screen.listen()

# start turtles at a random location
t.penup()
t2.penup()
t.goto(random.randint(-200, 200), random.randint(-200, 200))
t2.goto(random.randint(-200, 200), random.randint(-200, 200))
t.pendown()
t2.pendown()
t2.color("blue")

# both turtles continuously move and check for collisions
while True:
	t.forward(1)
	t2.forward(1)
	checkCollision()
