# Inspired by http://www.grantjenks.com/docs/freegames/index.html#fidget

import turtle

# setup drawing turtle and screen
t = turtle.Turtle()
t.ht()
t.width(20)
t.speed(0)

screen = turtle.Screen()
screen.tracer(0)

# global variable for turn speed
turnSpeed = 0


# flick() increases the turn speed
def flick():
    global turnSpeed
    turnSpeed += 10


# slow() decreases the turn speed
def slow():
    global turnSpeed
    if turnSpeed > 0:
        turnSpeed -= 10


# setup key listeners
screen.onkey(flick, 'space')
screen.onkey(slow, 'Down')
screen.listen()

# setup turnSpeed writer
writer = turtle.Turtle()
writer.ht()
writer.penup()
writer.goto(200, 200)

# main loop
while True:
    # clear our previous drawings
    t.clear()

    # get the angle that we will have to change by and rotate
    angle = turnSpeed / 10
    t.right(angle)

    # draw the red circle side
    t.color('black')
    t.forward(100)
    t.color('red')
    t.begin_fill()
    t.left(90)
    for i in range(36):
        t.forward(8)
        t.right(10)
    t.right(90)
    t.end_fill()
    t.color('black')
    t.backward(100)
    t.right(120)

    # draw the green circle side
    t.color('black')
    t.forward(100)
    t.color('green')
    t.begin_fill()
    t.left(90)
    for i in range(36):
        t.forward(8)
        t.right(10)
    t.right(90)
    t.end_fill()
    t.color('black')
    t.backward(100)
    t.right(120)

    # draw the blue circle side
    t.color('black')
    t.forward(100)
    t.color('blue')
    t.begin_fill()
    t.left(90)
    for i in range(36):
        t.forward(8)
        t.right(10)
    t.right(90)
    t.end_fill()
    t.color('black')
    t.backward(100)
    t.right(120)

    # write turnSpeed
    writer.clear()
    writer.write("Turn Speed: " + str(turnSpeed))

    screen.update()
