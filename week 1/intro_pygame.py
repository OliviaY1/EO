import pygame

# Initialize Pygame
pygame.init()

# Set up the window dimensions
WINDOW_WIDTH = 600   # Width of the window in pixels
WINDOW_HEIGHT = 700   # Height of the window in pixels

# Create the window
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Pygame Introduction - EO')

# Define colors
# RGB color for yellow
YELLOW = (255, 255, 0)
# HEX color example (e.g., #FF5733)
HEX_COLOR = (0x10, 0xFF, 0x33) # Green

# Define circle properties
circle_position = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)  # Center of the window
circle_radius = 50                                         # Radius of the circle in pixels

# Main loop flag
running = True

# Main loop
while running:
    # Handle events (e.g., window close, key presses)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white color
    window.fill((255, 255, 255))

    # Draw the circle using the yellow color
    pygame.draw.circle(window, YELLOW, circle_position, circle_radius)

    # TODO: use hex color to draw the circle
    # find more hex color from https://imagecolorpicker.com/color-code/15b5ef
    pygame.draw.circle(window, HEX_COLOR, circle_position, circle_radius)
    pygame.draw.circle(window, "#07aaff", circle_position, circle_radius)

    # TODO: look at the web, try to draw some other shape with your fav color: https://www.pygame.org/docs/ref/draw.html
    pygame.draw.ellipse(window, YELLOW, pygame.Rect(10, 10, 100, 50))
    # Update the display to show the drawn circle
    pygame.display.flip()

# Quit Pygame when the main loop ends
pygame.quit()
