size = int(input("Enter the size of the box: "))

for _ in range(size):
    for _ in range(size):
        print("#", end="")
    print()

"""
for _ in range(size):
    print("#"*size)

print(("#"*size+"\n")*size)
"""
