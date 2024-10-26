"""Week1. Introduction to Pygame
Pygame is a Python library that is used to create video games.
Pygame provides a set of functions that allow you to create games and multimedia applications (such as playing sounds)
In this week's assignment, you will learn how to use Pygame to create a simple game."""
import pygame 

def main():
    pygame.init()
    SCREEN_WIDTH = ...
    SCREEN_HEIGHT = ...
    surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("FILL WITH YOUR GAME NAME ... ")

    running = True
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get(): # TODO: Q: What are some posssible events players could trigger?
            if event.type == pygame.QUIT:
                running = False
            # TODO: Try to add more events here
        ...
        pygame.display.flip()  # Update the screen
        clock.tick(30)  # 30 FPS (Frame per second)
    pygame.quit()

if __name__ == "__main__":
    main()