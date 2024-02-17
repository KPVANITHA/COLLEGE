class Graph:
    def __init__(self):
        self.graph = {}
        self.heuristic = {}
        self.pqueue = []
        self.all_paths = []

    def isEmpty(self):
        return len(self.pqueue) == 0
        
    def enqueue(self, node, cost, path):
        self.pqueue.append((node, cost, path))
        self.all_paths.append((cost, path))

        '''for n,c,p in self.pqueue:
            print(p," : ", c)'''

    def dequeue(self):
        state, cost, path = min(self.pqueue, key = lambda x:x[1])
        self.pqueue.remove((state, cost, path))
        return state, cost, path
    
    def all_paths_display(self):
        for c, p in self.all_paths:
            print(p, " : ", c)

    def addEdge(self, node1, node2, c):
        if node1 not in self.graph:
            self.graph[node1] = []
        if node2 not in self.graph:
            self.graph[node2] = []
        t = (node2, c)
        self.graph[node1].append(t)

    def addNode(self, n, h):
        if n not in self.graph:
            self.graph[n] = []
            self.heuristic[n] = h
            print("Node added successfully")
        else:
            print("Node already exists")

    def delNode(self, n):
        del self.graph[n]
        for val in self.graph.values():
            for i, j in val:
                if i == n:
                    val.remove((i, j))

    def delEdge(self, node1, node2):
        if node1 in self.graph and node2 in self.graph:
            for key, val in self.graph.items():
                if key == node1:
                    for i, j in val:
                        if i == node2:
                            val.remove((i, j))
                if key == node2:
                    for i, j in val:
                        if i == node1:
                            val.remove((i, j))

    def display(self):
        print("Graph:")
        for key, val in self.graph.items():
            print(f"{key} -> {val}")
        print("Heuristic values:")
        for key, val in self.heuristic.items():
            print(f"{key} -> {val}")

    def astarSearch(self, start, end):
        visited = set()
        self.enqueue(start, 0, [start])

        while not self.isEmpty():
            state, fn, path = self.dequeue()

            if state == end:
                return fn, path
            
            visited.add(state)
            if fn != 0:
                fn = fn - int(self.heuristic[state])

            for neighbour, edge_cost in self.graph[state]:
                if neighbour not in visited:
                    self.enqueue(neighbour, (edge_cost + int(self.heuristic[neighbour]) + fn), path + [neighbour])

        return float('inf'), None

    def find_all_paths(self, start, end, path=[], cost=0):
        path = path + [start]
        if start == end:
            return [(path, cost)]
        if start not in self.graph:
            return []
        paths = []
        for node, edge_cost in self.graph[start]:
            if node not in path:
                new_cost = cost + edge_cost
                new_paths = self.find_all_paths(node, end, path, new_cost)
                for new_path in new_paths:
                    paths.append(new_path)
        return paths

g = Graph()

while True:
    print("\n**********TAKE THE MONKEY TO EAT FRUIT IT DESIRES**********")
    print("1) Add Tree\n2) Add Ropes between trees\n3) Help the monkey to reach the fruit at minimum cost?")
    print("4) Delete tree\n5) Delete Branch\n6) All short paths to reach all the trees\n7) Show tree connections\n8) Exit")
    ch = int(input("Enter the choice: "))
    
    if ch == 1:
        n = input("Enter the Tree to add: ")
        h = input("Enter the heuristic value of the Tree: ")
        g.addNode(n, h)

    elif ch == 2:
        n1, n2 = input("Enter the trees to add ropes between them: ").split()
        c = int(input("Enter the cost for this rope:"))
        g.addEdge(n1, n2, c)

    elif ch == 3:
        start, goal = input("Enter the start tree and the fruit name to reach: ").split()
        cost, path = g.astarSearch(start, goal)
        if cost == float('inf'):
            print("No path found")
        else:
            print("ALL POSSIBLE PATHS ARE: ")
            g.all_paths_display()
            print("Optimal path is : ", path)
            print("Minimum cost from tree", start, "to fruit:", cost)
        
    elif ch == 4:
        n = input("Enter tree to cut: ")
        g.delNode(n)
        g.display()

    elif ch == 5:
        n1, n2 = input("Enter the trees between which we have to cut the rope: ").split()
        g.delEdge(n1, n2)
                
    elif ch == 6:
        print("Fringe cost to reach all trees: ")
        start, goal = input("Enter the start tree and the fruit name to reach: ").split()
        all_paths = g.find_all_paths(start, goal)
        for path, cost in all_paths:
            print(' -> '.join(path), "Cost:", cost)
        
    elif ch == 7:
        g.display()

    elif ch == 8:
        print("EXITING!!!")
        break

    else:
        print("Invalid choice! Please enter the correct choice!")     
