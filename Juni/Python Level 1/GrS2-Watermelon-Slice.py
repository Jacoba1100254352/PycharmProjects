import turtle
t = turtle.Turtle()
t.speed(10000)

# draw the outer green layer
t.penup()
t.goto(-200,0)
t.pendown()
t.color("green")
t.begin_fill()
t.forward(400)
t.right(90)

for i in range(37):
  t.forward(17.5)
  t.right(5)

t.end_fill()

# draw the inner pink layer
t.penup()
t.right(85)
t.forward(50)
t.pendown()
t.color("pink")
t.begin_fill()
t.forward(300)
t.right(90)

for i in range(37):
  t.forward(13)
  t.right(5)

t.end_fill()

# draw seeds

t.penup()
t.goto(80,-40)
t.pendown()
t.color("black")
t.begin_fill()

for i in range(36):
  t.forward(1)
  t.right(10)
t.end_fill()

t.penup()
t.goto(-10,-100)
t.pendown()
t.color("black")
t.begin_fill()

for i in range(36):
  t.forward(1)
  t.right(10)
t.end_fill()

t.penup()
t.goto(-90,-30)
t.pendown()
t.color("black")
t.begin_fill()

for i in range(36):
  t.forward(1)
  t.right(10)
t.end_fill()