import random
NUM_ROWS = 4
NUM_COLS = 4
"""
grid:
[[0,0,0,0],
[0,0,0,0],
[0,0,1,0],
[0,0,0,0]]

grid[2] == [1,2,3,4]
grid[2][2] == 3
"""

# create a 2d array of NUM_ROWS x NUM_COLS
grid = []
for _ in range(NUM_ROWS): # [0, 1, .., NUM_ROWS- 1]
    grid.append([0] * NUM_COLS)
    
# set the initial snake position in the center of the grid
grid[2][2] = 1


# Let's try the following
# print(f"use print:\n")
# print(grid)
# It's not very easy to read. Let's define a function to print the 2d grid in a human-readable format
# define a function to print the 2d grid in a human-readable format
def print_grid(grid):
    """For example:
    >>> print_grid([[0, 0], [0, 0]])
    [[0, 0],
    [0, 0]]
    >>> print_grid([[0, 0], [0, 0, 0], [0, 0, 0, 0]])
    [[0, 0],
    [0, 0, 0],
    [0, 0, 0, 0]]
    """
    # HINT: use a for loop to print each row
    # for loop: for __ in __:
    for row in grid:
        print(row)

# print(f"using function print_grid:\n")
# print_grid(grid)

# define a function that can let the snake move up, down, left, or right
snake_body = [(2, 2)] # list[tuple[int, int]]
# the first element of snake_body is the head of the snake. the last element of snake_body is the tail of the snake
def move(grid, direction):
    # HINT: how many cases do you need to consider?
    # insert new snake head
    # pop out the snake tail
    """for example:
    >>> snake_body = [(1,1)]
    >>> move([[0,0], [0,1]], 'left')
    True
    
    more examples:
    >>> move([[0,0], [0,1]], 'down') # out of boundary
    False

    >>> move([[0,0], [2,1]], 'left') # ate apple
    True # also update apples && do not remove tail away from snake_body
   
    >>> snake_body = [(1, 1), (1, 0)] 
    >>> move([[0,0],[1,1]], 'left') # snake hits itself
    False 
    """
    head = snake_body[0] # tuple[int, int]
    if direction == 'up':
        new_head = (head[0] - 1, head[1])
        snake_body.insert(0, new_head) # lst.insert(index_to_insert, element_to_insert)
    elif direction == 'down':
        new_head=(head[0]+1, head[1])
        snake_body.insert(0, new_head)
    elif direction == 'left':
        new_head=(head[0], head[1]-1)
        snake_body.insert(0, new_head)
    elif direction == 'right':
        new_head=(head[0], head[1]+1)
        snake_body.insert(0, new_head)
    else: # none of directions above
        print("Error! The input direction is not in ['up'. 'down', 'left', 'right']")
    tail = snake_body.pop()
    # update the grid based on snake_body:
    grid[new_head[0]][new_head[1]] = 1  # make grid's new_head position to be 1:
    grid[tail[0]][tail[1]] = 0 # make grid's tail position to be 0

"""Uncomment what's below to see if your function works"""
# uncomment: mac: cmd + /
    # windows: ctrl + / 
# print_grid(grid)
# print("\n")
# move(grid, 'down')
# print_grid(grid)
# print("\n")

# move(grid, 'right')
# move(grid, 'up')
# print_grid(grid)
# print("\n")

# Or we can use a directory to simplify the move function
def move_simplified(grid, direction):
    directions = {
        'up': (-1, 0),
        'down': (1, 0),
        'left': (0, -1),
        'right': (0, 1)
    }
    if direction not in directions:
        print("Error! invalid direction to move")
        return
    row_change, col_change = directions[direction]
    head = snake_body[0]
    new_head = (head[0]+row_change, head[1] + col_change)
    snake_body.insert(0, new_head)
    grid[new_head[0]][new_head[1]] = 1
    tail = snake_body.pop()
    grid[tail[0]][tail[1]] = 0
      

# write a function that gives random direction
def random_direction():
    """Return a random direction: 'up', 'down', 'left', 'right
    >>> random_direction()
    'up'
    >>> random_direction()
    'down'
    '"""
    # HINT: use random.choice
    # Read the documentation to learn random.choice: https://www.w3schools.com/python/ref_random_choice.asp
    return random.choice(['up', 'down', 'right', 'left'])

apples = [] # a list of tuple[int, int] to record which grid coordinate is apples
# write a function that randomly place 1 apple on the grid
def place_apple(grid):
    """Randomly place 1 apple on the grid. Update the list apples"""
    # HINT: use random.randint
    # Read the documentation: https://www.w3schools.com/python/ref_random_randint.asp
    while True:
        row = random.randint(0, NUM_ROWS - 1)
        col = random.randint(0, NUM_COLS - 1)
        if grid[row][col] == 0:  # Ensure it's an empty cell
            grid[row][col] = 2  # Place an apple
            apples.append((row, col))
            break

# Uncomment following code by delete """. The code below make 2 random moves on grid:
"""
grid = []
for _ in range(NUM_ROWS): # [0, 1, .., NUM_ROWS- 1]
    grid.append([0] * NUM_COLS)
grid[2][2] = 1
snake_body = [(2, 2)]
print("grid at the begining:")
print_grid(grid)
for s in range(2):
    direct = random_direction()
    move_simplified(grid, direct)
    print(f"take the random direction: {direct}")
    print(f"the grid after {direct}:")
    print_grid(grid)
"""


# TODO: let's go back to move_simplifed() or move() function, check if the snake goes out of the boundary
# if out of boundary, move function return false.
# TODO: go back to move_simplifed() or move() function, check if the snake hits itself
# if snake hits itself, move function return false.
# TODO: go back to move_simplifed() or move() function, check if the snake hits apple
# if snake hits apples, what should we do?
# TODO: go back to move_simplifed() or move() function, check if none of the cases above,
# return true.


# Lecture 2: Why not put all the functions in a class?
#TODO for lec2: combine all of them into a class
