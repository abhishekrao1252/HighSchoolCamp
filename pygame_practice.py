"""
title: pygame_practice
author: Abhishek Rao
date: 2019-06-14 09:53
"""

# Import a library of functions called 'pygame'
import pygame

# Initialize the game engine
pygame.init()

# Set the height and width of the screen
size = (400, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("First Pygame")

# Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()

# Loop as long as done == False
while not done:

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    PINK =(255, 105, 180)
    RED = (255, 0, 0)
    MOUTH = (255, 184, 166)
    PI = 3.141592653
    pygame.draw.circle(screen, PINK, [180, 140], 100)
    pygame.draw.line(screen, WHITE, [150, 50], [150, 100], 5)
    pygame.draw.line(screen, WHITE, [200, 50], [200, 100], 5)
    pygame.draw.line(screen, WHITE, [80, 130], [20, 130], 5)
    pygame.draw.line(screen, WHITE, [275, 130], [335, 130], 5)
    pygame.draw.line(screen, WHITE, [100, 200], [50, 280], 5)
    pygame.draw.line(screen, WHITE, [260, 200], [315, 280], 5)
    pygame.draw.ellipse(screen, MOUTH, [140, 140, 75, 50])
    pygame.draw.line(screen, WHITE, [175, 115], [175, 105], 5)


    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.flip()

    # This limits the while loop to a max of 60 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(60)

# Be IDLE friendly
pygame.quit()

