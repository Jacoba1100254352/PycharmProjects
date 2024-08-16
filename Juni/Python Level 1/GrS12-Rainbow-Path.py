import random
import turtle


colors = [
	"white", "white smoke", "gainsboro", "light gray", "silver", "dark gray", "gray", "dim gray", "black",
	"slate gray", "alice blue", "royal blue", "blue", "medium blue", "navy", "dark blue", "midnight blue",
	"light blue", "deep sky blue", "dodger blue", "powder blue", "sky blue", "light sky blue", "steel blue",
	"azure", "light cyan", "cyan", "pale turquoise", "dark turquoise", "turquoise", "cadet blue", "dark cyan",
	"teal", "mint cream", "aquamarine", "dark sea green", "sea green", "honeydew", "pale green", "light green",
	"spring green", "lime green", "green", "forest green", "dark green", "green yellow", "chartreuse", "lawn green",
	"lime", "yellow green", "olive drab", "beige", "dark khaki", "olive", "pale goldenrod", "khaki", "ivory",
	"light yellow", "cornsilk", "lemon chiffon", "yellow", "gold", "goldenrod", "dark goldenrod", "wheat", "tan",
	"burlywood", "peru", "sienna", "saddle brown", "floral white", "old lace", "navajo white", "moccasin",
	"sandy brown", "orange", "dark orange", "chocolate", "firebrick", "brown", "dark red", "maroon", "antique white",
	"papaya whip", "bisque", "peach puff", "light salmon", "coral", "tomato", "orange red", "red", "crimson",
	"dark salmon", "salmon", "light coral", "indian red", "rosy brown", "linen", "seashell", "misty rose", "pink",
	"light pink", "hot pink", "deep pink", "snow", "lavender blush", "violet red", "purple", "dark magenta", "violet",
	"magenta", "thistle", "plum", "orchid", "medium orchid", "dark orchid", "dark violet", "blue violet",
	"medium purple", "rebecca purple", "indigo", "ghost white", "lavender", "slate blue"
]

t = turtle.Turtle()
t.shape("turtle")
t.penup()
t.goto(-200, -200)
t.pendown()
t.setheading(45)

for color in colors:
	t.color(color)
	t.forward(random.randint(3, 7))
	t.right(random.randint(-10, 10))
