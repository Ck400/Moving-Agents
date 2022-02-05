import pygame
import Constants
import Player
import Enemy
import random

from pygame.locals import *
from Player import *
from Enemy import *

# Initialize pygame
pygame.init()

# Setup variables
run = True
game_display = pygame.display.set_mode((Constants.DISPLAY_WIDTH, Constants.DISPLAY_HEIGHT))
pygame.display.set_caption('Moving Agents')
clock = pygame.time.Clock()

enemies = []
player = Player(Vector(Constants.DISPLAY_WIDTH/2 - Constants.PLAYER_SIZE/2, Constants.DISPLAY_HEIGHT/2 - Constants.PLAYER_SIZE/2), Constants.PLAYER_SIZE, Constants.PLAYER_MOVESPEED)

for num in range(Constants.ENEMY_COUNT):
    enemy = Enemy(Vector(random.randrange(0, Constants.DISPLAY_WIDTH - Constants.ENEMY_SIZE/2), random.randrange(0, Constants.DISPLAY_HEIGHT - Constants.ENEMY_SIZE/2)), Constants.ENEMY_SIZE, Constants.ENEMY_MOVESPEED)
    enemies.append(enemy)

# Main Game Loop
while run:

    clock.tick(Constants.FRAME_RATE)

    # Paint over screen to refresh it
    game_display.fill(Constants.BACKGROUND_COLOR)

    # If the player hits the x button exit loop
    for event in pygame.event.get():

        if event.type == QUIT:
            run = False

    for enemy in enemies:
        enemy.draw(enemy.update(player), game_display, Constants.MOVE_VECTOR_DIR_LENG)
        
    player.draw(player.update(enemies), game_display, Constants.MOVE_VECTOR_DIR_LENG)

    # Flip display
    pygame.display.flip()
    
# Exit pygame
pygame.quit()