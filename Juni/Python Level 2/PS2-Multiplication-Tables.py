"""
The ultimate test of whether you truly know your multiplication tables: write a program to print the whole thing out! Use nested loops to print out all the possible combinations to multiply the numbers between 1 and 12 together, following the graphic below.
"""

for i in range(1, 13):
	for j in range(1, 13):
		print(str(i) + " x " + str(j) + " = " + str(i * j))
