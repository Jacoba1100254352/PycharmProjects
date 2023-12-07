import turtle

t = turtle.Turtle()
t.speed(0)
t.penup()
t.goto(-200, 0)
t.pendown()

t.left(70)
for i in range(30):
    t.forward(20)
    t.right(140)
    t.forward(20)
    t.left(140)

"""
# Bonus extension for advanced students
t.right(70)
for i in range(4):
  t.forward(100)
  t.right(90)

t.penup()
t.goto(-200, 0)
t.pendown()
t.right(60)
for i in range(3):
  t.forward(100)
  t.right(120)
"""
