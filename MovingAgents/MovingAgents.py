import pygame
import Constants

from pygame.locals import *

# Initialize pygame
pygame.init()

# Setup variables
quit = 1
game_display = pygame.display.set_mode((Constants.DISPLAY_WIDTH, Constants.DISPLAY_HEIGHT))
pygame.display.set_caption('Moving Agents')
clock = pygame.time.Clock()

# Main Game Loop
while quit:

    clock.tick(Constants.FRAME_RATE)

    # Paint over screen to refresh it
    game_display.fill((100,149,237))

    # If the player hits the x button exit loop
    for event in pygame.event.get():

        if event.type == QUIT:
            quit = 0

    # Flip display
    pygame.display.flip()
    
# Exit pygame
pygame.quit()