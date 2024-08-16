#########################################

# LOOPS WITH VARIABLES

#########################################

# Turtle Setup: First, have the student write out their import statements and create a turtle named zebra.

import turtle


turtle.colormode(255)
zebra = turtle.Turtle()
zebra.speed(0)

# Write a loop that repeats 10 times and a variable sideLength which is set to 10. Each time in the loop, zebra should move forward by sidelength, turn 90 degrees, and increment sideLength by 5.

sideLength = 10
for i in range(10):
	zebra.forward(sideLength)
	zebra.left(90)
	sideLength += 5

# Change your loop so that sideLength does not change if it is 30px or longer.

sideLength = 10
for i in range(10):
	zebra.forward(sideLength)
	zebra.left(90)
	if sideLength < 30:
		sideLength += 5

# Change your loop from a for loop to a while loop while maintaining the same output. When should we use for loops and when should we use while loops when coding?

sideLength = 10
counter = 0
while counter < 10:
	zebra.forward(sideLength)
	zebra.left(90)
	counter += 1
	if sideLength < 30:
		sideLength += 5


#########################################

# FUNCTIONS

#########################################

# What are functions? If we create a function to help us draw a specific shape, what advantages does it give us over just using a for loop to create a shape? When are functions useful?

# Define a function called moveForward50() which moves zebra forward by 50 pixels.

def moveForward50():
	zebra.forward(50)


# Call your function.

moveForward50()


# What are parameters and why are they useful?

# Define a function called drawSquare(sideLength) which takes in the square's side length as input. Call this function with an input of 40.

def drawSquare(sideLength):
	for i in range(4):
		zebra.right(90)
		zebra.forward(sideLength)


drawSquare(40)

#########################################

# EVENT LISTENERS

#########################################

# What is an event listener? What functionality do they help us add to our programs?

# Create the screen variable we need for our event listeners.

screen = turtle.Screen()

# Program an event listener that moves the turtle 50 pixels forward each time the right arrow key is pressed. Hint: You can use one of the functions we created earlier.

screen.onkey(moveForward50, "Right")


# Program an event listener that draws a triangle each time the up arrow key is pressed. Then, add a line of code that also draws a triangle each time the "A" key is pressed.

def drawTriangle():
	for i in range(3):
		zebra.left(120)
		zebra.forward(50)


screen.onkey(drawTriangle, "Up")
screen.onkey(drawTriangle, "a")

# If the student has not already added this to their program, what is the last line of code we have to add to make sure that these event listeners actually function?

screen.listen()
