for i in range(4):
    size = i + 3

    # draw the top side of the box
    for j in range(size):
        print("#", end="")
    print("")

    # draw the sides of the box, one line at a time
    for j in range(size - 2):
        print("#", end="")
        for k in range(size - 2):
            print(" ", end="")
        print("#")

    # draw the bottom side of the box
    for j in range(size):
        print("#", end="")
    print("")

    print()
