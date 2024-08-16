import random
import turtle


screen = turtle.Screen()
screen.bgcolor("black")

# draw Earth
earth = turtle.Turtle()
earth.speed(10000)
earth.penup()
earth.goto(-200, 0)
earth.color("deep sky blue")
earth.pendown()
earth.begin_fill()
for i in range(36):
	earth.forward(10)
	earth.right(10)
earth.end_fill()
earth.ht()

# draw moon
moon = turtle.Turtle()
moon.speed(10000)
moon.penup()
moon.goto(200, -25)
moon.color("light slate gray")
moon.pendown()
moon.begin_fill()
for i in range(36):
	moon.forward(5)
	moon.right(10)
moon.end_fill()
moon.ht()


def launch():
	t = turtle.Turtle()
	t.color("red")
	t.shape("turtle")
	t.speed(10000)
	t.penup()
	t.goto(-200, -50)
	t.speed(10)
	travelDist = random.randint(200, 500)
	t.forward(travelDist)
	if travelDist > 400:
		t.color("white")


screen.onkey(launch, "space")
screen.listen()
