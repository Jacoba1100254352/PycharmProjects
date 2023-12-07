import turtle

t = turtle.Turtle()
turtle.colormode(255)
# This function draws a circle with size "circleSize"
def drawSnowball(circleSize):
    t.color("black")
    t.setheading(0)
    for i in range(36):
        t.forward(circleSize)
        t.right(10)

# This function draws a hat, where the middle of the bottom of the hat is at coordinates (x, y)
def drawHat(x, y):
    t.color("black")
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.setheading(0)
    t.forward(30)
    t.left(180)
    t.forward(60)
    t.penup()
    t.begin_fill()
    t.goto(x+20, y)
    t.pendown()
    t.right(90)
    t.forward(20)
    t.left(90)
    t.forward(40)
    t.left(90)
    t.forward(20)
    t.left(90)
    t.forward(40)
    t.end_fill()

# This function draws a nose, with size "noseSize" at coordinates (x, y)
def drawCarrotNose(x, y, size):
    t.setheading(0)
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color("orange")
    t.begin_fill()
    for i in range(36):
        t.forward(size)
        t.left(10)
    t.end_fill()

# This function draws an eye, with size "eyeSize" at coordinates (x, y)
def drawCharcoalEye(x, y, size):
    t.setheading(0)
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color("black")
    t.begin_fill()
    for i in range(36):
        t.forward(size)
        t.left(10)
    t.end_fill()

def drawLeftBroomstickArm(x, y, armLength):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color("brown")
    t.setheading(145)
    t.forward(armLength)
    # Draw fingers
    t.right(40)
    for i in range(20):
        t.forward(15)
        t.backward(15)
        t.left(4)

def drawRightBroomstickArm(x, y, armLength):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color("brown")
    t.setheading(35)
    t.forward(armLength)
    # Draw fingers
    t.right(40)
    for i in range(20):
        t.forward(15)
        t.backward(15)
        t.left(4)


# Draw the whole snowman!

# Draw his three snowballs: size 8 at (0,100), size 10 at (0,10), and size 12 at (0,-105)
t.penup()
t.goto(0, 100)
t.pendown()
drawSnowball(8)

t.penup()
t.goto(0, 10)
t.pendown()
drawSnowball(10)

t.penup()
t.goto(0, -105)
t.pendown()
drawSnowball(12)

# Draw nose of size 1 at (0,50)
drawCarrotNose(0, 50, 1)

# Draw eyes of size 0.75 at (-15,65) and (15,65)
drawCharcoalEye(-15, 65, 0.75)
drawCharcoalEye(15, 65, 0.75)

# Draw hat at (0,100)
drawHat(0, 100)

# Draw arms of size 100 at (-25,-25) and (25,-25)
drawLeftBroomstickArm(-25, -25, 100)
drawRightBroomstickArm(25, -25, 100)
