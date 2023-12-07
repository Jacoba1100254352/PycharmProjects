import random
import turtle

juni = turtle.Turtle()

x = random.randint(0, 3)

if x == 0:
    for i in range(4):
        juni.forward(50)
        juni.right(90)

elif x == 1:
    for i in range(3):
        juni.forward(50)
        juni.right(120)

else:
    for i in range(36):
        juni.forward(5)
        juni.right(10)
