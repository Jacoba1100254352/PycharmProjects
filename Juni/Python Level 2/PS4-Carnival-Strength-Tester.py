"""
At the carnival, there is a game where the player strikes a pad with hammer as hard as they can, bouncing a puck in the air. The game measures how high the puck flies, and the player wins a prize based on how high they can make the puck go. Ask the user to enter in how far the puck flew (in inches), and based on what is entered, print out the prize they won! Make sure there are at least four different possible prizes.
"""

height = int(input("Enter the height you reached (in inches): "))

if height < 50:
	print("Sorry, you do not win a prize!")
elif height < 100:
	print("You win a small stuffed animal!")
elif height < 150:
	print("You win a frisbee!")
else:
	print("You win a large stuffed animal!")
