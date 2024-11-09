import pygame
from setting import SCREEN_WIDTH, SCREEN_HEIGHT, WHITE, RED, BLACK, GRAY, BEIGE, LIGHT_BLUE, GRID_SIZE, SCOREBOARD_HEIGHT, MARGIN, NUM_COLS, NUM_ROWS, GRID_WIDTH, GRID_HEIGHT
from array_class import ArrayGameBoard


pygame.font.init()
FONT = pygame.font.Font(None, 36)  # Default font, size 36, 

class GameBoard:
    gameboard: ArrayGameBoard # This is related to the array.py
    mode: str # either "human" or "auto"
    surface: pygame.Surface
    apple_image: pygame.Surface
    rect: pygame.Rect # the rect referring to the whole gameboard 

    def __init__(self, surface): # default mode is "human"
        self.surface = surface
        self.gameboard = ArrayGameBoard(NUM_ROWS, NUM_COLS)  # Get the initial gameboard state

        # used for drawing the grid
        self.grid_length =  min((SCREEN_WIDTH - 2 * MARGIN) // NUM_COLS, (SCREEN_HEIGHT - SCOREBOARD_HEIGHT - MARGIN) // NUM_ROWS)
        self.width = self.grid_length * NUM_COLS
        self.height = self.grid_length * NUM_ROWS
        self.margin_width = (SCREEN_WIDTH - self.width) // 2
        self.margin_height = (SCREEN_HEIGHT - SCOREBOARD_HEIGHT - self.height) // 2

        self.rect = pygame.Rect(self.margin_width, self.margin_height, self.width, self.height)  # Game area dimensions

        # load apple's image
        self.apple_image = pygame.image.load('final_product/assets/apple.png')
        self.apple_image = pygame.transform.scale(self.apple_image, (self.grid_length, self.grid_length))

    def array_to_pixel(self, row, col):
        """Converts 2d array coordinates to pixel coordinates on the image.
        returned value: x, y is the pixel coordinates of the topleft point of the grid (row, col)
        """
        x = self.margin_width + col * self.grid_length
        y = self.margin_height + row * self.grid_length
        return x, y

    def draw(self):
        """Draws the gameboard with beige background, grid lines, and black border."""
        pygame.draw.rect(self.surface, BEIGE, self.rect)
        # TODO: Draw the self.rect on self.surface with BEIGE color
        # TODO: Draw the self.rect's black borders

        # use self.gameboard to draw the grid
        for row in range(NUM_ROWS):
            for col in range(NUM_COLS):
                # TODO: given (row, col), find its pixel coordinates on self.surface
                # TODO: create a rect to represent the grid (row, col) on the canvas, knowing its size is (self.grid_length * self.grid_length

                # TODO: draw the rect on self.surface. Its color depends on the if this grid represents an apple / snake body / nothing
                # HINT: use self.gameboard.get_grid()
                if self.gameboard.get_grid()[row][col] == 1:
                    # TODO: what to do?
                    ...
                elif self.gameboard.get_grid()[row][col] == 0:
                    ...
                elif self.gameboard.get_grid()[row][col] == 2:
                    # pygame.draw.rect(self.surface, RED, grid_rect)
                    # TODO: use blit on self.surface to project the image of self.apple_image on this position
                    ...

    def update(self, move: str):
        """Given a move (such as "up", "down"), updates the gameboard"""
        self.gameboard.move(move)
    
    def is_game_over(self):
        """Returns True if the game is over."""
        return self.gameboard.is_game_over
    
    def get_score(self):
        """Returns the current score."""
        return self.gameboard.get_score()


class RestartButton:
    surface: pygame.Surface
    rect: pygame.Rect
    def __init__(self, surface):
        self.surface = surface
        self.rect = pygame.Rect(SCREEN_WIDTH - 170, SCREEN_HEIGHT - SCOREBOARD_HEIGHT + 20, 120, 50)

    def draw(self):
        """Draws the restart button on the screen."""
        # TODO: draw self.rect on self.surface
        pygame.draw.rect(self.surface, BEIGE, self.rect)
        # TODO: draw self.rect's black border on self.surface. Adjust the border thickness
        # TODO: render a font with string "RESTART" on the screen, choose color you like
        # TODO: use blit on self.surface so that the font shows
        

    def is_clicked(self, mouse_pos):
        """Given the mouse_pos, Checks if the button is clicked."""
        # TODO: use collidepoint to check if self.rect collide the mouse_pos
        # QUESTION: what would mouse_pos be here? 
        return False
        
class GamePanel:
    surface: pygame.Surface
    def __init__(self, surface):
        self.surface = surface

    def draw(self, score: int):
        """Draws the game panel, which includes the gameboard, score, and restart button."""
        # TODO: Fill self.surface with color LIGHT_BLUE
        # TODO: use _draw_score() to draw the score on the self.surface
        ...

    def _draw_score(self, score):
        """Draws the score at the bottom of the screen."""
        # TODO: put the text you want into FONT.render
        score_text = FONT.render("placeholder", True, BLACK)
        self.surface.blit(score_text, (20, SCREEN_HEIGHT - SCOREBOARD_HEIGHT + 30))
    
if __name__=="__main__":
    pygame.init()
    surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("EO: Snake Game")

    clock = pygame.time.Clock()
    running = True
    game_panel = GamePanel(surface)
    restart_button = RestartButton(surface)
    game_board = GameBoard(surface)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if restart_button.is_clicked(event.pos):
                    print("RESTART THE GAME!")
            elif event.type == pygame.KEYDOWN:
                # TODO: when the key is clicked, What to do!
                # HINT: use game_board.update()
                if event.key == pygame.K_UP:
                    print("up clicked")
                elif event.key == pygame.K_DOWN:
                    print("down clicked")
                elif event.key == pygame.K_LEFT:
                    print("left clicked")
                elif event.key == pygame.K_RIGHT:
                    print("right clicked")
        # TODO: the order of game_panel, game_board matters. Try to swtich the order and see what may happen!
        game_panel.draw(game_board.get_score())
        game_board.draw()
       
        restart_button.draw()
        pygame.display.flip()  # Update the display/canvas
        clock.tick(30)  # 30 FPS

    pygame.quit()