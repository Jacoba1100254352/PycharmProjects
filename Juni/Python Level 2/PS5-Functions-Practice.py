def add(x, y):
	return x + y


def subtract(x, y):
	return x - y


def multiply(x, y, z):
	return x * y * z


def average(x, y):
	return (x + y) / 2


def factorial(n):
	answer = 1
	for i in range(1, n + 1):
		answer *= i
	return answer


def exponent(b, p):
	answer = 1
	for i in range(0, p):
		answer *= b
	return answer


print("The sum of 2 and 3 is: " + str(add(2, 3)))
print("The difference of 2 and 3 is: " + str(subtract(2, 3)))
print("The product of 2, 3, and 4 is: " + str(multiply(2, 3, 4)))
print("The average of 2 and 3 is: " + str(average(2, 3)))
print("The factorial of 4 is: " + str(factorial(4)))
print("2 raised to the 3rd power is: " + str(exponent(2, 3)))
