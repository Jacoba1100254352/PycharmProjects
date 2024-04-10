import turtle


turtle.colormode(255)

t = turtle.Turtle()
t.color("white")
t.speed(100)
t.setheading(300)
t.penup()
t.goto(-10, 200)
t.pendown()

s = turtle.Screen()
s.bgcolor('black')

n = 300

for i in range(200):
	t.forward(n)
	t.right(119)
	n = n - 3

t.ht()
