import turtle

turtle.colormode(255)

t = turtle.Turtle()
t.color('white')
t.speed(100)

s = turtle.Screen()
s.bgcolor('black')

n = 50

for i in range(300):
    t.forward(n)
    t.right(91)
    n = n + 1
