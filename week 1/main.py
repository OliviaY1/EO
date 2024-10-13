import gameboard
import pygame
WHITE = (255, 255, 255)   # Color for empty cells (0)
BLACK = (0, 0, 0)         # Color for snake body (1)
RED = (255, 0, 0)         # Color for rewards or obstacles (-1)
CELL_SIZE = 30     # Size of each cell in pixels


WIDTH = 5
HEIGHT = 5

a = gameboard.GameBoard(WIDTH, HEIGHT)


pygame.init()
window_width = WIDTH * CELL_SIZE
window_height = HEIGHT * CELL_SIZE
window = pygame.display.set_mode((window_width, window_height))

# Main loop
running = True
clock = pygame.time.Clock()
FPS = 25

while running:
    # Handle events (e.g., window close)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background (optional)
    window.fill(WHITE)

    # Draw the game board
    a.update_board()
    a.draw(window)

    # Update the display
    pygame.display.flip()
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
