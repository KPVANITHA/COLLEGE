#!/usr/bin/env python
# coding: utf-8

# In[8]:


class WumpusWorldSolver:
    def __init__(self, size, pits, wumpus, gold, start):
        self.size = size
        self.pits = pits
        self.wumpus = wumpus
        self.gold = gold
        self.start = start
        self.current_location = start
        self.visited = set()
        self.perceptions = {
            "breeze": False,
            "stench": False
        }
        self.score = 0

    def is_valid_location(self, location):
        x, y = location
        return 1 <= x <= self.size and 1 <= y <= self.size

    def is_safe_location(self, location):
        return (
            self.is_valid_location(location)
            and location not in self.pits
            and location != self.wumpus
        )

    def move(self, location):
        self.current_location = location
        self.visited.add(location)

    def update_perceptions(self):
      self.perceptions = {
        "breeze": self.current_location in self.adjacent_to_pits(),
        "stench": self.current_location == self.wumpus
      }


    def adjacent_to_pits(self):
        adjacent_cells = [
            (self.current_location[0] + 1, self.current_location[1]),
            (self.current_location[0] - 1, self.current_location[1]),
            (self.current_location[0], self.current_location[1] + 1),
            (self.current_location[0], self.current_location[1] - 1)
        ]
        return [cell for cell in adjacent_cells if self.is_valid_location(cell) and cell in self.pits]

    def adjacent_to_wumpus(self):
        adjacent_cells = [
            (self.wumpus[0] + 1, self.wumpus[1]),
            (self.wumpus[0] - 1, self.wumpus[1]),
            (self.wumpus[0], self.wumpus[1] + 1),
            (self.wumpus[0], self.wumpus[1] - 1)
        ]
        return [cell for cell in adjacent_cells if self.is_valid_location(cell)]


    def calculate_score(self):
        if self.current_location == self.gold:
            self.score += 1000  # Agent gets 1000 points for finding gold
        if self.current_location in self.pits:
            self.score -= 500  # Agent loses 1000 points for falling into a pit
        if self.current_location == self.wumpus:
            self.score -= 1000  # Agent loses 1000 points for being eaten by the Wumpus
        self.score -= 1  # Agent loses 1 point for each move

    def solve(self):
        path=[]
        path.append(self.start)
        moves = 0
        print("Initial state:")
        self.print_state()

        while self.current_location != self.gold:
            moves += 1
            possible_moves = [
                (self.current_location[0] + 1, self.current_location[1]),
                (self.current_location[0] - 1, self.current_location[1]),
                (self.current_location[0], self.current_location[1] + 1),
                (self.current_location[0], self.current_location[1] - 1),
            ]
            valid_moves = [move for move in possible_moves if self.is_safe_location(move) and move not in self.visited]

            if valid_moves:
              self.move(valid_moves[0])
              self.calculate_score()
              self.update_perceptions()  
              path.append(valid_moves[0])
              print(f"\nMove {moves}:")
              self.print_state()
              print(path)  

            else:
                print("\nStuck! No safe moves.")
                break

        if self.current_location == self.gold:
            print("\nFound gold in")
        else:
            print("\nGold could not be found.")

        print("\nFinal score:", self.score)

    def print_state(self):
      for i in range(self.size, 0, -1):
        row = []
        for j in range(1, self.size + 1):
            location = (i, j)
            cell_representation = ""
            if location == self.current_location:
                cell_representation += "A"  # Agent's current position
            if location in self.pits:
                cell_representation += "P"  # Pit
            if location == self.wumpus:
                cell_representation += "W"  # Wumpus
            if location == self.gold:
                cell_representation += "G"  # Gold
            if location in self.visited:
                cell_representation += "V"  # Visited empty cell
            # if "breeze" in self.perceptions and self.perceptions["breeze"]:
            #     cell_representation += "B"  # Breeze
            # if "stench" in self.perceptions and self.perceptions["stench"]:
            #     cell_representation += "S"  # Stench

            # Check if there are characters already on the grid
            if len(cell_representation) == 0:
                cell_representation = "-"  # Unvisited empty cell

            row.append(cell_representation.center(2))
        print(" ".join(row))
      print("Current Location:", self.current_location)
      print("Score:", self.score)
      self.update_perceptions()

    
def main():
    size = int(input("Enter the size of the Wumpus World: "))
    pits = []
    wumpus = ()
    gold = ()
    start = ()

    # Input handling for pits
    num_pits = int(input("Enter the number of pits: "))
    for _ in range(num_pits):
        pit_row, pit_col = map(int, input("Enter the pit position: ").split())
        pits.append((pit_row, pit_col))

    # Input handling for wumpus
    wumpus_row, wumpus_col = map(int, input("Enter the wumpus position: ").split())
    wumpus = (wumpus_row, wumpus_col)

    # Input handling for gold
    gold_row, gold_col = map(int, input("Enter the gold position: ").split())
    gold = (gold_row, gold_col)

    # Input handling for start position
    start_row, start_col = map(int, input("Enter the starting position: ").split())
    start = (start_row, start_col)

    # Create the solver and solve the problem
    solver = WumpusWorldSolver(size, pits, wumpus, gold, start)
    solver.solve()

if __name__ == "__main__":
    main()


# # 

# In[ ]:




