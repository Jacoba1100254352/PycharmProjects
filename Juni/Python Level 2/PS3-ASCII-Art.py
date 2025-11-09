"""
Write a program that asks for a number and then prints out a grid of # symbols with these dimensions.
"""

size = int(input("Enter the size of the box: "))

for _ in range(size):
	for _ in range(size):
		print("#", end="")
	print()

"""
for _ in range(size):
    print("#"*size)

print(("#"*size+"\n")*size)
"""
