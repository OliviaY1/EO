# Save all the settings for the game
# You can call these constants as MACROS

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Common Used Colors. You can try to modify the numbers to see the effect
# Remeber the number needs to be in the range [0, 255] inclusive
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
BLUE = (173, 216, 230)
RED = (255, 0, 0)
BEIGE = (245, 245, 220)  # Beige color for gameboard and restart button
LIGHT_BLUE = (173, 216, 230)  # Light blue color for the background

# Grid/Pixels settings
# The minimum component of a screen is a pixel. We can use pixels to create a grid
GRID_SIZE = 20    # 20 pixels for each grid
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE

# Gameboard settings
NUM_ROWS = 15  # Number of rows in the gameboard
NUM_COLS = 20  # Number of columns in the gameboard

MARGIN = 20  # Margin of the gameboard from the screen edge

# UI settings
SCOREBOARD_HEIGHT = 100
