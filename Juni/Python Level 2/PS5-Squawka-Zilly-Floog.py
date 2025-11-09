"""
Your friend, a mathematician, needs your help solving some complex math problems. She needs you to write some functions (the computer science kind) to calculate the results of several mathematical functions. The functions should compute the result and return it. Please program the following functions.
zilly(x) should take in a number x and return the value of 2*x+1
floog(x) should take in a number x and return the value of x*x - 6*x + 12
squawka(x) should take in a number and return the value of 2*zilly(x) + 3*floog(x)
"""


def zilly(x):
	return 2 * x + 1


def floog(x):
	return x * x - 6 * x + 12


def squawka(x):
	return 2 * zilly(x) + 3 * floog(x)


print(zilly(4))
print(floog(4))
print(squawka(4))
