# Your friend, Kant D. Bugg, needs your help once more! Please again help Kant find the bugs in his code by using the console and fix them! Your code should not only run, but work as intended (read the comments Kant wrote about what each section of code should do).

import turtle


listOfTurtles = []

# Add 25 red turtles to the list
for i in range(25):
	t = turtle.Turtle()
	t.color("red")
	t.speed(10000)
	listOfTurtles.append(t)

# Turn each turtle a random number of degrees
degrees = random.randint(0 - 360)
listOfTurtles.right(degrees)

# Move each turtle forward a different random amount between 0 and 100 pixels
distance = random.randint(0, 100)
for turtle in listOfTurtles
	turtle.forward(distance)

# Make each turtle a different random color
r = random.randint(0, 255)
g = random.randint(0, 255)
b = random.randint(0, 255)
for turtle in listOfTurtles:
	t.color(r, g, b)
