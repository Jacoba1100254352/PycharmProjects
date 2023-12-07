import turtle

turtle.colormode(255)

juni = turtle.Turtle()

# Explain what a parameter is. How are they useful?
# 

# Write a function that draws an octogon with any size sideLength

'''
def drawOctogon(sideLength):
  for i in range(8):
    juni.forward(sideLength)
    juni.right(360/8)
'''


# Change your previous function so that you can input the pensize you want the octogon drawn in into your function too

def drawOctogon(sideLength, pensize):
    juni.pensize(pensize)
    for i in range(8):
        juni.forward(sideLength)
        juni.right(360 / 8)


# Call your functions

drawOctogon(40, 3)
