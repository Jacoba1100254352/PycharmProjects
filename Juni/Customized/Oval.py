import math
import turtle


screen = turtle.Screen()
screen.tracer(0)


def ellipse(xlen, ylen, xpos=0, ypos=0, angle=360, angle_unit="d"):
	t = turtle.Turtle()
	t.speed(0)
	
	# We are multiplying by 0.875 because for making a complete ellipse
	# we are plotting 315 pts according to our parametric angle value
	
	converted_angle = angle * 0.875  # Angle in radians
	if angle_unit == "r":
		converted_angle *= 180 / math.pi  # Converting radian to degrees.
	
	for i in range(int(converted_angle) + 1):
		t.up() if i == 0 else t.down()
		t.setposition(xpos + xlen * math.cos(i / 50), ypos + ylen * math.sin(i / 50))


ellipse(200, 20)

screen.update()
turtle.done()
