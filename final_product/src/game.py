from ui import GameBoard, GamePanel, RestartButton
import pygame
from setting import SCREEN_WIDTH, SCREEN_HEIGHT, BLACK

class SnakeGame:
    game_panel: GamePanel
    game_board: GameBoard
    restart_button: RestartButton
    is_game_over: bool
    score: int
    mode: str # either "human" or "auto"
    surface: pygame.Surface
    def __init__(self, surface, mode = "human"):
        self.mode = mode
        self.is_game_over = False
        self.surface = surface
        self.game_board = GameBoard(surface, mode)
        self.game_panel = GamePanel(surface)
        self.restart_button = RestartButton(surface)
        self.score = 0
    
    def update(self, event: str):
        self.game_board.update(event)
        if self.game_board.is_game_over():
            self.is_game_over = True
        self.score = self.game_board.get_score()
        
    
    def draw(self):
        self.game_panel.draw(self.score)
        self.game_board.draw()
        self.restart_button.draw()
        if self.is_game_over:
            self._draw_game_over()
    
    def restart(self):
        self.game_board = GameBoard(self.surface, self.mode)
        self.is_game_over = False
        self.score = 0

    def _draw_game_over(self):
        """Draws the Game Over message on the screen."""
        game_over_font = pygame.font.Font(None, 100)  # Larger font for Game Over
        game_over_text = game_over_font.render('GAME OVER', True, BLACK)
        
        # Center the text on the gameboard
        text_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
        self.surface.blit(game_over_text, text_rect)