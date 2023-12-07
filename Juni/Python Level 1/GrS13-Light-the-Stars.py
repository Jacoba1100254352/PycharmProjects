import random, turtle

# set up player turtle and screen
player = turtle.Turtle()
player.speed(10000)
player.shape("turtle")
player.color("white")
player.penup()

screen = turtle.Screen()

# set up the stars to be lit
stars = []
for _ in range(10):
    star = turtle.Turtle()
    star.speed(10000)
    star.color("white")
    star.penup()
    star.goto(random.randint(-250, 250), random.randint(-250, 250))
    star.shape("circle")
    stars.append(star)


# set up event listeners for controlling the player
def turnLeft():
    player.left(10)

def turnRight():
    player.right(10)

screen.onkey(turnLeft, "Left")
screen.onkey(turnRight, "Right")
screen.listen()


# lightStar() draws a star wherever we light one
def lightStar():
    player.pendown()
    player.color("yellow")
    player.begin_fill()
    for _ in range(5):
        player.forward(30)
        player.right(144)
    player.end_fill()
    player.color("white")
    player.penup()


# main loop
# note: for the sunset:
# startColor = rgb(195, 20, 50)
# endColor = rgb(60, 20, 50)

r = 195
g = 20
b = 50
numStarsLit = 0

while True:
    # move player
    player.forward(1)

    # update background color
    # Will need to introduce how to round r into whole number for our background
    screen.bgcolor(int(r), g, b)
    r -= 0.1

    # check if we have reached sunset
    if r < 30:
        player.write("Time's up! Game over!")
        break

    # check for collision with a star
    for star in stars:
        if abs(player.xcor() - star.xcor()) < 10 and abs(player.ycor() - star.ycor()) < 10:
            lightStar()
            star.goto(500, 500)  # move the star offscreen
            numStarsLit += 1

    # check for win condition
    if numStarsLit == 10:
        player.write("I win!")
        break
