"""
Use a nested for loop to print out each of the blocks of numbers shown in the graphic below!

Note: To print something without a newline at the end in Python, use print("Hello", end="").
"""

import time


# Part I
for i in range(5):
	for j in range(5):
		print(j + 1, end='')
	print()

print()
time.sleep(1)

# Part II
for i in range(5):
	for j in range(5):
		print(5 - j, end='')
	print()

print()
time.sleep(1)

# Part III
for i in range(5):
	for j in range(5):
		print(j + i + 1, end='')
	print()

print()
time.sleep(1)

# Part IV
for i in range(5):
	for j in range(i + 1):
		print(j + 1, end='')
	print()

print()
time.sleep(1)

# Part V
for i in range(5):
	for j in range(5 - i):
		print(j + 1, end='')
	print()
