import random
import turtle

turtle.colormode(255)

screen = turtle.Screen()
t = turtle.Turtle()
t.speed(10000)
t.penup()


def turnLeft():
    t.left(20)


def turnRight():
    t.right(20)


def moveForward():
    t.forward(20)


def moveBackward():
    t.backward(20)


def draw():
    t.pendown()
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    t.color(r, g, b)
    t.begin_fill()
    side = random.randint(3, 10)
    for i in range(36):
        t.forward(side)
        t.right(10)
    t.end_fill()
    t.penup()


screen.onkey(turnLeft, "Left")
screen.onkey(turnRight, "Right")
screen.onkey(moveForward, "Up")
screen.onkey(moveBackward, "Down")
screen.onkey(draw, "space")

screen.listen()
