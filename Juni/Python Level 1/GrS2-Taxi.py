import turtle

t = turtle.Turtle()
t.pensize(10)
t.speed(10)
 
# rectangle for body 
t.color('yellow')
t.penup()
t.goto(-150,0)
t.pendown()
t.begin_fill()
for i in range(2):
  t.forward(300)
  t.right(90)
  t.forward(60)
  t.right(90)
t.end_fill()

# trapezoid for windows and roof
t.penup()
t.goto(-70,0)
t.pendown()
t.setheading(45)
t.forward(80)
t.right(45)
t.forward(80)
t.right(45)
t.forward(80)

# line to seperate windows
t.setheading(90)
t.penup()
t.goto(50, 10)
t.pendown()
t.forward(40)

# tires
t.penup()
t.goto(-80, -60)
t.pendown()
t.color('black')
t.begin_fill()
for i in range(36):
  t.forward(3)
  t.right(10)
t.end_fill()

t.penup()
t.goto(60, -60)
t.pendown()
t.begin_fill()
for i in range(36):
  t.forward(3)
  t.right(10)
t.end_fill()
 
t.ht()
