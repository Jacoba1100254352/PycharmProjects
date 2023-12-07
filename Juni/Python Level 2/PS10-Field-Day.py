kickball = []
flag = []

for i in range(10):
    name = input("Enter your name: ")

    answer = input(
        "Would you like to play kickball, capture the flag, both, or neither?\nEnter '1' for kickball\nEnter '2' for capture the flag\nEnter '3' for both\nEnter '4' for neither\nYour choice: ")
    print()

    if answer == '1' or answer == '3':
        kickball.append(name)
    if answer == '2' or answer == '3':
        flag.append(name)

print("Kickball team roster:")
for name in kickball:
    print(name)

print("Capture the flag roster:")
for name in flag:
    print(name)
