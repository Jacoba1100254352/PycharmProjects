sum = 0
numStudents = 5

minScore = 100
maxScore = 0
sum = 0

for i in range(numStudents):
	score = int(input("Enter student " + str(i + 1) + "'s score: "))
	
	sum += score
	
	if score < minScore:
		minScore = score
	if score > maxScore:
		maxScore = score

average = sum / numStudents
print("The highest score was: " + str(maxScore))
print("The lowest score was: " + str(minScore))
print("The class average was: " + str(average))
