graph = dict()
dblock_graph = []#node=buliding block name
d = 1
route = []
queue = []
fringe = {}


class priorityQueue:
    
    '''def enqueue(n, c, l): #n is the deptblock.c is the cost.l is the path.

     queue.append((n,c,l))
    
    def sort(queue):
     #to sort the priority queue based on the cost of the paths to the deptblocks.   
     queue.sort(key =lambda x:x[1])
     
    def dequeue():
     deptblock, cost, path = queue.pop(0)
     return deptblock, cost, path'''
    def enqueue(self,n,c,a):
        queue.append((n,c,a))
        self.PercolateUp(len(queue) - 1)
    def dequeue(self):
        priority ,item,a = queue[0]
        self.swap(0, len(queue) - 1)
        queue.remove(queue[len(queue)-1])
        self.PercolateDown(0)
        return priority, item, a
    def peek():
        a,b,c = queue[0]
        return a,b,c
    def PercolateUp(self,i):
        parent = (i - 1)//2
        while i > 0 and queue[i][1] < queue[parent][1]:
            self.swap(i, parent)
            i = parent
            parent = (i - 1)//2
    def PercolateDown(self,i):
        while True:
            left = 2*i+1
            right = 2*i+2
            minimum = i
            #print("Hi")
            if left<len(queue) and queue[left][1]<queue[minimum][1]:
                minimum = left
            if right<len(queue) and queue[right][1]<queue[minimum][1]:
                minimum = right
            if minimum != i:
                self.swap(i, minimum)
                i = minimum
            else:
                break
    def swap(self, i, j):
        queue[i], queue[j] = queue[j], queue[i]
    

#Graph initialization
def addroute(block1, block2, d, c):
    if block1 not in graph:
        graph[block1] = [] #When a block comes initially it will not be having any neighbours

    if block2 not in graph:
        graph[block2] = []

    if(d == 1):
        t = (block2, c)
        graph[block1].append(t)

    else:
        t1 = (block2, c)
        graph[block1].append(t1)
        t2 = (block1, c)

    
def uniform_cost_search(graph, start_deptblock, destination_deptblock):
    visited = set()  # Set to store visited deptblocks
    q=priorityQueue()
    q.enqueue(start_deptblock, 0, [start_deptblock])  # List to store blocks and their costs

    while queue:
          #sorts the priority queue based on the cost of the paths to the deptblocks
        #q.sort(queue)
        deptblock, cost, path =  q.dequeue()

        #checks if the dequeued deptblock is the destination deptblock.
        if deptblock == destination_deptblock:
            print("THE PATH TO THE DESTINATION DEPTBLOCK IS :",path)
            return cost

        visited.add(deptblock)
        
        #adds all of its unvisited neighbors to the priority queue.
        for neighbor, route_cost in graph[deptblock]:
            if neighbor not in visited:
                 q.enqueue(neighbor, cost + route_cost, path + [neighbor])
                 path = path + [neighbor]
                 print("Path:", path)
                

 # If destination_deptblock deptblock is not reachable   
    return float('inf')  

def display():
    for key, val in graph.items():
            print(f"{key}-->{val}")
               
    
def calculate_fringe(graph):
    f = 0
    for key in graph.keys():
        start_deptblock = key
        break
    fringe[start_deptblock] = 0
    for key in graph.keys():
        if key != start_deptblock:
            c = uniform_cost_search(graph, start_deptblock, key)
            fringe[key] = c

    print("Fringe list is: ", fringe)
    
while True:
        print("\n***MENU***")
        print("----------------------------------")     
        print("1) Graph initialization")
        print("2) Add department block")
        print("3) Add route")
        print("4) uniform cost search")
        print("5) Delete the department block")
        print("6) Delete the route")
        print("7) Calculate fringe")
        print("8) Display graph")
        print("9)Exit")
        print("------------------------------------")
        ch = int(input("Enter the choice: "))
        if ch == 1:
                d = int(input("Directed graph(1) or undirected graph(0)"))
                blocks, routes = input("Enter number of department blocks and no. of routes").split()
                print("Enter the department block who has routes between them: ")
                for i in range(int(routes)):
                    block1, block2 = input().split()
                    c = int(input(("Now enter the cost for this route: ")))
                    addroute(block1, block2, d, c)
                    if block1 not in dblock_graph:
                        dblock_graph.append(block1)
                    if block2 not in dblock_graph:
                        dblock_graph.append(block2)
                print("The department block list is: ", dblock_graph)
                display()
        elif ch == 2:
                n = input("Enter the department block to add: ")
                if n not in dblock_graph:
                        dblock_graph.append(n)
                        graph[n] = []
                else:
                        print("department block already exists")
        elif ch == 3:
                n1, n2 = input("Enter the department blocks to add route between them: ").split()
                c = int(input("Enter the cost for this route:"))
                addroute(n1, n2, d, c)
                display()
        elif ch == 4:
                start_deptblock, destination_deptblock = input("Enter the start_deptblock & destination_deptblock block").split()

                cost = uniform_cost_search(graph, start_deptblock, destination_deptblock)

                print(f"Minimum cost from {start_deptblock} to {destination_deptblock}: {cost}")
        elif ch == 5:
                n = input("Enter block to delete: ")
                del graph[n]
                for val in graph.values():
                    for i,j in val:
                        if i == n:
                           val.remove((i, j))
                display()
        elif ch == 6:
            
            n1, n2= input("Enter the 2 nodes between whom you want to remove an edge: ").split()
             
            '''
             for key,val in graph.items():
              if key == block1:
                if(block2 in val):
                    val.remove(block2)
              if key == block2:
                if(block1 in val):
                    val.remove(block1)
              display()                    
            '''
            ''' 
            n1= input("Enter the block name to be deleted: ")
            n2=input("Enter the block name to be deleted: ")
            '''
            if n1 in graph.keys():     
                     for k,val in graph.items():
                         if k==n1:
                            for i,j in val:
                                 if i == n2:
                                    val.remove((i,j))
            display()    
            
        elif ch == 7:
            print("Fringe cost to reach all blocks: ")
            calculate_fringe(graph)
        elif ch == 8:
                display()
                
        else:
                print("_______EXITING____")
                break

