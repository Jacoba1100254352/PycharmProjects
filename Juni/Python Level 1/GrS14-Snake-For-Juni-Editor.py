import turtle
import random
import time

screen = turtle.Screen()
screen.bgcolor("dark green")
# screen.tracer(0)
drawer = turtle.Turtle()
drawer.color("black")
drawer.speed(1000)
drawer.penup()
drawer.goto(-300, 150)
drawer.pendown()
for i in range(2):
    drawer.forward(600)
    drawer.right(90)
    drawer.forward(280)
    drawer.right(90)
drawer.ht()
snakes = []
headSnake = turtle.Turtle()
headSnake.shape("square")
headSnake.color("lawn green")
headSnake.penup()
headSnake.goto(0, 100)
headSnake.speed(3)
headDirection = "stop"
tomato = turtle.Turtle()
tomato.shape("circle")
tomato.color("tomato")
tomato.penup()
tomato.goto(0, 0)


# tomato.speed(0)
def directionUp():
    global headDirection
    if headDirection != "down":
        headDirection = "up"


def directionDown():
    global headDirection
    if headDirection != "up":
        headDirection = "down"


def directionLeft():
    global headDirection
    if headDirection != "right":
        headDirection = "left"


def directionRight():
    global headDirection
    if headDirection != "left":
        headDirection = "right"


screen.onkey(directionUp, "up")
screen.onkey(directionDown, "down")
screen.onkey(directionLeft, "left")
screen.onkey(directionRight, "right")
screen.listen()
score = 0
highscore = 0
drawer.goto(-300, 155)
drawer.color("ghost white")
drawer.write("Score: " + str(score))
drawer.penup()
drawer.goto(-250, 155)
drawer.write("High Score: " + str(highscore))


def move():
    if headDirection == "up":
        y = headSnake.ycor()
        headSnake.sety(y + 20)
    if headDirection == "down":
        y = headSnake.ycor()
        headSnake.sety(y - 20)
    if headDirection == "right":
        x = headSnake.xcor()
        headSnake.setx(x + 20)
    if headDirection == "left":
        x = headSnake.xcor()
        headSnake.setx(x - 20)


while True:
    screen.tracer(0)
    if headSnake.distance(tomato) < 20:
        score += 1
        drawer.clear()
        drawer.goto(-300, 155)
        tomato.goto(random.randint(-300, 300), random.randint(-130, 150))
        bodySnake = turtle.Turtle()
        bodySnake.shape("square")
        bodySnake.color("lawn green")
        bodySnake.penup()
        bodySnake.speed(0)
        snakes.append(bodySnake)
        if score > highscore:
            highscore = score
            drawer.clear()
            drawer.goto(-250, 155)
            drawer.write("High Score: " + str(highscore))
    for i in range(len(snakes) - 1, 0, -1):
        x = snakes[i - 1].xcor()
        y = snakes[i - 1].ycor()
        snakes[i].goto(x, y)
    if len(snakes) > 0:
        snakes[0].goto(headSnake.xcor(), headSnake.ycor())
    screen.update()
    screen.tracer(1)
    move()
    screen.tracer(0)
    headHitBody = False
    for i in range(len(snakes) - 1, 0, -1):
        if headSnake.distance(snakes[i]) < 15:
            snakes = []
            score = 0
            headHitBody = True
    if headSnake.xcor() < -300 or headSnake.xcor() > 300 or headSnake.ycor() < -130 or headSnake.ycor() > 150 or headHitBody:
        snakes = []
        score = 0
        break
    drawer.write("Score: " + str(score))
    screen.update()


# Very Much Simplified code:
"""
import turtle
import random

def set_direction(new_dir):
    if (new_dir, head_direction) not in {("up", "down"), ("down", "up"), ("left", "right"), ("right", "left")}:
        global head_direction
        head_direction = new_dir

def move():
    x, y = head_snake.xcor(), head_snake.ycor()
    head_snake.setpos(x + 20 * (head_direction == "right") - 20 * (head_direction == "left"), y + 20 * (head_direction == "up") - 20 * (head_direction == "down"))

def update_score():
    drawer.clear()
    drawer.write(f"Score: {score} High Score: {highscore}", align="left")

screen = turtle.Screen()
screen.bgcolor("dark green")

drawer = turtle.Turtle()
drawer.color("ghost white")
drawer.hideturtle()
drawer.penup()
drawer.goto(-300, 155)
update_score()

head_snake = turtle.Turtle()
head_snake.shape("square")
head_snake.color("lawn green")
head_snake.penup()
head_snake.goto(0, 100)
head_snake.speed(3)
head_direction = "stop"

tomato = turtle.Turtle()
tomato.shape("circle")
tomato.color("tomato")
tomato.penup()
tomato.goto(0, 0)

screen.onkey(lambda: set_direction("up"), "Up")
screen.onkey(lambda: set_direction("down"), "Down")
screen.onkey(lambda: set_direction("left"), "Left")
screen.onkey(lambda: set_direction("right"), "Right")
screen.listen()

score, highscore, snakes = 0, 0, []

while True:
    screen.tracer(0)
    
    if head_snake.distance(tomato) < 20:
        score += 1
        tomato.goto(random.randint(-300, 300), random.randint(-130, 150))
        body_snake = turtle.Turtle()
        body_snake.shape("square")
        body_snake.color("lawn green")
        body_snake.penup()
        snakes.append(body_snake)
        highscore = max(highscore, score)
        update_score()
    
    for i in range(len(snakes) - 1, 0, -1):
        snakes[i].goto(snakes[i - 1].pos())
    
    if snakes:
        snakes[0].goto(head_snake.pos())
    
    move()
    
    if any(head_snake.distance(snake) < 15 for snake in snakes) or not (-300 < head_snake.xcor() < 300 and -130 < head_snake.ycor() < 150):
        snakes.clear()
        score = 0
        head_snake.goto(0, 100)
        head_direction = "stop"
    
    screen.update()
"""
