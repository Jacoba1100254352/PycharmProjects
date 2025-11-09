"""
Today is field day, and your class is going to compete against another class in two games: kickball and capture the flag. Your classmates have asked you to write a program that will help them keep track of who is on the kickball team and who is on the capture the flag team. Your program should allow your classmates enter their names one at a time and choose whether they would like to be on the kickball team, the capture the flag team, both, or neither. At the end of the program, it should print out the roster for both teams. For simplicity, assume there are exactly 10 people in your class.
"""

kickball = []
flag = []

for i in range(10):
	name = input("Enter your name: ")
	
	answer = input(
		"Would you like to play kickball, capture the flag, both, or neither?\nEnter '1' for kickball\nEnter '2' for capture the flag\nEnter '3' for both\nEnter '4' for neither\nYour choice: ")
	print()
	
	if answer == '1' or answer == '3':
		kickball.append(name)
	if answer == '2' or answer == '3':
		flag.append(name)

print("Kickball team roster:")
for name in kickball:
	print(name)

print("Capture the flag roster:")
for name in flag:
	print(name)
