f = open("input.txt")
lines = f.readlines()
lines = [line.strip() for line in lines]
f.close()

d = {}

keys = []
values = []
for i in range(len(lines)):
	if i % 2:
		values.append(lines[i])
	else:
		keys.append(lines[i])

for i in range(len(keys)):
	d[keys[i]] = values[i]

print(d)
