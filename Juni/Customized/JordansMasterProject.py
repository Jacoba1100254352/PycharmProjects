import random


# map#
Map = [[1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
       [1, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
       [1, 0, 1, 1, 1, 1, 1, 1, 1, 2, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 1],
       [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1],
       [1, 3, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1],
       [1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1],
       [1, 1, 1, 4, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 5, 1, 1, 1, 1],
       [1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
       [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1]]
visualMap = "1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1\n1,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1\n1,0,1,1,1,1,1,1,1,0,0,0,0,0,1,1,1,1,1,1,1\n1,0,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,0,1,1,1\n1,0,0,0,0,0,1,1,1,1,1,1,1,0,1,1,0,0,1,1,1\n1,0,1,1,1,0,1,0,0,0,0,0,0,0,1,1,0,1,1,1,1\n1,1,1,0,0,0,1,0,1,1,1,1,1,0,0,0,0,1,1,1,1\n1,1,1,1,1,0,0,0,0,1,1,1,1,1,1,1,0,1,1,1,1\n1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1"


def color(text):
	return ('\033[91m' + text + '\033[0m')


def printMap(x, y):
	# for i in range(len(Map[0])):
	#  print("_", end="")
	# print()
	
	for index in range(len(Map)):
		rowCopy = Map[index].copy()
		for i in range(len(rowCopy)):
			if rowCopy[i] == 2 or rowCopy[i] == 3 or rowCopy[i] == 4 or rowCopy[i] == 5:
				rowCopy[i] = 0
		Row = str(rowCopy)
		Row = Row[1:len(Row) - 1]
		
		# Color our current position red
		for i, value in enumerate(Row):
			if index == y and i == x * 3:
				Row = Row[:i] + color(value) + Row[i + 1:]
				# Map[index][i] = color(value)
		
		# Only print the rows within range (5 positions) of our current location
		# leftMostPos = 0 if x<= 1 else (x+2)*3-1-len(color('0'))-1 if index == y else (x-2)*3
		if x <= 1:
			leftMostPos = 0
		else:
			if index == y:
				leftMostPos = (x + 2) * 3 - 1 - len(color('0')) - 1
			else:
				leftMostPos = (x - 2) * 3
		
		if y - 3 < index < y + 3:
			if index == y:
				Row = Row[leftMostPos:(x + 3) * 3 - 2 + len(color('0')) - 1]
			else:
				Row = Row[leftMostPos:(x + 3) * 3 - 2]
			print(Row)
	
	# for i in range(len(Map[0])):
	#  print("_", end="")
	# print()


"""
def printMap(x, y):  
    for index in range(len(Map)):  
        rowCopy = Map[index].copy()  
        for i in range(len(rowCopy)):  
            if rowCopy[i] == 2 or rowCopy[i] == 3 or rowCopy[i] == 3:  
                rowCopy[i] = 0  
        for i, value in enumerate(Map[index]):  
            if index == y and i == x * 3:  
                #Row = Row[:i] + color(value) + Row[i+1:]  
                Map[index][i] = color(str(value))  
        Row = str(rowCopy)  
        Row = Row[1:len(Row) - 1]  
        print(f"{Row}") 
"""

# variables#
x = 1
y = 0
currentPosition = (Map[y][x])
hp = 100


# functions#
def clear():
	print("\033c", end="")


def checkPostion():
	global y, x, currentPosition
	positionCheck = (Map[y][x])
	if positionCheck == 1:
		print("You can't move there")
		return False
	else:
		currentPosition = positionCheck
		return True


def move(direction, amount):
	positionCheck = 0
	global y, x, currentPosition
	initialY = y
	initialX = x
	if direction == "forwards":
		y += amount
	elif direction == "backwards":
		y -= amount
	elif direction == "left":
		x += amount
	elif direction == "right":
		x -= amount
	else:
		print("That option doesn't exist, please reenter:")
		direction = input("what direction would you like to go(forwards,backwards,left,right)")
		amount = int(input("how many steps would you like to take?"))
		move(direction, amount)
	
	# If unable to move somewhere, don't update position, instead ask again
	if not checkPostion():
		direction = input("what direction would you like to go(forwards,backwards,left,right)")
		amount = int(input("how many steps would you like to take?"))
		y = initialY
		x = initialX
		move(direction, amount)


def monster(mhp, dmg, c1, c2):
	global hp
	while mhp >= 1 and hp >= 1:
		attack = input("punch(10dmg/100%),slash(40dmg/50%),or kick(20dmg/80%):")
		if attack == "punch":
			mhp -= 10
			print("the monsters hp is " + str(mhp))
		elif attack == "slash":
			chance = random.randint(1, 2)
			if chance == 1:
				mhp -= 40
				print("the monsters hp is " + str(mhp))
			elif chance == 2:
				print("u missed")
		elif attack == "kick":
			chance = random.randint(1, 5)
			if chance != 5:
				mhp -= 20
				print("the monsters hp is " + str(mhp))
			else:
				print("u missed")
		if mhp <= 0:
			print("you defeated the monster")
			input("Press Enter to continue...")
		elif hp <= 0:
			print("you died")
			exit()
		print("its the monsters turn now")
		print("the monster attacks")
		chance = random.randint(c1, c2)
		if chance == 1:
			hp -= dmg
			print("your hp is " + str(hp))
		else:
			print("the monster missed")


input("Welcome to the dungeon. Your objective is to find the correct way out without dying. 1's are walls and 0's are where you can walk. You have 100 health points. Click ENTER to play!")
while True:
	clear()
	
	printMap(x, y)
	# print(visualMap)
	
	direction = input("what direction would you like to go(forwards,backwards,left,right)")
	amount = int(input("how many steps would you like to take?"))
	
	move(direction, amount)
	print(currentPosition)
	if currentPosition == 3:
		print("you have encountered a monster!")
		print("It has 100hp and does 10dmg/50%")
		monster(100, 10, 1, 2)
	
	if currentPosition == 2:
		hp += 30
		print("your hp is " + str(hp))
	
	if currentPosition == 4:
		print("you have encountered a monster!")
		print("It has 150hp and does 30dmg/20%")
		monster(150, 15, 1, 5)
	
	if currentPosition == 5:
		print("you have encountered a monster!")
		print("It has 100hp and does 20dmg/50%")
		monster(100, 20, 1, 2)
	
	if currentPosition == Map[8][17]:
		print("u escaped the dungeon :)")
