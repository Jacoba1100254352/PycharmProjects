import random
import turtle


turtle.colormode(255)


def drawSnowflake(numBranches, branchLength, sideBranchLength):
	t = turtle.Turtle()
	t.speed(10000)
	t.penup()
	
	r = random.randint(0, 255)
	g = random.randint(0, 255)
	b = random.randint(0, 255)
	t.color(r, g, b)
	
	x = random.randint(-200, 200)
	y = random.randint(-200, 200)
	
	for i in range(numBranches):
		t.goto(x, y)
		t.pendown()
		
		for i in range(10):
			# draw part of the branch
			t.forward(branchLength / 10)
			
			# draw a little side branch
			t.right(45)
			t.forward(sideBranchLength)
			t.backward(sideBranchLength)
			
			# draw the symmetrical little side branch
			t.left(90)
			t.forward(sideBranchLength)
			t.backward(sideBranchLength)
			
			# reset positioning
			t.right(45)
		
		# turn to start drawing the next branch
		t.right(360 / numBranches)
	
	t.penup()


for i in range(10):
	numBranches = random.randint(5, 20)
	branchLength = random.randint(20, 80)
	sideBranchLength = random.randint(5, 20)
	drawSnowflake(numBranches, branchLength, sideBranchLength)
