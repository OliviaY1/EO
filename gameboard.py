import pygame
WHITE = (255, 255, 255)   # Color for empty cells (0)
BLACK = (0, 0, 0)         # Color for snake body (1)
RED = (255, 0, 0)         # Color for rewards or obstacles (-1)
CELL_SIZE = 30     # Size of each cell in pixels

class GameBoard:
    # game_board_size: (width, height)
    # game_board: list[list[int]]
    # snake_body: list[tuple[int, int]]
    #rewards: list[tuple[int, int]]
    def __init__(self, width: int, height: int) -> None:
        # initialize a game board
        self.game_board = [[0 for x in range(width)] for y in range(height)]
        self.game_board_size = (width, height)
        self.snake_body = [(height // 2, width//2)]
        self.rewards = [(1, 2)]
        # TODO: add score attribute

    def _update_rewards(self):
        for s in self.rewards:
            self.game_board[s[0]][s[1]] = -1

    def _update_snake(self):
        for s in self.snake_body: # s: (row index, col index)
            self.game_board[s[0]][s[1]] = 1

    def update_board(self):
        # update board
        self.game_board = [[0 for x in range(self.game_board_size[0])] for y in range(self.game_board_size[1])]
        self._update_snake()
        self._update_rewards()
    
    def move(self, direction: str) -> bool: # return if move successfully
        snake_head = self.snake_body[0]
        if direction == "up":
            snake_head_after_move = (snake_head[0] - 1, snake_head[1])
        elif direction == "down":
            # TODO: complete me
            ...
        elif direction == "right":
            # TODO: complete me
            ...
        elif direction == "left":
            # TODO: complete me
            ...
        else:
            print("not correct direction")
        if self.out_of_bound(snake_head_after_move):
            return False
        self.snake_body.insert(0, snake_head_after_move)
        if not self.get_reward_and_eat():
            self.snake_body.pop() # pop out the last element
            print(self.snake_body)
        return True
    
    def get_reward_and_eat(self) -> bool:
        snake_head = self.snake_body[0]
        got_reward = snake_head in self.rewards
        if got_reward:
            self.rewards.remove(snake_head)
        return got_reward
    
    def out_of_bound (self, pos: tuple[int, int]) -> bool:
        width, height = self.game_board_size[0], self.game_board_size[1]
        return pos[0] >= width or pos[0] < 0 or pos[1] >= height or pos[1] < 0 
    

    def draw(self, window): # draw on pygame canvs:
        # Function to draw the game board
        width, height = self.game_board_size[0], self.game_board_size[1]
        for row in range(height):
            for col in range(width):
                cell_value = self.game_board[row][col]
                # Determine the color based on the cell value
                if cell_value == 0:
                    color = WHITE
                elif cell_value == -1:
                    color = RED
                elif cell_value == 1:
                    color = BLACK
                else:
                    color = WHITE  # Default to white if unknown value
                # Calculate the rectangle for the cell
                rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                # Draw the cell
                pygame.draw.rect(window, color, rect)
                # Optional: Draw grid lines (in light gray)
                pygame.draw.rect(window, (200, 200, 200), rect, 1)  # Border width of 1 pixel

    
