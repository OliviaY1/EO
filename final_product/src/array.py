from setting import NUM_ROWS, NUM_COLS
import random
import heapq

class ArrayGameBoard:
    grid: list[list[int]]
    is_game_over: bool
    apples: list[tuple[int, int]]
    def __init__(self, num_rows=NUM_ROWS, num_cols=NUM_COLS):
        # Initialize the 2D array representing the gameboard
        self.grid = [[0] * NUM_COLS for _ in range(NUM_ROWS)]
        
        # Set the initial snake position in the center of the grid
        self.snake_body = [(NUM_ROWS // 2, NUM_COLS // 2)]  # List of (row, col) tuples
        self.grid[self.snake_body[0][0]][self.snake_body[0][1]] = 1  # Mark the initial position of the snake

        # Directions dictionary for movement
        self.current_direction = 'up'  # Default initial direction
        self.directions = {
            'up': (-1, 0),
            'down': (1, 0),
            'left': (0, -1),
            'right': (0, 1)
        }
        self.apples = []
        self.place_apple()
        self.place_apple()
        self.is_game_over = False
    
    def place_apple(self):
        while True:
            row = random.randint(0, NUM_ROWS - 1)
            col = random.randint(0, NUM_COLS - 1)
            if self.grid[row][col] == 0:  # Ensure it's an empty cell
                self.grid[row][col] = 2  # Place an apple
                self.apples.append((row, col))
                break
        

    def move(self, direction):
        """Move the snake in the specified direction."""
        # update the current direction
        if direction in self.directions:
            self.current_direction = direction
        elif direction != 'current_direction':
            raise ValueError(f"Invalid direction: {direction}")

        # Get the current head position
        current_head = self.snake_body[0]
        row_change, col_change = self.directions[self.current_direction]
        new_head = (current_head[0] + row_change, current_head[1] + col_change)

        # when movement is valid:
        if 0 <= new_head[0] < NUM_ROWS and 0 <= new_head[1] < NUM_COLS:
            self.snake_body.insert(0, new_head)
            if self.grid[new_head[0]][new_head[1]] == 2: # hit an apple
                # Eat the apple and grow the snake (do not remove tail)
                self.grid[new_head[0]][new_head[1]] = 1 
                self.apples.remove(new_head)
                self.place_apple()  # Place a new apple
            elif self.grid[new_head[0]][new_head[1]] == 1: # hit snake itself
                self.is_game_over = True
            else:
                self.grid[new_head[0]][new_head[1]] = 1
                # Remove the tail (simulate movement)
                tail = self.snake_body.pop()
                self.grid[tail[0]][tail[1]] = 0  # Clear the old tail position
        else:
            self.is_game_over = True

    def get_grid(self):
        """Returns the current state of the gameboard."""
        return self.grid
    
    def is_game_over(self):
        return self.is_game_over
    
    def get_score(self):
        return len(self.snake_body) - 1

    def __str__(self) -> str:
        res = ""
        for row in self.grid:
            for cell in row:
                if cell == 0:
                    res += "_ "
                else:
                    res += str(cell) + " "
            res += "\n"
        return res
        
    def manhattan_distance(self, pos1, pos2):
        """Calculate Manhattan distance between two positions."""
        return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])
    
    def greedy_best_first_search(self) -> str:
        """Perform one-move horizon Greedy Best-First Search to get the next move direction."""
        
        # Priority queue to store possible moves
        priority_queue = []
        head = self.snake_body[0]  # Current position of the snake's head

        # Check all four possible directions
        for direction, (row_change, col_change) in self.directions.items():
            new_head = (head[0] + row_change, head[1] + col_change)

            # Check if the new position is within bounds and not a collision with the snake's body
            if 0 <= new_head[0] < NUM_ROWS and 0 <= new_head[1] < NUM_COLS and self.grid[new_head[0]][new_head[1]] != 1:
                # Calculate the Manhattan distance to the apple
                for apple in self.apples:
                    distance = self.manhattan_distance(new_head, apple)
                    heapq.heappush(priority_queue, (distance, direction))

        # Get the best move based on the closest Manhattan distance
        if priority_queue:
            _, best_direction = heapq.heappop(priority_queue)
            return best_direction
        else: # no way to go
            self.is_game_over = True
            return "up"

if __name__=="__main__":
    game = ArrayGameBoard()
    print(game)
    while (not game.is_game_over):
        r = game.greedy_best_first_search()
        game.move(r)
        print(game)
        print(game.get_score())
        print(game.is_game_over)