# read in states
f = open("states.txt")
data = f.readlines()
states = [line.strip() for line in data]
f.close()

# read in capitals
f = open("capitals.txt")
data = f.readlines()
capitals = [line.strip() for line in data]
f.close()

# now, there is a list of states stored in the variable "states" and their corresponding capitals stored in "capitals"
