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

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
PINK = (255, 105, 180)
RED = (255, 0, 0)
MOUTH = (255, 184, 166)
PI = 3.141592653

# Speed in pixels per frame
x_speed = 0
y_speed = 0

# Current position
x_coord = 10
y_coord = 10

ball_pos = 0
ball_change = 1


def draw_stick_figure(screen, x, y):
    pygame.draw.ellipse(screen, RED, [20 + x, 130 + ball_pos + y, 40, 40])
    pygame.draw.circle(screen, PINK, [180 + x, 140 + y], 100)
    pygame.draw.line(screen, WHITE, [150 + x, 50 + y], [150 + x, 100 + y], 5)
    pygame.draw.line(screen, WHITE, [200 + x, 50 + y], [200 + x, 100 + y], 5)
    pygame.draw.line(screen, WHITE, [80 + x, 130 + y], [20 + x, 130 + y], 5)
    pygame.draw.line(screen, WHITE, [275 + x, 130 + y], [335 + x, 130 + y], 5)
    pygame.draw.line(screen, WHITE, [100 + x, 200 + y], [50 + x, 280 + y], 5)
    pygame.draw.line(screen, WHITE, [260 + x, 200 + y], [315 + x, 280 + y], 5)
    pygame.draw.ellipse(screen, MOUTH, [140 + x, 140 + y, 75, 50])
    pygame.draw.line(screen, WHITE, [175 + x, 115 + y], [175 + x, 105 + y], 5)



# Loop as long as done == False
while not done:
    ball_pos += ball_change
    if ball_pos > 130:
        ball_change -= 1
    elif ball_pos < 100:
        ball_change += 1
    # User did something
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x_speed = -3
    if keys[pygame.K_RIGHT]:
        x_speed = 3
    if keys[pygame.K_UP]:
        y_speed = -3
    if keys[pygame.K_DOWN]:
        y_speed = 3

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop

    # Move the object according to the speed vector.
    x_coord += x_speed
    y_coord += y_speed

    # Reset x_speed and y_speed for the next frame
    x_speed = 0
    y_speed = 0

    screen.fill(BLACK)

    draw_stick_figure(screen, x_coord, y_coord)

    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.flip()

    # This limits the while loop to a max of 60 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(60)

# Be IDLE friendly
pygame.quit()

