import turtle

turtle.colormode(255)

juni = turtle.Turtle()
juni.speed(0)


def drawHouse():
    juni.fillcolor("red")
    juni.begin_fill()
    for i in range(3):
        juni.forward(50)
        juni.left(120)
    juni.end_fill()

    juni.forward(5)

    juni.fillcolor("grey")
    juni.begin_fill()
    for i in range(4):
        juni.forward(40)
        juni.right(90)
    juni.end_fill()


drawHouse()

juni.penup()
juni.goto(-100, 100)
juni.pendown()

drawHouse()

juni.penup()
juni.goto(100, 100)
juni.pendown()

drawHouse()

juni.penup()
juni.goto(100, -100)
juni.pendown()

drawHouse()

juni.penup()
juni.goto(-100, -100)
juni.pendown()

drawHouse()
