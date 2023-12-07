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
