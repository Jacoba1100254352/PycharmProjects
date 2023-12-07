import turtle

# DO NOT EDIT THIS CODE

graphDrawer = turtle.Turtle()
graphDrawer.speed(0)

graphDrawer.penup()
graphDrawer.goto(-500, 0)
graphDrawer.pendown()
graphDrawer.goto(500, 0)
graphDrawer.penup()
graphDrawer.goto(0, -500)
graphDrawer.pendown()
graphDrawer.goto(0, 500)

graphDrawer.penup()
graphDrawer.goto(50, 100)
graphDrawer.write("Quadrant I", font=("Arial", 16, "normal"))
graphDrawer.goto(-150, 100)
graphDrawer.write("Quadrant II", font=("Arial", 16, "normal"))
graphDrawer.goto(-150, -100)
graphDrawer.write("Quadrant III", font=("Arial", 16, "normal"))
graphDrawer.goto(50, -100)
graphDrawer.write("Quadrant IV", font=("Arial", 16, "normal"))
graphDrawer.goto(10, -150)
graphDrawer.write("y-axis", font=("Arial", 12, "normal"))
graphDrawer.goto(-120, 10)
graphDrawer.write("x-axis", font=("Arial", 12, "normal"))

graphDrawer.ht()

# START CODING BELOW THIS LINE

# make a turtle and move it from the origin (where the two lines meet and our turtle starts) to somewhere in Quadrant I using goto()

# Next, move your turtle to Qudrant II. Did our X or Y coordinate change into a negative number?

# Now move your turtle to Quadrant III. Again, which of our coordinates changed from a positive to a negative?


# Finally, have your turtle move to Quadrant IV. Which of our coordinates changed its sign this time?

# Are positive X coordinates to the left or the right of the y-axis? What about negative coordinates?
#

# Are positive Y coordinates below or above the x-axis? What about negative coordinates?
#

# Tell your turtle to go to (50, 0). What axis is your turtle sitting on after it moves?
#

# Next, tell your turtle to go to (0, 50). What axis is your turtle sitting on after it moves?
#

# Which quadrant will your turtle be in if it goes to the coordinates (-100, -100)?
#

# Which quadrant will your turtle be in if it goes to the coordinates (-200, 50)?
#

# Which quadrant will your turtle be in if it goes to the coordinates (30, 20)?
#

# Which quadrant will your turtle be in if it goes to the coordinates (30, -200)?
#
