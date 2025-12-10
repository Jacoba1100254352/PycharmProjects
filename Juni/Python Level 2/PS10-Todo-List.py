"""
Program a To-do List program, as shown in the graphic below! Write out pseudocode in your code comments to plan out the program flow and data structures you'll need to set up.
"""

print("Welcome to your todo list!\n")
tasks = []

while True:
	inputNum = input(
		"What would you like to do with your todo list? \n 1. Add a task \n 2. Remove a task \n 3. Exit \nType in the number here: ")
	
	print("")
	if inputNum == "1":
		task = input("Please type in the task you'd like to add: ")
		tasks.append(task)
	elif inputNum == "2":
		removeNum = input("Please type in the number of the task you'd like to remove: ")
		tasks.remove(tasks[int(removeNum) - 1])
	elif inputNum == "3":
		break
	
	# print todo list
	print()
	print("Here's your updated list: ")
	for i in range(0, len(tasks)):
		print(str(i + 1) + ". " + tasks[i])
	print()
