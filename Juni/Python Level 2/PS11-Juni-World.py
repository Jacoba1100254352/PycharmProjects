ridesDict = {
	'Tower of Turtles': 90,
	'String Mountain': 130,
	'Debug Track': 5,
	'Concatenation Carousel': 100,
	'Cinderella Casting': 90,
	'Magic For Loop': 10,
	'Pythons of the Carribean': 30
}

minutesRemaining = 360
visitedRides = []


# prints time rmeaining in hours and minutes
def printAsHours(time):
	numHours = int(time / 60)
	numMins = time % 60
	print("Remaining hours: " + str(numHours))
	print("Remaining minutes: " + str(numMins))


print(
	"Welcome to Juni World! We have a large selection of rides for you to ride! We'll even help you keep track of how much time you have left in the park after each ride!\n")

while minutesRemaining > 15:
	print("Here's how much time you have left in Juni World:")
	printAsHours(minutesRemaining)
	
	print("\nHere are the rides and their wait times: ")
	for ride in ridesDict:
		print(ride + ": " + str(ridesDict[ride]) + " minutes")
	
	desiredRide = input("\nEnter the ride you wish to go on next: ")
	while desiredRide not in ridesDict:
		desiredRide = input("\nSorry, that ride isn't part of the list. Please enter the ride you wish to go on next: ")
	
	waitTime = ridesDict[desiredRide]
	print("\nThat was awesome! You rode the " + desiredRide + "\n")
	
	# update minutesRemaining and visitedRides
	minutesRemaining -= ridesDict[desiredRide]
	visitedRides.append(desiredRide)

print("\nWow! That was a great day. Here's a list of all the rides you visited today, in order: ")
for ride in visitedRides:
	print(ride)
print("\nThanks for visiting Juni World! Come back again soon!")
