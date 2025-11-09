"""
Your friend, Kant D. Bugg, is learning how to use for loops and while loops and wrote a program to simulate a rocketship launch. His code contains some bugs, and he needs your help to debug it. Help Kant debug his code and get the rocketship launch simulator working! Remember to read Kant’s comments so you know what each piece of code is supposed to do.

Each time you run the code, read the error messages in the console. Each message will tell you which line to look for a bug, and even give you a hint about what the bug is. After you find and fix the bug, run the code again. Read the new error message and find the next bug, until the program runs fully! If you can't remember how to fix a certain line of code, look at one of your past projects for an example. You can copy and paste Kant's buggy code into your file from here: https://repl.it/@JuniLearning/PS2-Debugging-Loops.
"""

# Ask the astronauts if they are ready to take off. Keep asking them until they say they are ready
while input("Are we ready for takeoff yet? (Y/N): ") != "Y":
	print("Rechecking critical systems...")

# Print the countdown to takeoff (print the numbers from 10 down to 1)
print()
print("Final Countdown:")
for i in range(10, 0, -1):
	print(i)
print("Blastoff!!")

print()

# Print out whether the spaceship is still in earth's atmosphere every 15 seconds. For example, it should print "0 minutes and 0 seconds", "0 minutes and 15 seconds", "0 minutes and 30 seconds" ... "4 minutes and 45 seconds"
# The spaceship should exit the atmosphere after 5 minutes
print("The spaceship has been in the atmosphere for:")
for i in range(5):
	for j in range(0, 60, 15):
		print(i, "minutes and", j, "seconds")
print("The spaceship has exited the atmosphere after 5 minutes")
