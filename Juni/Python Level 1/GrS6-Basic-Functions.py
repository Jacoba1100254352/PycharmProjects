import random
import turtle

turtle.colormode(255)

t = turtle.Turtle()
t.pensize(5)


def randomSpot():
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    t.penup()
    t.goto(x, y)
    t.pendown()


def randomColor():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    t.color(r, g, b)


def reset():
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.color('black')
    t.setheading(0)
    t.clear()
    t.speed(6)


def allRandom():
    randomSpot()
    randomColor()


randomColor()
randomSpot()
t.right(90)
t.forward(100)
reset()
