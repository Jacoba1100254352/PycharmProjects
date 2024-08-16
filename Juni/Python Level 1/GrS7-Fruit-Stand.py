import random
import turtle


fruit = turtle.Turtle()
fruit.speed(1000)
fruit.width(5)

screen = turtle.Screen()
screen.bgcolor("light blue")


def orange():
	x = random.randint(-200, 200)
	y = random.randint(-200, 200)
	fruit.penup()
	fruit.goto(x, y)
	fruit.setheading(0)
	fruit.color("orange")
	fruit.pendown()
	
	fruit.begin_fill()
	for i in range(36):
		fruit.forward(7)
		fruit.right(10)
	fruit.end_fill()


def starfruit():
	x = random.randint(-200, 200)
	y = random.randint(-200, 200)
	fruit.penup()
	fruit.goto(x, y)
	fruit.setheading(0)
	fruit.color("yellow")
	fruit.pendown()
	
	fruit.begin_fill()
	for i in range(5):
		fruit.forward(50)
		fruit.right(144)
	fruit.end_fill()


def cherry():
	x = random.randint(-200, 200)
	y = random.randint(-200, 200)
	fruit.penup()
	fruit.goto(x, y)
	fruit.setheading(0)
	fruit.color("dark red")
	fruit.pendown()
	
	fruit.begin_fill()
	for i in range(36):
		fruit.forward(2)
		fruit.right(10)
	fruit.end_fill()
	
	# draw the stem
	fruit.left(90)
	fruit.forward(15)


screen.onkey(orange, "1")
screen.onkey(starfruit, "2")
screen.onkey(cherry, "3")
screen.listen()
