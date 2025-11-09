import queue


class Node:
	# Stores node id and a dict: neighbor_key -> edge weight
	def __init__(self, key):
		self.key = key
		self.neighbors = {}
	
	def add_neighbor(self, node, weight):
		self.neighbors[node.key] = weight
	
	def __str__(self):
		s = "ID: " + self.key + "\nNeighbors: "
		for n in self.neighbors:
			s += n + ":" + str(self.neighbors[n]) + "  "
		return s
	
	# PriorityQueue may compare items with equal priorities; keep this
	def __lt__(self, other):
		return self.key < other.key


class Graph:
	def __init__(self):
		self.graph = {}
	
	def add_node(self, node):
		self.graph[node.key] = node
	
	def get_node(self, key):
		return self.graph.get(key, None)
	
	# Undirected edge with weight
	def add_edge(self, node1, node2, weight):
		if node1.key not in self.graph:
			print("Node with ID " + node1.key + " is not in the graph")
		elif node2.key not in self.graph:
			print("Node with ID " + node2.key + " is not in the graph")
		else:
			node1.add_neighbor(node2, weight)
			node2.add_neighbor(node1, weight)
	
	def get_nodes(self):
		return list(self.graph.keys())
	
	def __str__(self):
		s = ""
		for node in self.graph:
			s += self.graph[node].__str__() + "\n\n"
		return s
	
	def a_star_search(self, start_key, goal_key, h_func):
		"""
        Classic A*:
        - start_key: key of the start node
        - goal_key: key of the goal node
        - h_func: callable h(node_key) -> estimated cost from node to goal
        Returns: (path_list, total_cost). Also prints expansion order.
        """
		if start_key not in self.graph or goal_key not in self.graph:
			raise ValueError("Start or goal not in graph")
		
		start = self.graph[start_key]
		goal = self.graph[goal_key]
		
		# g_score: best known cost from start to each node
		g_score = {k: float("inf") for k in self.graph}
		g_score[start.key] = 0.0
		
		# came_from: for path reconstruction
		came_from = {}
		
		# Priority queue items: (f, tie_breaker, node_key)
		# We keep a separate index to ensure a deterministic order on ties.
		pq = queue.PriorityQueue()
		tie = 0
		pq.put((h_func(start.key), tie, start.key))
		
		closed = set()
		expansion_order = []
		
		while not pq.empty():
			f_curr, _, curr_key = pq.get()
			if curr_key in closed:
				continue
			
			closed.add(curr_key)
			expansion_order.append(curr_key)
			
			if curr_key == goal.key:
				# Reconstruct path
				path = [curr_key]
				total_cost = g_score[curr_key]
				while curr_key in came_from:
					curr_key = came_from[curr_key]
					path.append(curr_key)
				path.reverse()
				print("Expansion order:", " ".join(expansion_order))
				print("Path:", " ".join(path))
				print("Total cost:", total_cost)
				return path, total_cost
			
			# Relax neighbors
			curr_node = self.graph[curr_key]
			for neigh_key, edge_w in curr_node.neighbors.items():
				if neigh_key in closed:
					continue
				tentative_g = g_score[curr_node.key] + edge_w
				if tentative_g < g_score[neigh_key]:
					g_score[neigh_key] = tentative_g
					came_from[neigh_key] = curr_node.key
					tie += 1
					f_val = tentative_g + h_func(neigh_key)
					pq.put((f_val, tie, neigh_key))
		
		# If we get here, no path to goal
		print("Expansion order:", " ".join(expansion_order))
		print("No path found.")
		return [], float("inf")


# ---- Build your example graph ----
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")

g = Graph()
g.add_node(a)
g.add_node(b)
g.add_node(c)
g.add_node(d)
g.add_node(e)

g.add_edge(a, b, 2)
g.add_edge(a, c, 1)
g.add_edge(e, d, 1)
g.add_edge(c, d, 1)
g.add_edge(b, e, 3)

# Heuristic tied to the goal "e":
# Matches your narrative idea: h(a)=3, h(b)=2, h(c)=2, h(d)=1, h(e)=0
h_map = {"a": 3, "b": 2, "c": 2, "d": 1, "e": 0}
h = lambda key: h_map[key]

# Run A* from a to e
# Expected optimal path: a -> c -> d -> e with cost 1 + 1 + 1 = 3
g.a_star_search("a", "e", h)
