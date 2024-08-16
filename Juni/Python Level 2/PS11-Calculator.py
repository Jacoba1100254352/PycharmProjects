def add(a, b):
	return a + b


def subtract(a, b):
	return a - b


def multiply(a, b):
	return a * b


def divide(a, b):
	return a / b


def modulus(a, b):
	return a % b


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


catalog = {"Addition": '+', "Subtraction": '-', "Multiplication": '*', "Division": '/', "Modulus": '%',
           "Factorial": '!', "Exponent": '^'}

print("Welcome to the Python Calculator. These are the operations we offer:")
for operator in catalog:
	print(operator + ": " + catalog[operator])

while True:
	operator = input("\nPlease enter the operator of the function you would like to use: ")
	
	if operator == '!':
		a = int(input("Number: "))
		print("Result: " + str(factorial(a)))
	else:
		a = int(input("Number 1: "))
		b = int(input("Number 2: "))
		
		if operator == '+':
			print("Result: " + str(add(a, b)))
		elif operator == '-':
			print("Result: " + str(subtract(a, b)))
		elif operator == '*':
			print("Result: " + str(multiply(a, b)))
		elif operator == '/':
			print("Result: " + str(divide(a, b)))
		elif operator == '%':
			print("Result: " + str(modulus(a, b)))
		elif operator == '^':
			print("Result: " + str(exponent(a, b)))
		else:
			print("Invalid Operator")
	
	answer = input("\nWould you like to perform another operation? Enter 'Y' for yes or 'N' for no: ")
	
	if answer == 'N':
		break
