import pygame
import Dog
import Enemy

from pygame.locals import *
from Dog import *
from Enemy import *

# Initialize pygame
pygame.init()

test = Vector(8,2)

print(test.dot(Vector(2,8)))

# Setup variables
run = True
game_display = pygame.display.set_mode((Constants.DISPLAY_WIDTH, Constants.DISPLAY_HEIGHT))
pygame.display.set_caption('Driving Sheep')
clock = pygame.time.Clock()

# Setup agents
enemies = []
dog = Dog(Vector(Constants.DISPLAY_WIDTH/2 - Constants.DOG_SIZE.x/2, Constants.DISPLAY_HEIGHT/2 - Constants.DOG_SIZE.y/2), Constants.DOG_SIZE, Constants.DOG_MOVESPEED)

for num in range(Constants.SHEEP_COUNT):
    enemy = Enemy(Vector(random.randrange(0, Constants.DISPLAY_WIDTH - Constants.SHEEP_SIZE.x/2), random.randrange(0, Constants.DISPLAY_HEIGHT - Constants.SHEEP_SIZE.y/2)), Constants.SHEEP_SIZE, Constants.SHEEP_MOVESPEED)
    enemies.append(enemy)

# Main Game Loop
while run:

    # Set framerate
    clock.tick(Constants.FRAME_RATE)

    # Paint over screen to refresh it
    game_display.fill(Constants.BACKGROUND_COLOR)

    # If the player hits the x button exit loop
    for event in pygame.event.get():

        if event.type == QUIT:
            run = False
    
    deltaTime = clock.get_time()/1000

    # Update player
    dog.update(enemies, Constants.DISPLAY_WIDTH, Constants.DISPLAY_HEIGHT, deltaTime)
    dog.draw(game_display, Constants.MOVE_VECTOR_DIR_LENG)

    # Update the enemies
    for enemy in enemies:
        enemy.update(dog, Constants.DISPLAY_WIDTH, Constants.DISPLAY_HEIGHT, deltaTime)
        enemy.draw(game_display, Constants.MOVE_VECTOR_DIR_LENG)
    
   

    # Flip display
    pygame.display.flip()
    
# Exit pygame
pygame.quit()

