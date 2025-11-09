"""
The engineers at Space Mountain need to make sure their roller coaster is safe. Because the roller coaster has such precise physics, it will only be safe if the total weight of the four passengers in each car does not exceed 900 pounds. Write a program that allows the user to enter each rider's weight, and print how much weight capacity remains after each rider.
"""

sum = 0

rider1 = int(input("Enter person 1's weight: "))
sum += rider1
print("Remaining weight capacity: " + str(900 - sum) + " pounds")

rider2 = int(input("Enter person 2's weight: "))
sum += rider2
print("Remaining weight capacity: " + str(900 - sum) + " pounds")

rider3 = int(input("Enter person 3's weight: "))
sum += rider3
print("Remaining weight capacity: " + str(900 - sum) + " pounds")

rider4 = int(input("Enter person 4's weight: "))
sum += rider4
print("Remaining weight capacity: " + str(900 - sum) + " pounds")
