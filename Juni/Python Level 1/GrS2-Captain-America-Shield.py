import turtle


t = turtle.Turtle()
t.speed(0)
t.color("red")

t.penup()
t.goto(0, 195)
t.pendown()

t.begin_fill()
for i in range(40):
	t.forward(30)
	t.right(9)
t.end_fill()

t.penup()
t.goto(0, 165)
t.pendown()

t.color("light grey")
t.begin_fill()
for i in range(40):
	t.forward(25)
	t.right(9)
t.end_fill()

t.penup()
t.goto(0, 135)
t.pendown()

t.color("red")
t.begin_fill()
for i in range(40):
	t.forward(20)
	t.right(9)
t.end_fill()

t.penup()
t.goto(0, 105)
t.pendown()

t.color("blue")
t.begin_fill()
for i in range(40):
	t.forward(15)
	t.right(9)
t.end_fill()

t.penup()
t.goto(-60, 35)
t.pendown()
t.color("white")

# star will not appear filled in repl.it however should be filled in on the student's web portal
t.begin_fill()
for i in range(5):
	t.forward(140)
	t.right(144)
t.end_fill()
