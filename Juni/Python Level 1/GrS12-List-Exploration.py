import turtle


t = turtle.Turtle()

colors = []

colors.append("red")
colors.append("yellow")
colors.append("purple")
colors.append("pink")
colors.append("green")

for color in colors:
	t.color(color)
	t.forward(10)

if "purple" in colors:
	t.write("yes")
else:
	t.write("no")
