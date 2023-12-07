import turtle

screen = turtle.Screen()
juni = turtle.Turtle()
juni.speed(1029)
juni.goto(0, 0)


def firstCircle():
    juni.penup()
    juni.goto(0, 0)
    juni.pendown()

    for i in range(72):
        juni.forward(9)
        juni.right(5)


def secondCircle():
    juni.penup()
    juni.goto(0, 0)
    juni.pendown()

    for i in range(72):
        juni.forward(6)
        juni.left(5)


def thirdCircle():
    juni.penup()
    juni.goto(0, 228)
    juni.pendown()

    for i in range(72):
        juni.forward(4)
        juni.right(5)


def face():
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


screen.onkey(firstCircle, 's')
screen.onkey(secondCircle, 'n')
screen.onkey(thirdCircle, 'o')
screen.onkey(face, 'w')

screen.listen()
