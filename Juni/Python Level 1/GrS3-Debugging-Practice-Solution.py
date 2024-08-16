import turtle


bob = turtle.Turtle()
bob.speed(1000)

bob.penup()
bob.goto(54, 54)
bob.pendown()

# Draw triangle
for i in range(3):
	bob.forward(60)
	bob.left(120)

bob.penup()
bob.goto(-103, 54)
bob.pendown()

# Draw square
for i in range(4):
	bob.forward(84)
	bob.right(90)

bob.penup()
bob.goto(20, -50)
bob.pendown()

# Draw pentagon
for i in range(5):
	bob.forward(67)
	bob.right(72)
