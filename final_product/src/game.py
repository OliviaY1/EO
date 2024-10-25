from setting import NUM_ROWS, NUM_COLS
import random

class ArrayGameBoard:
    grid: list[list[int]]
    is_game_over: bool
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
        self.place_apple()
        self.place_apple()
        self.is_game_over = False
    
    def place_apple(self):
        while True:
            row = random.randint(0, NUM_ROWS - 1)
            col = random.randint(0, NUM_COLS - 1)
            if self.grid[row][col] == 0:  # Ensure it's an empty cell
                self.grid[row][col] = 2  # Place an apple
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
