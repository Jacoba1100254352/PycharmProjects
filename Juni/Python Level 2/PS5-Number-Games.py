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
