import pygame
from setting import SCREEN_WIDTH, SCREEN_HEIGHT, WHITE, RED, BLACK, GRAY, BEIGE, LIGHT_BLUE, GRID_SIZE, SCOREBOARD_HEIGHT, MARGIN, NUM_COLS, NUM_ROWS, GRID_WIDTH, GRID_HEIGHT
from array import ArrayGameBoard

pygame.font.init()
FONT = pygame.font.Font(None, 36)  # Default font, size 36

class GameBoard:
    gameboard: ArrayGameBoard
    
    def __init__(self, surface, mode = "human"):
        self.mode = mode
        self.surface = surface
        self.gameboard = ArrayGameBoard(NUM_ROWS, NUM_COLS)  # Get the initial gameboard state

        # used for drawing the grid
        self.grid_length =  min((SCREEN_WIDTH - 2 * MARGIN) // NUM_COLS, (SCREEN_HEIGHT - SCOREBOARD_HEIGHT - MARGIN) // NUM_ROWS)
        self.width = self.grid_length * NUM_COLS
        self.height = self.grid_length * NUM_ROWS
        self.margin_width = (SCREEN_WIDTH - self.width) // 2
        self.margin_height = (SCREEN_HEIGHT - SCOREBOARD_HEIGHT - self.height) // 2

        self.rect = pygame.Rect(self.margin_width, self.margin_height, self.width, self.height)  # Game area dimensions

        self.apple_image = pygame.image.load('final_product/assets/apple.png')
        self.apple_image = pygame.transform.scale(self.apple_image, (self.grid_length, self.grid_length))

    def array_to_pixel(self, row, col):
        """Converts 2d array coordinates to pixel coordinates.
        x, y is the topleft of the grid"""
        x = self.margin_width + col * self.grid_length
        y = self.margin_height + row * self.grid_length
        return x, y

    def draw(self):
        """Draws the gameboard with beige background, grid lines, and black border."""
        pygame.draw.rect(self.surface, BEIGE, self.rect) # beige background
        pygame.draw.rect(self.surface, BLACK, self.rect, 3) # black border

        # use self.gameboard to draw the grid
        for row in range(NUM_ROWS):
            for col in range(NUM_COLS):
                grid_pixel_coord = self.array_to_pixel(row, col)
                grid_rect = pygame.Rect(grid_pixel_coord[0], grid_pixel_coord[1], self.grid_length, self.grid_length)
                # pygame.draw.rect(self.surface, GRAY, grid_rect, 1)
                if self.gameboard.get_grid()[row][col] == 1:
                    pygame.draw.rect(self.surface, BLACK, grid_rect)
                elif self.gameboard.get_grid()[row][col] == 0:
                    pygame.draw.rect(self.surface, GRAY, grid_rect, 1)
                elif self.gameboard.get_grid()[row][col] == 2:
                    # pygame.draw.rect(self.surface, RED, grid_rect)
                    self.surface.blit(self.apple_image, grid_pixel_coord)

    def update(self, move: str):
        """Updates the gameboard based on the move."""
        if self.mode == "human":
            self.gameboard.move(move)
        elif self.mode == "auto":
            ai_move = self.gameboard.greedy_best_first_search()
            self.gameboard.move(ai_move)
    
    def is_game_over(self):
        """Returns True if the game is over."""
        return self.gameboard.is_game_over
    
    def get_score(self):
        """Returns the current score."""
        return self.gameboard.get_score()


class RestartButton:
    def __init__(self, surface):
        self.surface = surface
        self.rect = pygame.Rect(SCREEN_WIDTH - 170, SCREEN_HEIGHT - SCOREBOARD_HEIGHT + 20, 120, 50)

    def draw(self):
        """Draws the restart button on the screen."""
        pygame.draw.rect(self.surface, BEIGE, self.rect)
        pygame.draw.rect(self.surface, BLACK, self.rect, 2)
        button_text = FONT.render('RESTART', True, BLACK)
        self.surface.blit(button_text, (SCREEN_WIDTH - 160, SCREEN_HEIGHT - SCOREBOARD_HEIGHT + 30))

    def is_clicked(self, mouse_pos):
        """Checks if the button is clicked."""
        return self.rect.collidepoint(mouse_pos)
    
class GamePanel:
    def __init__(self, surface):
        self.surface = surface

    def draw(self, score: int):
        """Draws the game panel, which includes the gameboard, score, and restart button."""
        # Fill the entire screen with light blue background
        self.surface.fill(LIGHT_BLUE)

        # Draw the score
        self._draw_score(score)

    def _draw_score(self, score):
        """Draws the score at the bottom of the screen."""
        score_text = FONT.render(f'SCORE: {score}', True, BLACK)
        self.surface.blit(score_text, (20, SCREEN_HEIGHT - SCOREBOARD_HEIGHT + 30))
    