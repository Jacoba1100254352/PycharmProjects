biology = ["Sarah", "Ahmed", "Fred", "Gillian", "Shradah", "Max", "Max", "Sara", "Max", "Esther"]

computerScience = ["Sarah", "John", "Fred", "Gillian", "Jermaine", "Max", "Sara", "Juan", "Esther"]

english = ["Nico", "Sharjeel", "Isabella", "Taylor", "Ali", "Ali", "Jean-Baptiste", "Jean-Baptiste", "Jean-Baptiste",
           "William"]


def generateWaitlist(students):
	enrolled = set()
	waitlist = set()
	for name in students:
		if len(enrolled) < 6:
			enrolled.add(name)
		elif name not in enrolled:
			waitlist.add(name)
	return waitlist


print("Waitlisted for Biology: " + str(generateWaitlist(biology)))
print("Waitlisted for Computer Science: " + str(generateWaitlist(computerScience)))
print("Waitlisted for English: " + str(generateWaitlist(english)))
