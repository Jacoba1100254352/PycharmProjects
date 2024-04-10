import random
import turtle


# setup the screen and the paddle shape
screen = turtle.Screen()
screen.bgcolor("black")
screen.tracer(0)
screen.register_shape("paddle", ((0, 0), (10, 0), (10, 100), (0, 100)))

# draw boundary
boundaryT = turtle.Turtle()
boundaryT.color("white")
boundaryT.speed(0)
boundaryT.penup()
boundaryT.goto(-300, 300)
boundaryT.pensize(2)
boundaryT.pendown()
for i in range(4):
	boundaryT.forward(600)
	boundaryT.right(90)

# player 1
p1 = turtle.Turtle()
p1.speed(0)
p1.shape("paddle")
p1.color("white")
p1.penup()
p1.goto(-290, 0)
p1.setheading(90)

# player 2
p2 = turtle.Turtle()
p2.speed(0)
p2.shape("paddle")
p2.color("white")
p2.penup()
p2.goto(300, 0)
p2.setheading(90)

# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.right(random.randint(-30, 30))  # start off in a random direction

# score
p1Score = 0
p2Score = 0
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player 1: 0  Player 2: 0", align="center", font=("Courier", 24, "normal"))


# movement functions
def p1Up():
	p1.forward(20)


def p1Down():
	p1.backward(20)


def p2Up():
	p2.forward(20)


def p2Down():
	p2.backward(20)


# key binds
screen.onkey(p1Up, "w")
screen.onkey(p1Down, "s")
screen.onkey(p2Up, "Up")
screen.onkey(p2Down, "Down")
screen.listen()


# changeBallDirection(context) is a function that should be provided to the student, or you may help them with the geometry. This function takes in one of four options for the context: p1, p2, topBound, or bottomBound, and changes the ball's heading angle after the bounce.
# There are two versions of changeBallDirection(context) below. The first is the most optimized version of the code that abstracts the changes based on context to the maximimum level. It condenses the multiple steps into a single changeBallDirection(degree). If you choose this one, walk your student through the math required to come up with the degree values.
# The second version in the comments writes out all of the angle changes and changeBallDirection steps. The second one may be easier for students that have less geometry experience, as you can draw out each scenario and walk them through the individual steps required. You can use either one of these functions, either as teaching tools or as-is.

def changeBallDirection(context):
	# finds offset to any plane
	ballHeading = ball.heading()
	
	if context == "topBound" or context == "bottomBound":
		ball.setheading(360 - ballHeading)
	elif 0 <= ballHeading < 180:
		ball.setheading(180 - ballHeading)
	elif 180 <= ballHeading < 360:
		ball.setheading(540 - ballHeading)


'''
def changeBallDirection(context):
  # finds offset to any plane
  ballHeading = ball.heading()
  offset = 0
  if 0 <= ballHeading < 90:
    offset = ballHeading
  elif 90 <= ballHeading < 180:
    offset = 180 - ballHeading
  elif 180 <= ballHeading < 270:
    offset = ballHeading - 180
  elif 270 <= ballHeading <= 360:
    offset = 360 - ballHeading

  # ball is hitting p1's paddle
  if context == "p1":
    # coming from bottom
    if 90 <= ballHeading <= 180:
      ball.setheading(90)
      ball.right(90 - offset)
    # coming from top
    elif 180 <= ballHeading <= 270:
      ball.setheading(270)
      ball.left(90 - offset)

  # ball is hitting p2's paddle
  elif context == "p2":
    # coming from bottom
    if 0 <= ballHeading <= 90:
      ball.setheading(90)
      ball.left(90 - offset)

    # coming from top
    elif 270 <= ballHeading <= 360:
      ball.setheading(270)
      ball.right(90 - offset)

  # ball is hitting the top
  elif context == "topBound":
  # coming from left
    if 0 <= ballHeading <= 90:
      ball.setheading(0)
      ball.right(offset)

    # coming from right
    elif 90 < ballHeading <= 180:
      ball.setheading(180)
      ball.left(offset)

  # ball is hitting the bottom
  elif context == "bottomBound":
    # coming from right
    if 180 <= ballHeading <= 270:
      ball.setheading(180)
      ball.right(offset)
  
    # coming from left
    elif 270 < ballHeading <= 360:
      ball.setheading(0)
      ball.left(offset)
'''

# main game loop
while True:
	ball.forward(4)
	
	# if the ball is within the coordinates of p1 (left side)
	if abs(p1.xcor() - ball.xcor()) < 10 and p1.ycor() <= ball.ycor() <= p1.ycor() + 100:
		changeBallDirection("p1")
	
	# if the ball is within the coordinates of p2 (right side)
	elif abs(ball.xcor() - p2.xcor()) <= 10 and p2.ycor() <= ball.ycor() <= p2.ycor() + 100:
		changeBallDirection("p2")
	
	# ball exceeded boundaries on left; p1 missed the ball
	elif ball.xcor() <= -300:
		# sets heading to face left again so that we do not start off in the wrong angle
		ball.setheading(180)
		ball.right(random.randint(-30, 30))
		ball.goto(0, 0)
		p1.clear()
		p2.clear()
		p2.write("     I Win!")
		p2Score += 1
		pen.clear()
		pen.write("Player 1: " + str(p1Score) + " Player 2: " + str(p2Score), align="center",
		          font=("Courier", 24, "normal"))
	
	# ball exceeded boundaries on right; p2 missed the ball
	elif ball.xcor() >= 300:
		# sets heading to face right again so that we do not start off in the wrong angle
		ball.setheading(0)
		ball.right(random.randint(-30, 30))
		ball.goto(0, 0)
		p1.clear()
		p2.clear()
		p1.write("     I Win!")
		p1Score += 1
		pen.clear()
		pen.write("Player 1: " + str(p1Score) + " Player 2: " + str(p2Score), align="center",
		          font=("Courier", 24, "normal"))
	
	# top boundary
	elif ball.ycor() >= 290:
		changeBallDirection("topBound")
	
	# bottom boundary
	elif ball.ycor() <= -290:
		changeBallDirection("bottomBound")
	
	# end by updating the screen with changes
	screen.update()
