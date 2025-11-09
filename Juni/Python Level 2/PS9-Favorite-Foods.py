"""
Get to know your instructor better! Both you (the student) and the instructor will enter five of your favorite foods. Then, your program should print out which favorite foods you both share. Be careful with spelling though - if you spell the same food differently, then the computer will think you mean different things!

Challenge: Also have your program print out which foods only you like, and which foods only your instructor likes.
"""

studentFoods = set()
instructorFoods = set()

print("Student, enter five of your favorite foods.")
for i in range(5):
	studentFoods.add(input("Food " + str(i + 1) + ": "))

print("Instructor, enter five of your favorite foods.")
for i in range(5):
	instructorFoods.add(input("Food " + str(i + 1) + ": "))

shared = studentFoods.intersection(instructorFoods)

if len(shared) == 0:
	print("You like completely different foods!")
else:
	print("You both share these top foods: " + str(shared))

# Challenge
print("Here are the foods that only the student likes:")
for food in studentFoods:
	if food not in instructorFoods:
		print(food)

print("Here are the foods that only the instructor likes:")
for food in instructorFoods:
	if not food in studentFoods:
		print(food)
