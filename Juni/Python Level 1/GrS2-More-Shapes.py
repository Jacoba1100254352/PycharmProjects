import turtle
t = turtle.Turtle()
t.speed(5)

screen = turtle.Screen()
screen.bgcolor("black")

t.pendown()
t.color('magenta')
t.begin_fill()
for i in range(6):
  t.forward(100)
  t.right(60)
t.end_fill()
t.penup()

t.goto(100,200)
t.pendown()
t.color('purple')
t.begin_fill()
for i in range(10):
  t.forward(30)
  t.right(36)
t.end_fill()
t.penup()

#star will not appear filled in repl.it however should be filled in on the student's web portal
t.goto(-150,150)
t.pendown()
t.color('teal')
t.begin_fill()
for i in range(5):
  t.forward(50)
  t.right(144)
t.end_fill()