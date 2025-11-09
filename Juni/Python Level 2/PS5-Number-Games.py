"""
Note that in the problems below, although a function may be described as functionName(), it may still need one or more inputs. It's up to you to define the function with the correct input(s)!
Write a function isEven() that returns True if the input number is even and False if the input number is odd. Use this function to print all of the even numbers between 1 and 50.
Write a function isOdd() that returns True if the input number is odd and False if the input number is even. Use this function to print all of the odd numbers between 1 and 50.
Write a function isOdd2() that only uses the isEven() function in its implementation. Use this function to print all of the odd numbers between 1 and 50.
Write a function isMultiple7() that returns True if the input number is a multiple of 7 and False otherwise. Use this function to print all of the multiples of 7 between 1 and 50.
Write a function isMultiple14() that returns True if the input number is a multiple of 14 and False otherwise. Use this function to print all of the multiples of 14 between 1 and 50.
Write a function isMultiple14v2() that only uses the isEven() and isMultiple7 functions in its implementation. Use this function to print all of the multiples of 14 numbers between 1 and 50.
Challenge: Write a function isPrime() that returns True if the input number is a prime number and False otherwise. Use this function to print all of the prime numbers between 1 and 50.
"""


def isEven(n):
	return n % 2 == 0


print("The even numbers between 1 and 50 are...")
for i in range(1, 51):
	if isEven(i):
		print(i)
print()


##########

def isOdd(n):
	return n % 2 != 0


print("The odd numbers between 1 and 50 are...")
for i in range(1, 51):
	if isOdd(i):
		print(i)
print()


##########

def isOdd2(n):
	return not isEven(n)


print("The odd numbers between 1 and 50 are...")
for i in range(1, 51):
	if isOdd2(i):
		print(i)
print()


##########

def isMultiple7(n):
	return n % 7 == 0


print("The multiples of 7 between 1 and 50 are...")
for i in range(1, 51):
	if isMultiple7(i):
		print(i)
print()


##########

def isMultiple14(n):
	return n % 14 == 0


print("The multiples of 14 between 1 and 50 are...")
for i in range(1, 51):
	if isMultiple14(i):
		print(i)
print()


##########

def isMultiple14v2(n):
	return isEven(n) and isMultiple7(n)


print("The multiples of 14 between 1 and 50 are...")
for i in range(1, 51):
	if isMultiple14v2(i):
		print(i)
print()


##########

def isPrime(n):
	if n == 1:
		return False
	for i in range(2, n):
		if n % i == 0:
			return False
	return True


print("The prime numbers between 1 and 50 are...")
for i in range(1, 51):
	if isPrime(i):
		print(i)
print()
