import turtle
t = turtle.Turtle()
t.speed(10000)

t.penup()
t.goto(0,100)
t.pendown()
t.right(5)        # This allows the target to appear centered

t.color('red')
t.begin_fill()
for i in range(36):
  t.forward(20)
  t.right(10)
t.end_fill()

t.penup()
t.goto(0,77)      # Moving down by 23 contributes to making the rings appear more concentric
t.pendown()

t.color('white')
t.begin_fill()
for i in range(36):
  t.forward(16)
  t.right(10)
t.end_fill()

t.penup()
t.goto(0,54)
t.pendown()

t.color('red')
t.begin_fill()
for i in range(36):
  t.forward(12)
  t.right(10)
t.end_fill()

t.penup()
t.goto(0,31)
t.pendown()

t.color('white')
t.begin_fill()
for i in range(36):
  t.forward(8)
  t.right(10)
t.end_fill()

t.penup()
t.goto(0,8)
t.pendown()

t.color('red')
t.begin_fill()
for i in range(36):
  t.forward(4)
  t.right(10)
t.end_fill()