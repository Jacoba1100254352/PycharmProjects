# Ask the astronauts if they are ready to take off. Keep asking them until they say they are ready
while input("Are we ready for takeoff yet?(Y/N): ") != "Y"
	print("Rechecking critical systems...")

# Print the countdown to takeoff (print the numbers from 10 down to 1)
print()
print("Final Countdown:")
for i in range(10, 0)
	print(i)
print("Blastoff!!")

print()

# Print out whether the spaceship is still in earth's atmosphere every 15 seconds. For example, it should print "0 minutes and 0 seconds", "0 minutes and 15 seconds", "0 minutes and 30 seconds" ... "4 minutes and 45 seconds"
# The spaceship should exit the atmosphere after 5 minutes
print("The spaceship has been in the atmosphere for:")
for i in range(5):
	for i in range(15):
		print(i, "minutes and", i, "seconds")
print("The spaceship has exited the atmosphere after 5 minutes")
