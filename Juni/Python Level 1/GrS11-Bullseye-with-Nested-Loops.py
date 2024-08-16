import turtle


t = turtle.Turtle()
t.speed(10000)
t.right(5)

y = 100
circleStep = 20

for i in range(5):
	t.penup()
	t.goto(0, y)
	t.pendown()
	
	# decide which color
	if (i % 2 == 0):
		t.color('red')
	else:
		t.color('white')
	
	# draw circle
	t.begin_fill()
	for i in range(36):
		t.forward(circleStep)
		t.right(10)
	t.end_fill()
	
	# decrease y and circleStep
	y -= 23
	circleStep -= 4
