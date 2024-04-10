import random
import turtle


screen = turtle.Screen()

# draw lanes
screen.tracer(0)
box = turtle.Turtle()
box.penup()
box.goto(-200, 200)
box.pendown()

for i in range(20):
	if i % 2 == 0:
		box.color("light cyan")
	else:
		box.color("deep sky blue")
	
	box.begin_fill()
	for j in range(2):
		box.forward(400)
		box.right(90)
		box.forward(20)
		box.right(90)
	box.end_fill()
	
	box.right(90)
	box.forward(20)
	box.left(90)

box.ht()
screen.update()

# create enemies (red turtles)
enemies = []
for i in range(18):
	enemy = turtle.Turtle()
	enemy.shape("turtle")
	enemy.color("coral")
	enemy.penup()
	enemies.append(enemy)

# place enemies on alternating left and right sides
for i in range(len(enemies)):
	if i % 2 == 0:
		enemies[i].goto(random.randint(-180, -100), (190 - 20 * i))
	else:
		enemies[i].goto(random.randint(100, 180), (190 - 20 * i))
		enemies[i].right(180)
screen.update()

# place dots in random positions
dots = []
for i in range(10):
	dot = turtle.Turtle()
	dot.shape("circle")
	dot.color("royal blue")
	dot.penup()
	dots.append(dot)

for i in range(len(dots)):
	dots[i].goto(random.randint(-180, 180), random.randint(-190, 190))
screen.update()

# set up player turtle
player = turtle.Turtle()
player.penup()
player.shape("turtle")
player.left(90)
player.goto(0, -170)


# event listeners to control player turtle
def moveForward():
	player.forward(10)


def moveBackward():
	player.backward(10)


def turnLeft():
	player.left(90)


def turnRight():
	player.right(90)


screen.onkey(moveForward, "Up")
screen.onkey(moveBackward, "Down")
screen.onkey(turnLeft, "Left")
screen.onkey(turnRight, "Right")
screen.listen()

# set up scoreTurtle
score = 0
scoreTurtle = turtle.Turtle()
scoreTurtle.ht()
scoreTurtle.penup()
scoreTurtle.goto(-200, 210)
scoreTurtle.write("Score: 0", font=("Arial", 14, "normal"))
screen.update()

# set up gameOver turtle
gameOver = turtle.Turtle()
gameOver.penup()
gameOver.ht()
gameOver.goto(-150, 0)


# function to make sure turtles stay inbounds
def checkCollision(turtle):
	if turtle.xcor() <= -185 or turtle.xcor() >= 185:
		turtle.right(180)


# main game loop
continueGame = True
while continueGame:
	checkCollision(player)
	
	# make enemy turtles move forward
	for turtle in enemies:
		turtle.forward(random.randint(1, 3))
		checkCollision(turtle)
		
		# if player hits an enemy turtle, end the game
		if abs(player.xcor() - turtle.xcor()) < 10 and abs(player.ycor() - turtle.ycor()) < 10:
			player.ht()
			continueGame = False
	
	# if player eats a dot, move dot to new random location and update the score
	for d in dots:
		if abs(player.xcor() - d.xcor()) < 15 and abs(player.ycor() - d.ycor()) < 15:
			d.goto(random.randint(-180, 180), random.randint(-190, 190))
			score = score + 1
			scoreTurtle.clear()
			scoreTurtle.write("Score: " + str(score), font=("Arial", 20, "normal"))
	screen.update()

gameOver.write("Game Over!", font=("Arial", 40, "normal"))
screen.update()
