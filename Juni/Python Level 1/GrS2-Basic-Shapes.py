import turtle

t = turtle.Turtle()

t.pendown()
t.color('blue')
for i in range(4):
    t.forward(100)
    t.right(90)
t.penup()

t.goto(-150, 150)
t.pendown()
t.color('red')
for i in range(3):
    t.forward(100)
    t.right(120)
t.penup()

t.goto(-150, -100)
t.pendown()
t.color('green')
for i in range(36):
    t.forward(10)
    t.right(10)
