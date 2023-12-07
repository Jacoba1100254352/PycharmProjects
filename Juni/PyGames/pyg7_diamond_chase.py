import random
import sys

import pgzrun

mod = sys.modules['__main__']

WIDTH = 520
HEIGHT = 520

alien = mod.Actor("ufo", (WIDTH / 2, HEIGHT / 2))
gem1 = mod.Actor("diamond_s", (100, 100))
gem2 = mod.Actor("diamond_s", (400, 400))

gems = [gem1, gem2]

points = 0

# timer
timer = 30

# game state
gameState = "start"


def draw():
    mod.screen.clear()

    if gameState == "play":
        alien.draw()
        gem1.draw()
        gem2.draw()

        mod.screen.draw.text("Points: " + str(points), center=(50, 30), fontsize=30, color=(255, 255, 255))
        mod.screen.draw.text("Timer: " + str(timer), center=(50, 50), fontsize=30, color=(255, 255, 255))
    elif gameState == "end":
        mod.screen.draw.text("Game Over! \n Press space to play again!", center=(WIDTH / 2, HEIGHT / 2), fontsize=50,
                             color=(255, 255, 255))
    else:
        mod.screen.draw.text("Press space to play!", center=(WIDTH / 2, HEIGHT / 2), fontsize=50, color=(255, 255, 255))


def moveAlien():
    if mod.keyboard.up and alien.y > 20:
        alien.y -= 10

    if mod.keyboard.down and alien.y < 480:
        alien.y += 10

    if mod.keyboard.left and alien.x > 30:
        alien.x -= 10

    if mod.keyboard.right and alien.x < 470:
        alien.x += 10


def checkCollision():
    global points

    for g in gems:
        if alien.colliderect(g):
            g.x = random.randint(50, 450)
            g.y = random.randint(50, 450)
            points += 1


def decreaseTimer():
    global timer
    timer -= 1


def update():
    global gameState, points, timer

    if gameState == "start" or gameState == "end":
        if mod.keyboard.SPACE:
            points = 0
            timer = 30
            gameState = "play"
            mod.clock.schedule_interval(decreaseTimer, 1.0)

        if mod.keyboard.ESCAPE:
            quit()

    else:
        moveAlien()
        checkCollision()

        if timer <= 0:
            gameState = "end"
            mod.clock.unschedule(decreaseTimer)


pgzrun.go()
