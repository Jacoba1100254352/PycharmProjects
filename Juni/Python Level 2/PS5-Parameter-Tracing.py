# Read through the following code, and figure out what will print out each time

def function1(a, b, c):
	temp = a + b
	c = temp * a
	return c + b


def function2(c, b, a):
	x = function1(a, b, c)
	return x + b + 3


answer1 = function1(1, 2, 3)
# print(answer1)

answer2 = function1(-2, 4, 1)
# print(answer2)

a = 1
b = 2
c = 3

answer3 = function1(c, b, a)
# print(answer3)

answer4 = function1(a, 2, a)
# print(answer4)

answer5 = function1(c, c, c)
# print(answer5)

answer6 = function2(2, 3, 4)
# print(answer6)

x = 1
answer7 = function2(x + 1, x + 2, x + 3)
# print(answer7)
