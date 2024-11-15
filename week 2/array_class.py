import random

class ArrayGameBoard:
    grid: list[list[int]] # list[xxx]
    apples: list[tuple[int, int]]
    snake_body: list[tuple[int, int]]
    is_game_over: bool # True | False

    grid_size: tuple[int, int] # (height, width)
    """is_game_over == False when the game is not over. == True when the game is over"""
    def __init__(self, num_row, num_col): # method
        self.grid_size = (num_row, num_col)
        # initialize grid
        self.grid = []
        for _ in range(num_row): # [0, 1, .., NUM_ROWS- 1]
            self.grid.append([0] * num_col)
        
        # initialzie snake body: default snake head is the center of the grid
        self.grid[num_row // 2][num_col // 2] = 1 
        self.snake_body = [(num_row // 2, num_col // 2)]

        self.apples = []
        # place 2 random apples
        self.place_apple()
        self.place_apple()
    
    def __str__(self):
        for row in self.grid:
            print(row)
        return ""


    def move(self, direction):
        """Return if the snake moves to a valid position on the grid
        invalid:
            - out of boundary
            - snake hits itself
        """
        directions = {
            'up': (-1, 0), # (row, col)
            'down': (1, 0), 
            'left': (0, -1),
            'right': (0, 1)
        } # change in rows and cols
        if direction not in directions:
            print("Error! invalid direction to move")
            return
        row_change, col_change = directions[direction]
        head = self.snake_body[0]
        new_head = (head[0]+row_change, head[1] + col_change)
        
        num_row = self.grid_size[0]
        num_col = self.grid_size[1]
        if 0 <= new_head[0] < num_row or 0 <= new_head[1] < num_col:
            # we are within the boundary
            # snake hit itself:
            if new_head in self.snake_body: # snake hits itself
                print("snake hits itself")
                self.is_game_over = True
                return False
            elif new_head in self.apples: # snake eat the apple
                # we insert snake body
                self.snake_body.insert(0, new_head)
                # do not pop the tail
                self.grid[new_head[0]][new_head[1]] = 1 # update grid
                # remove a hit apple from apples
                self.apples.remove(new_head)
                # place a random apple in grid
                self.place_apple()
                return True
            else: # u goes to an empty slot
                self.snake_body.insert(0, new_head) # update snake_body
                self.grid[new_head[0]][new_head[1]] = 1 # update grid
                tail = self.snake_body.pop() 
                self.grid[tail[0]][tail[1]] = 0 # update grid
                return True
        else:
            print("you are out of boundary now")
            self.is_game_over = True
            return False

    def place_apple(self):
        """Randomly place 1 apple on the grid. Update the list apples"""
        # HINT: use random.randint
        # Read the documentation: https://www.w3schools.com/python/ref_random_randint.asp
        while True:
            row = random.randint(0, self.grid_size[0] - 1) # random.randint(0,10) Q: 2.3? 10? 0? inclusively
            col = random.randint(0, self.grid_size[1] - 1)
            if self.grid[row][col] == 0:  # Ensure it's an empty cell
                self.grid[row][col] = 2  # Place an apple
                self.apples.append((row, col)) # update list of apples
                break

# create an object of ArrayGameBoard:
game = ArrayGameBoard(4, 4) # num_row: 4, num_col: 4
print(game) # the default __str__ gives the data type of game
game.move("right")
print(game)