'''
from queue import PriorityQueue

def uniform_search(graph, start, goal):
    # Create a priority queue to store the nodes to be explored
    queue = PriorityQueue()
    queue.put((0, start))  # Add the start node to the queue with a priority of 0

    # Create a dictionary to store the cost of reaching each node
    cost = {start: 0}

    # Create a dictionary to store the path to each node
    path = {start: []}

    while not queue.empty():
        # Get the node with the lowest priority (cost)
        current_cost, current_node = queue.get()

        # Check if the current node is the goal
        if current_node == goal:
            return path[current_node]

        # Explore the neighbors of the current node
        for neighbor, neighbor_cost in graph[current_node].items():
            # Calculate the total cost to reach the neighbor
            total_cost = current_cost + neighbor_cost

            # Check if the neighbor has not been visited or the new cost is lower
            if neighbor not in cost or total_cost < cost[neighbor]:
                # Update the cost and path to the neighbor
                cost[neighbor] = total_cost
                path[neighbor] = path[current_node] + [neighbor]

                # Add the neighbor to the queue with the new cost as priority
                queue.put((total_cost, neighbor))

    # If the goal is not reachable, return None
    return None


# Define the input graph
graph = {
    'A': {'B': 2, 'C': 3},
    'B': {'D': 4, 'E': 5},
    'C': {'F': 6},
    'D': {},
    'E': {'G': 7},
    'F': {},
    'G': {}
}

# Specify the start and goal nodes
start = 'A'
goal = 'G'

# Perform the uniform search
path,+cost = uniform_search(graph, start, goal)

# Display the path and cost
if path is not None:
    print("Path:", path)
    print("Cost:", cost)
else:
    print("Goal is not reachable.")

'''
    
    
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

'''
class PriorityQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item, priority):
        self.queue.append((item, priority))
        self.queue.sort(key=lambda x: x[1])

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        return None

    def is_empty(self):
        return len(self.queue) == 0


def uniform_search(graph, start, goal):
    # Create a priority queue to store the nodes to be explored
    queue = PriorityQueue()
    queue.enqueue(start, 0)  # Add the start node to the queue with a priority of 0

    # Create a dictionary to store the cost of reaching each node
    cost = {start: 0}

    # Create a dictionary to store the path to each node
    path = {start: []}

    while not queue.is_empty():
        # Get the node with the lowest priority (cost)
        current_node, current_cost = queue.dequeue()

        # Check if the current node is the goal
        if current_node == goal:
            return path[current_node], cost[current_node]

        # Explore the neighbors of the current node
        for neighbor, neighbor_cost in graph[current_node].items():
            # Calculate the total cost to reach the neighbor
            total_cost = current_cost + neighbor_cost

            # Check if the neighbor has not been visited or the new cost is lower
            if neighbor not in cost or total_cost < cost[neighbor]:
                # Update the cost and path to the neighbor
                cost[neighbor] = total_cost
                path[neighbor] = path[current_node] + [neighbor]

                # Add the neighbor to the queue with the new cost as priority
                queue.enqueue(neighbor, total_cost)

    # If the goal is not reachable, return None
    return None, None
'''
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
'''
from queue import PriorityQueue

def ucs(graph, start, goal):
    visited = set()
    queue = PriorityQueue()
    queue.put((0, start, [start]))
    while not queue.empty():
        cost, node, path = queue.get()
        if node not in visited:
            visited.add(node)
            if node == goal:
                return cost, path
            for neighbor, weight in graph[node].items():
                if neighbor not in visited:
                    total_cost = cost + weight
                    queue.put((total_cost, neighbor, path + [neighbor]))
    return None, None

# Example usage
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'D': 3},
    'C': {'D': 2},
    'D': {'E': 1},
    'E': {}
}
start = 'A'
goal = 'E'
cost, path = ucs(graph, start, goal)
print(f"Cost: {cost}")
print(f"Path: {path}")
'''

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@22
'''
from queue import PriorityQueue

class Graph:
    def __init__(self):
        self.edges = {}
        self.weights = {}

    def add_edge(self, from_node, to_node, weight):
        if from_node not in self.edges:
            self.edges[from_node] = {}
        self.edges[from_node][to_node] = weight
        self.weights[(from_node, to_node)] = weight

    def add_node(self, node):
        if node not in self.edges:
            self.edges[node] = {}

    def delete_node(self, node):
        if node in self.edges:
            del self.edges[node]
            for from_node in self.edges:
                if node in self.edges[from_node]:
                    del self.edges[from_node][node]
                    del self.weights[(from_node, node)]

    def get_cost(self, from_node, to_node):
        return self.weights[(from_node, to_node)]

    def ucs(self, start, goal):
        visited = set()
        queue = PriorityQueue()
        queue.put((0, start, [start]))
        while not queue.empty():
            cost, node, path = queue.get()
            if node not in visited:
                visited.add(node)
                if node == goal:
                    return cost, path
                for neighbor in self.edges[node]:
                    if neighbor not in visited:
                        total_cost = cost + self.get_cost(node, neighbor)
                        queue.put((total_cost, neighbor, path + [neighbor]))
        return None, None

# Example usage
graph = Graph()

while True:
    print("1. Add edge")
    print("2. Add node")
    print("3. Delete node")
    print("4. Find cost and path")
    print("5. Quit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        from_node = input("Enter the from node: ")
        to_node = input("Enter the to node: ")
        weight = int(input("Enter the weight: "))
        graph.add_edge(from_node, to_node, weight)
    elif choice == 2:
        node = input("Enter the node: ")
        graph.add_node(node)
    elif choice == 3:
        node = input("Enter the node: ")
        graph.delete_node(node)
    elif choice == 4:
        start = input("Enter the start node: ")
        goal = input("Enter the goal node: ")
        cost, path = graph.ucs(start, goal)
        if cost is not None:
            print(f"Cost: {cost}")
            print(f"Path: {path}")
        else:
            print("No path found.")
    elif choice == 5:
        break
    else:
        print("Invalid choice. Try again.")
'''
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
class PriorityQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item, priority):
        self.queue.append((item, priority))
        self.queue.sort(key=lambda x: x[1])

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        return None

    def is_empty(self):
        return len(self.queue) == 0


def uniform_search(graph, start, goal):
    # Create a priority queue to store the nodes to be explored
    queue = PriorityQueue()
    queue.enqueue(start, 0)  # Add the start node to the queue with a priority of 0

    # Create a dictionary to store the cost of reaching each node
    cost = {start: 0}

    # Create a dictionary to store the path to each node
    path = {start: []}

    while not queue.is_empty():
        # Get the node with the lowest priority (cost)
        current_node, current_cost = queue.dequeue()

        # Check if the current node is the goal
        if current_node == goal:
            return path[current_node], cost[current_node]

        # Explore the neighbors of the current node
        for neighbor, neighbor_cost in graph[current_node].items():
            # Calculate the total cost to reach the neighbor
            total_cost = current_cost + neighbor_cost

            # Check if the neighbor has not been visited or the new cost is lower
            if neighbor not in cost or total_cost < cost[neighbor]:
                # Update the cost and path to the neighbor
                cost[neighbor] = total_cost
                path[neighbor] = path[current_node] + [neighbor]

                # Add the neighbor to the queue with the new cost as priority
                queue.enqueue(neighbor, total_cost)

    # If the goal is not reachable, return None
    return None, None


# Get the input from the user
graph = {}
num_nodes = int(input("Enter the number of nodes in the graph: "))

for i in range(num_nodes):
    node = input("Enter the name of node {}: ".format(i + 1))
    num_neighbors = int(input("Enter the number of neighbors for node {}: ".format(node)))

    neighbors = {}
    for j in range(num_neighbors):
        neighbor = input("Enter the name of neighbor {}: ".format(j + 1))
        cost = int(input("Enter the cost to reach neighbor {}: ".format(neighbor)))
        neighbors[neighbor] = cost

    graph[node] = neighbors

start = input("Enter the start node: ")
goal = input("Enter the goal node: ")

# Perform the uniform search
path, cost = uniform_search(graph, start, goal)

# Display the path and cost
if path is not None:
    print("Path:", path)
    print("Cost:", cost)
else:
    print("Goal is not reachable.")