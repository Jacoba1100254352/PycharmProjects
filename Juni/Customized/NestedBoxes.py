# main.py

# Get the length of the initial row
rows = int(input("Enter the initial number of rows: "))

# Print all the boxes
for i in range(5):
    # Initialize each box
    size = rows + i  # alternatively "size += 1" can be placed at the end, or you can write size += 1 if i != 0 else 0
    box = ["" for row in range(size)]

    # Fill each row one character at a time
    for col in range(size):
        for row in range(size):
            if col == size - 1 or col == 0 or row == 0 or row == size - 1:
                box[row] += '#'
            else:
                box[row] += ' '

    # Print each box
    for row in range(size):
        print(box[row])
    print()  # Here to add a space between each box

"""
size = 3
numBoxes = 4

for _ in range(numBoxes):
    for i in range(size):
        # Create each line
        for j in range(size):
            # 
            if i == 0 or j == 0 or i == size - 1 or j == size - 1:
                print("#", end="")
            else:
                print(" ", end="")
        print()
    print()
    size += 1
"""

"""
size = 3
numBoxes = 4

for _ in range(numBoxes):
  # Create front line of box
  print("#"*size)

  # Create middle
  for _ in range(size-2):
    print("#" + " "*(size-2) + "#")

  # Create last line of box
  print("#"*size)
  print()
  size += 1
"""

"""
size = 3
numBoxes = 4

for _ in range(numBoxes):
  print("#"*size + "\n" + ("#" + " "*(size-2) + "#\n")*(size-2) + "#"*size + "\n")
  size += 1
"""

"""
size = 3
numBoxes = 4

for _ in range(numBoxes):
  # Create front line of box
  for _ in range(size):
    print("#", end="")
  print()

  # Create middle
  for _ in range(size-2):
    print("#", end = "")
    for _ in range(size-2):
      print(" ", end="")
    print("#")

  # Create last line of box
  for _ in range(size):
    print("#", end="")
  print("\n")
  size += 1
"""

"""
size = 3
numBoxes = 4
outputString = ""

for _ in range(numBoxes):
  # Create front line of box
  for _ in range(size):
    outputString += "#"
  outputString += "\n"

  # Create middle
  for _ in range(size-2):
    outputString += "#"
    for _ in range(size-2):
      outputString += " "
    outputString += "#\n"

  # Create last line of box
  for _ in range(size):
    outputString += "#"
  outputString += "\n\n"
  size += 1

print(outputString)
"""
