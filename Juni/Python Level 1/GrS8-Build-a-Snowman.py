import turtle

juni = turtle.Turtle()
juni.speed(1029)


def drawCircle(size):
    for i in range(72):
        juni.forward(size)
        juni.right(5)


juni.penup()
juni.goto(0, 0)
juni.pendown()
drawCircle(9)

juni.penup()
juni.goto(0, 137)
juni.pendown()
drawCircle(6)

juni.penup()
juni.goto(0, 228)
juni.pendown()
drawCircle(4)

juni.color("black")

juni.penup()
juni.goto(-7, 200)
juni.pendown()

juni.goto(-7, 190)

juni.penup()
juni.goto(7, 200)
juni.pendown()

juni.goto(7, 190)

juni.penup()
juni.goto(-11, 175)
juni.pendown()

juni.right(90)

for i in range(36):
    juni.forward(1)
    juni.left(5)
