import turtle

t = turtle.Turtle()
t.speed(1000)

t.color("yellow")
t.penup()
t.goto(-100,-100)
t.pendown()

t.begin_fill()
t.forward(200)
t.left(90)
t.forward(200)

for i in range(18):
  t.forward(18)
  t.left(10)

t.forward(220)
t.left(90)
t.end_fill()

t.color("black")
t.penup()
t.goto(-105, 115)
t.pendown()

t.begin_fill()
for i in range(2):
  t.forward(205)
  t.right(90)
  t.forward(20)
  t.right(90)
t.end_fill()

t.color("silver")
t.penup()
t.goto(-60, 110)
t.pendown()

t.right(90)
t.begin_fill()
for i in range(36):
  t.forward(10)
  t.left(10)
t.end_fill()

t.color("white")
t.penup()
t.goto(-38,110)
t.pendown()

t.begin_fill()
for i in range(36):
  t.forward(6)
  t.left(10)
t.end_fill()

t.color("brown")
t.penup()
t.goto(-15,110)
t.pendown()

t.begin_fill()
for i in range(36):
  t.forward(2)
  t.left(10)
t.end_fill()

t.left(90)
t.penup()
t.goto(-105,-30)
t.pendown()

t.begin_fill()
t.color("blue")
t.forward(30)
t.right(90)
t.forward(50)
t.left(90)
t.forward(150)
t.left(90)
t.forward(50)
t.right(90)
t.forward(25)
t.right(90)
t.forward(70)
t.right(90)
t.forward(207)
t.right(90)
t.forward(70)
t.end_fill()

t.penup()
t.goto(-30,0)
t.pendown()

t.color("black")
t.right(90)
for i in range(18):
  t.forward(6)
  t.left(3)

t.penup()
t.goto(0,210)

t.setheading(0)
t.pendown()

for i in range(3):
  t.left(45)
  t.forward(70)
  t.backward(70)

turtle.done()
