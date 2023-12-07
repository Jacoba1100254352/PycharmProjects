import random
import turtle

# draw the boundary box
boxDrawer = turtle.Turtle()
boxDrawer.speed(10)
boxDrawer.penup()
boxDrawer.goto(-200, 200)
boxDrawer.pendown()
for i in range(4):
    boxDrawer.forward(400)
    boxDrawer.right(90)
boxDrawer.ht()

balls = []
for i in range(10):
    t = turtle.Turtle()
    t.penup()
    t.speed(1000)
    t.color("red")
    t.shape("circle")
    t.goto(random.randint(-200, 200), random.randint(-200, 200))
    t.right(random.randint(0, 360))
    balls.append(t)


def checkCollision(ball):
    if ball.xcor() > 200 or ball.xcor() < -200:
        ball.right(180)
    elif ball.ycor() > 200 or ball.ycor() < -200:
        ball.right(180)


while True:
    for ball in balls:
        checkCollision(ball)
        ball.forward(10)
