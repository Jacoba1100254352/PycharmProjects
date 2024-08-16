import turtle


t = turtle.Turtle()
screen = turtle.Screen()

# draw the boundary box
boxDrawer = turtle.Turtle()
boxDrawer.speed(10)
boxDrawer.color("red")
boxDrawer.penup()
boxDrawer.goto(-200, 200)
boxDrawer.pendown()
for i in range(4):
	boxDrawer.forward(400)
	boxDrawer.right(90)
boxDrawer.penup()


# create functions for keyboard events
def turnLeft():
	t.left(10)


def turnRight():
	t.right(10)


# bind keyboard events to screen
screen.onkey(turnLeft, "Left")
screen.onkey(turnRight, "Right")
screen.listen()

# write score
score = 0
scoreTurtle = turtle.Turtle()
scoreTurtle.speed(1000)
scoreTurtle.penup()
scoreTurtle.goto(-200, 210)
scoreTurtle.write("Score: " + str(score))

# main loop - turtle continuously moves and checks if out of bounds
t.color("black")
t.goto(0, 0)
t.pendown()
while True:
	t.forward(5)
	
	# check if turtle is out of bounds
	if t.xcor() > 200 or t.xcor() < -200 or t.ycor() > 200 or t.ycor() < -200:
		t.write("Out of bounds!")
		break
	else:
		# update score
		score += 1
		scoreTurtle.clear()
		scoreTurtle.write("Score: " + str(score))

'''
alternative while loop solution, for advanced students:

while not (t.xcor() > 200 or t.xcor() < -200 or t.ycor() > 200 or t.ycor() < -200):
  t.forward(5)
  score += 1
  scoreTurtle.clear()
  scoreTurtle.write("Score: " + str(score))
'''
