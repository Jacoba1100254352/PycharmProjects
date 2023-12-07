import random
import turtle

turtle.colormode(255)

t = turtle.Turtle()
t.speed(1000)

# to make the starting direction for each petal easier to implement, we create a variable degreesToTurn that goes 0, 60, 120, 180 etc. thus, after we goto(0,0), we always point toward the right and then turn by this amount
degreesToTurn = 0

for i in range(6):
    t.penup()
    t.goto(0, 0)
    t.setheading(0)
    t.right(degreesToTurn)
    t.pendown()

    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = 0

    angle = 0

    for j in range(40):
        t.color(r, g, b)
        t.forward(10)
        t.right(angle)

        angle = angle + 1
        b = b + 5

    degreesToTurn += 60
