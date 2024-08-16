import turtle
import random


listOfTurtles = []

# Add 25 red turtles to the list
for i in range(25):
	t = turtle.Turtle()
	t.color("red")
	t.speed(10000)
	listOfTurtles.append(t)

# Turn each turtle a random number of degrees
for t in listOfTurtles:
	degrees = random.randint(0, 360)
	t.right(degrees)

# Move each turtle forward a different random amount between 0 and 100 pixels
for turtle in listOfTurtles:
	distance = random.randint(0, 100)
	turtle.forward(distance)

# Make each turtle a different random color
for t in listOfTurtles:
	r = random.randint(0, 255)
	g = random.randint(0, 255)
	b = random.randint(0, 255)
	t.color(r, g, b)
