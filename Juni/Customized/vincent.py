import math
import random
import turtle


v = turtle.Turtle()
v.goto(0, 0)
v.speed(0)

screen = turtle.Screen()

size = 45


def S():
	v.color("white")
	screen.bgcolor("black")


def N():
	v.penup()
	v.goto(-270, -60)
	v.down()
	
	# Snowglobe code :)
	v.left(90)
	smooth = 4
	for i in range(18 * smooth):
		v.forward(size / smooth)
		v.right(360 / (36 * smooth))
	v.forward(size / smooth)
	v.right(90)
	v.forward(36 * size / math.pi)


def O():
	v.goto(-12, v.ycor())
	v.fd(1)
	xOrigin = v.xcor()
	yOrigin = v.ycor()
	screen.tracer(0)
	radius = round(36 * size / (math.pi * 2))
	for i in range(1000):
		v.setheading(random.random() * 180)
		
		# Goto the location of the snowflake
		v.up()
		v.forward(random.randint(30, radius))
		v.down()
		
		# Draw Snowflake
		v.setheading(90)
		v.forward(1)
		
		# Return to starting position
		v.up()
		v.goto(xOrigin, yOrigin)
		v.down()
	screen.update()
	screen.tracer(1)
	v.setheading(180)
	v.forward(45)


def W():
	v.begin_fill()
	v.rt(90)
	v.fd(60)
	v.rt(50)
	v.fd(25)
	v.rt(70)
	v.fd(25)
	v.rt(60)
	v.fd(35)
	v.lt(110)
	v.fd(25)
	v.rt(40)
	v.fd(25)
	v.rt(70)
	v.fd(30)
	v.rt(90)
	v.fd(90)
	v.end_fill()


def clear():
	v.setheading(0)
	v.goto(0, 0)
	v.clear()


screen.onkey(S, "s")
screen.onkey(N, "n")
screen.onkey(O, "o")
screen.onkey(W, "w")
screen.onkey(clear, "c")
screen.listen()

turtle.done()

"""
        x = random.randint(-int(radius), int(radius)) + xOrigin
        y = random.randint(int(yOrigin), int(math.sqrt(abs(pow(radius, 2) - pow(x, 2))) + yOrigin))

        # Goto position of snowflake
        v.up()
        v.goto(x, y)
        v.down()

        # Draw Snowflake
        v.forward(2)
"""
