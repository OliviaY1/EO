NUM_ROWS = ...
NUM_COLS = ...

# TODO: create a 2d array of NUM_ROWS x NUM_COLS
grid = ...

# TODO: set the initial snake position in the center of the grid
grid[...][...] = 1

# Let's try the following
print(grid)
# It's not very easy to read. Let's define a function to print the 2d grid in a human-readable format
# TODO: define a function to print the 2d grid in a human-readable format
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
    ...

# TODO: define a function that can let the snake move up, down, left, or right
def move(grid, direction):
    # HINT: how many cases do you need to consider?
    ...

"""Uncomment what's below to see if your function works"""
# print_grid(grid)
# move(grid, 'down')
# print_grid(grid)
# move(grid, 'right')
# move(grid, 'up')
# print_grid(grid)

# Or we can use a directory to simplify the move function
def move_simplified(direction):
    ...

# Use same way to test if your code works   


# we place some apple on the grid
def place_apple(grid):
    ...

# let's go back to move function, check if the snake goes out of the boundary

# Why not put all the functions in a class?
#TODO: combine all of them into a class
