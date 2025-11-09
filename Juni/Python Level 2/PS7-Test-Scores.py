"""
Your AP Computer Science A teacher would like to be able to store each of her student's test scores and average them. Write a program that firsts asks for the number of students and the number of tests they each took. Then, ask the user to enter in the test scores, storing each score in dictionary where the keys are the names of the students and the values are their lists of test scores. Print out both this dictionary and another dictionary that maps each student with their average test score.
"""

numStudents = int(input("Enter the number of students: "))
numTests = int(input("Enter the number of tests each student took: "))

testScores = {}

# ask the user to enter each student's name
for i in range(numStudents):
	name = input("Enter student " + str(1 + i) + "'s name: ")
	testScores[name] = []

# ask the user to enter each test score
for i in range(numTests):
	for name in testScores:
		score = int(input("Enter " + name + "'s score on test " + str(i + 1) + ": "))
		testScores[name].append(score)

print(testScores)

# calculate each student's average exam score
averages = {}
for name in testScores:
	sum = 0
	for score in testScores[name]:
		sum += score
	averages[name] = sum / len(testScores[name])

print(averages)
