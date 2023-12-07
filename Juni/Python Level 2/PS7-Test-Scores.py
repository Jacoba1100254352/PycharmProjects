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
