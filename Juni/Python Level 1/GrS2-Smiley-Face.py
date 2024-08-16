import turtle


#
t = turtle.Turtle()
screen = turtle.Screen()

#
t.speed(1000)
screen.bgcolor("yellow")

#
t.penup()
t.goto(-100, 200)
t.pendown()

#
for _ in range(2):
	t.forward(10)
	t.right(90)
	t.forward(100)
	t.right(90)

#
t.penup()
t.goto(50, 200)
t.pendown()

#
for _ in range(2):
	t.forward(10)
	t.right(90)
	t.forward(100)
	t.right(90)

#
t.penup()
t.goto(-200, 0)
t.pendown()

#
t.right(90)
for _ in range(37):
	t.forward(15)
	t.left(5)
