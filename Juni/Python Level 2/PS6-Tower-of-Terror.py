"""
This Halloween, the ogres have invented a new ride: the Tower of Terror! They are very excited to test out their new ride. Each car in the Tower of Terror can hold up to 10 ogres. To make sure the ride is safe, the ogres need to make sure the riders' weights are distributed evenly. Help the ogres by first writing a function that asks the leader of the ogres to enter each of their rider's weights. The function should return this list. Then, print out the list of weights, the sum of the weights, and the average weight.
"""


def getWeights():
	riders = []
	for i in range(10):
		weight = input("Enter rider " + str(i + 1) + "'s weight (or q to quit): ")
		if weight == 'q':
			break
		riders.append(int(weight))
	return riders


riders = getWeights()
print("The list of rider weights is:")
print(riders)

sum = 0
for r in riders:
	sum += r
print("The total weight of the riders is: " + str(sum))
print("The average weight of the riders is: " + str(sum / len(riders)))
