import turtle
import random

screen = turtle.Screen()
screen.bgcolor("black")

# draw Earth
earth = turtle.Turtle()
earth.speed(10000)
earth.penup()
earth.goto(-200, 0)
earth.color("deep sky blue")
earth.pendown()
earth.begin_fill()
for _ in range(36):
    earth.forward(10)
    earth.right(10)
earth.end_fill()
earth.ht()

# draw moon
moon = turtle.Turtle()
moon.speed(10000)
moon.penup()
moon.goto(200, -25)
moon.color("light slate gray")
moon.pendown()
moon.begin_fill()
for _ in range(36):
    moon.forward(5)
    moon.right(10)
moon.end_fill()
moon.ht()

# create list of turtles
turtles = []
for _ in range(10):
    turtle = turtle.Turtle()
    turtles.append(turtle)

# launch turtles
for turtle in turtles:
    turtle.color("red")
    turtle.shape("turtle")
    turtle.speed(10000)
    turtle.penup()
    turtle.goto(-200, -50)
    turtle.speed(10)
    travelDist = random.randint(200, 500)
    turtle.forward(travelDist)
    if travelDist > 400:
        turtle.color("white")
