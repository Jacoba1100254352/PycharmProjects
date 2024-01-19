import sys

import pgzrun

mod = sys.modules['__main__']

WIDTH, HEIGHT = 750, 240

runner = mod.Actor('runner-1', midleft=(0, 120))


def draw():
    mod.screen.fill((255, 255, 255))
    runner.draw()


def on_key_down(key):
    # check if the left or right key was pressed
    if key == mod.keys.LEFT or key == mod.keys.RIGHT:
        # move the runner to the right.
        runner.x += 15
        # swap the image
        if runner.image == 'runner-1':
            runner.image = 'runner-2'
        else:
            runner.image = 'runner-1'


def update():
    if runner.right >= WIDTH:
        runner.left = 0


pgzrun.go()
