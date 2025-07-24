from queue import PriorityQueue


class Node:
	
	def __init__(self, jug3L, jug5L, ):
		self.state = (jug3L, jug5L)
		self.neighbors = []
	
	def __eq__(self, other):
		return self.__class__ == other.__class__ and self.state == other.state
	
	def __lt__(self, other):
		return self.state < other.state
	
	# change string of both jug values to an int
	def __hash__(self):
		return int(str(self.state[0]) + str(self.state[1]))
	
	def __str__(self):
		return '3 Liter Jug: ' + str(self.state[0]) + ' | 5 Liter Jug: ' + str(self.state[1])
	
	# puzzle is solved if 5L Jug has 4L of water
	def is_solved(self):
		return self.state[1] == 4
	
	def get_heuristic(self):
		# if board is solved board, don't need to keep going
		# so we return the lowest possible heuristic value
		if self.is_solved():
			return 0
		
		# get the difference between the 4 (the amount we want) and the total number of liters of water in the the two jugs
		diff = abs(4 - (self.state[0] + self.state[1]))
		
		# if diff is 0, you are 1 move away from winning so return 1. Otherwise return the difference (assume that closer to value we want is closer to correct state)
		if diff == 0:
			return 1
		else:
			return diff
	
	# generate all possible neighbors of current node
	def generate_neighbors(self):
		neighbors = []
		
		# 6 possible actions from each Node
		# pour from 3L to 5L
		if self.state[0] + self.state[1] <= 5:
			neighbors.append(Node(0, self.state[0] + self.state[1]))
		else:
			neighbors.append(Node(self.state[0] - (5 - self.state[1]), 5))
	
	# pour from 5L to 3L
