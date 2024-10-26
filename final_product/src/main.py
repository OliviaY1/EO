import pygame
from setting import SCREEN_WIDTH, SCREEN_HEIGHT
from game import SnakeGame

# Define a new event for the snake's automatic movement
MOVE_EVENT = pygame.USEREVENT + 1

MODE = "auto"  # Set the mode to "auto" for automatic snake movement
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("EO: Snake Game")

    clock = pygame.time.Clock()
    running = True
    # game_panel = GamePanel(screen, MODE)
    game = SnakeGame(screen, MODE)
    # Set up a timer to trigger MOVE_EVENT every 1000 milliseconds (1 second)
    pygame.time.set_timer(MOVE_EVENT, 100)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if game.restart_button.is_clicked(event.pos):
                    print("button clicked.")
                    game.restart()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    game.update('up')
                elif event.key == pygame.K_DOWN:
                    game.update('down')
                elif event.key == pygame.K_LEFT:
                    game.update('left')
                elif event.key == pygame.K_RIGHT:
                    game.update('right')
            elif event.type == MOVE_EVENT:
                if not game.is_game_over:
                    # Automatically move the snake in the current direction every 1 second
                    game.update('current_direction')
        game.draw()
        pygame.display.flip()  # Update the display/canvas
        clock.tick(30)  # 30 FPS

    pygame.quit()

if __name__ == "__main__":
    main()
