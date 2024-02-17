graph = dict()
node_graph = []
d = 1
cost = []
queue = []
fringe = {}
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


#Graph initialization
def addEdge(node1, node2, d, c):
     if node1 not in graph:
        graph[node1] = [] #When a node comes initially it will not be having any neighbours

     if node2 not in graph:
        graph[node2] = []

     if(d == 1):
        t = (node2, c)
        graph[node1].append(t)

     else:
        t1 = (node2, c)
        graph[node1].append(t1)
        t2 = (node1, c)


def uniform_cost_search(graph, start, goal):
    visited = set()  # Set to store visited states
    priorityqueue =PriorityQueue
    priorityqueue.enqueue(start, 0, [start])  # List to store nodes and their costs

    while queue:
          # Sort the queue based on cost
        priorityqueue.sort(queue)
        state, cost, path = priorityqueue.dequeue()

        if state == goal:
            print(path)
            return cost

        visited.add(state)

        for neighbor, edge_cost in graph[state]:
            if neighbor not in visited:
                priorityqueue.enqueue(neighbor, cost + edge_cost, path + [neighbor])

    return float('inf')  # If goal state is not reachable

def display():
     for key, val in graph.items():
            print(f"{key}-->{val}")
               
    
def calculate_fringe(graph):
     f = 0
     for key in graph.keys():
        start = key
        break
     fringe[start] = 0
     for key in graph.keys():
        if key != start:
            c = uniform_cost_search(graph, start, key)
            fringe[key] = c
        print("Fringe list is: ", fringe)
    
    
while True:
        print("\n***MENU***")
        print("1)Give Graph initialisation\n2)Add node\n3)Add edge\n4)uniform cost search\n5)Delete the node\n6)Delete the edge\n7)Calculate fringe\n8)Display Graph\n9)Exit")
        ch = int(input("Enter the choice: "))
        if ch == 1:
                d = int(input("Directed graph(1) or undirected graph(0)"))
                nodes, edges = input("Enter number of nodes and no. of edges").split()
                print("Enter the node who has edges between them: ")
                for i in range(int(edges)):
                    node1, node2 = input().split()
                    c = int(input(("Now enter the cost for this edge: ")))
                    addEdge(node1, node2, d, c)
                    if node1 not in node_graph:
                        node_graph.append(node1)
                    if node2 not in node_graph:
                        node_graph.append(node2)
                print("The node list is: ", node_graph)
                display()
        elif ch == 2:
                n = input("Enter the node to add: ")
                if n not in node_graph:
                        node_graph.append(n)
                        graph[n] = []
                else:
                        print("Node already exists")
        elif ch == 3:
                n1, n2 = input("Enter the nodes to add edge between them: ").split()
                c = int(input("Enter the cost for this edge:"))
                addEdge(n1, n2, d, c)
                display()
        elif ch == 4:
                start, goal = input("Enter the start & goal node").split()

                cost = uniform_cost_search(graph, start, goal)

                print(f"Minimum cost from {start} to {goal}: {cost}")
        elif ch == 5:
                n = input("Enter node to delete: ")
                del graph[n]
                for val in graph.values():
                    for i,j in val:
                        if i == n:
                           val.remove((i, j))
                display()
        elif ch == 6:
                n = input("Enter the node to be deleted: ")
                for val in graph.values():
                        for i,j in val:
                            if i == n:
                                val.remove((i,j))
        elif ch == 7:
            print("Fringe cost to reach all nodes: ")
            calculate_fringe(graph)
        
        else:
                print("EXITING.....")
                break