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
