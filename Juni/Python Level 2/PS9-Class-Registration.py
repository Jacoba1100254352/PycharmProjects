biology = ["Sarah", "Ahmed", "Fred", "Gillian", "Shradah", "Max", "Max", "Sara", "Max", "Esther"]

computerScience = ["Sarah", "John", "Fred", "Gillian", "Jermaine", "Max", "Sara", "Juan", "Esther"]

english = ["Nico", "Sharjeel", "Isabella", "Taylor", "Ali", "Ali", "Jean-Baptiste", "Jean-Baptiste", "Jean-Baptiste",
           "William"]

# alternate Pythonic way: biologyStudents = set(biology)
biologyStudents = set()
for name in biology:
    biologyStudents.add(name)

print("Biology actually has " + str(len(biologyStudents)) + " students enrolled.")

computerScienceStudents = set()
for name in computerScience:
    computerScienceStudents.add(name)

print("Computer Science actually has " + str(len(computerScienceStudents)) + " students enrolled.")

englishStudents = set()
for name in english:
    englishStudents.add(name)

print("English actually has " + str(len(englishStudents)) + " students enrolled.")

# Optional: Write a function getStudents(students) that takes in the list of students and returns the set of students.
