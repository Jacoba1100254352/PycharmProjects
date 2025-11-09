"""
Write a program that prints the numbers 1 through 50. However, the program should print "Fizz" instead of the number if the number is a multiple of 3, and "Buzz" if the number is a multiple of 5. If it is a multiple of 3 and 5, the program should print "FizzBuzz."
"""

for i in range(1, 51):
	if i % 15 == 0:
		print("FizzBuzz")
	elif i % 3 == 0:
		print("Fizz")
	elif i % 5 == 0:
		print("Buzz")
	else:
		print(i)

# print("\n".join(["FizzBuzz" if i % 15 == 0 else "Fizz" if i % 3 == 0 else "Buzz" if i % 5 == 0 else str(i) for i in range(1, 51)]))
