name = input("What is your name? ")

print("Spelling your name...")

for i in range(len(name)):
    print(name[i])

print("Spelling every other letter in your name... ")

for i in range(0, len(name), 2):
    print(name[i])

print("Spelling your name backward... ")

for i in range(len(name) - 1, -1, -1):
    print(name[i])

print("Spelling your name...")

i = 0
while i < len(name):
    print(name[i])
    i += 1

print("Spelling every other letter in your name... ")

i = 0
while i < len(name):
    print(name[i])
    i += 2

print("Spelling your name backward... ")

i = len(name) - 1
while i >= 0:
    print(name[i])
    i -= 1
