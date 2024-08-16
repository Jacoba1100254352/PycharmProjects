import random
import turtle


turtle.colormode(255)

t = turtle.Turtle()
l = []

for i in range(15):
	l.append(random.randint(0, 10))

t.penup()
t.goto(-100, 0)

for num in l:
	t.write(num)
	t.forward(20)

t.goto(-100, -30)

for num in l:
	t.write(num + 10)
	t.forward(20)

t.goto(-100, -60)

for num in l:
	t.write((num + 10) * 10)
	t.forward(20)

'''
If your student is comfortable with lists, you can introduce them to indexing
then they can use this technique to actually change the values inside the list

Discuss with the student when they want to change the values in the list, and when they want to keep them stagnant
'''
