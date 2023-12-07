import random
import turtle

t = turtle.Turtle()

t.penup()
t.goto(random.randint(-200, 200), random.randint(-200, 200))
t.pendown()

if t.xcor() >= 0 and t.ycor() >= 0:
    t.color("blue")
if t.xcor() <= 0 and t.ycor() >= 0:
    t.color("yellow")
if t.xcor() >= 0 and t.ycor() <= 0:
    t.color("orange")
if t.xcor() <= 0 and t.ycor() <= 0:
    t.color("green")

if t.xcor() >= 0 or t.ycor() >= 0:
    for i in range(4):
        t.forward(20)
        t.right(90)
if t.xcor() >= 0 and t.ycor() <= 0:
    for i in range(36):
        t.forward(2)
        t.right(10)
