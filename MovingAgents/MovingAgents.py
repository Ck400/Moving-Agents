import pygame
import Constants
import Player

from pygame.locals import *
from Player import *

# Initialize pygame
pygame.init()

# Setup variables
quit = 1
game_display = pygame.display.set_mode((Constants.DISPLAY_WIDTH, Constants.DISPLAY_HEIGHT))
pygame.display.set_caption('Moving Agents')
clock = pygame.time.Clock()

enemies = []
player = Player(Vector(Constants.DISPLAY_WIDTH/2, Constants.DISPLAY_HEIGHT/2), Constants.PLAYER_SIZE, Constants.PLAYER_MOVESPEED)

# Main Game Loop
while quit:

    clock.tick(Constants.FRAME_RATE)

    # Paint over screen to refresh it
    game_display.fill(Constants.BACKGROUND_COLOR)

    # If the player hits the x button exit loop
    for event in pygame.event.get():

        if event.type == QUIT:
            quit = 0

    print(player)
    player.draw(player.update(enemies), game_display, Constants.MOVE_VECTOR_DIR_LENG)

    # Flip display
    pygame.display.flip()
    
# Exit pygame
pygame.quit()