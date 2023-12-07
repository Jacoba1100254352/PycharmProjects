import turtle

turtle.colormode(255)

t = turtle.Turtle()
t.speed(50)
t.penup()

distance = 25
numRows = 5
numCols = 8

for i in range(numRows):
    for j in range(numCols):
        t.dot()
        t.forward(distance)
    t.backward(distance * numCols)
    t.right(90)
    t.forward(distance)
    t.left(90)
t.ht()
