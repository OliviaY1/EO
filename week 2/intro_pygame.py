"""Week2. Introduction to Pygame
Pygame is a Python library that is used to create video games.
Pygame provides a set of functions that allow you to create games and multimedia applications (such as playing sounds)
In this week's assignment, you will learn how to use Pygame to create a simple game."""
import pygame 

def main():
    pygame.init()
    SCREEN_WIDTH = ...
    SCREEN_HEIGHT = ...
    window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("FILL WITH YOUR GAME NAME ... ")

    running = True
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get(): # TODO: Q: What are some posssible events players could trigger?
            if event.type == pygame.QUIT:
                running = False
            # TODO: Try to add event MOUSEBUTTONUP, and print out the cooridnate of clicked mouse
            # TODO: Try to add event KEYDOWN, print out the key user pressed
        ...
        name = "olivia"
        x = f"Hello! my name is {name}"
        # TODO: given string x, draw x on the window

        # TODO: draw a rectangle on the window with the color you like
        # read the documentation to see how to do: https://www.pygame.org/docs/ref/draw.html#pygame.draw.rect


        pygame.display.flip()  # Update the screen
        clock.tick(30)  # 30 FPS (Frame per second)
    pygame.quit()

if __name__ == "__main__":
    main()