import pygame
import Vector
import Agent

from pygame.locals import *
from Vector import *

# Player class
class Player(Agent):

    # Called on initilization
    def __init__(self, center, size):
        self.center = center 
        self.size = size

    # Draw Method to draw the players square and also the vector lines
    def draw(self, dir, screen, leng):

        # Draw new player position
        self.center =  self.center + dir
        pygame.draw.rect(screen, (245, 175, 240), pygame.Rect(self.center.x - self.size/2, self.center.y - self.size/2,  self.size, self.size))

        # Only draw vector line when vector is greater than 0
        if dir.length() != 0:
            entPt = dir.scale(leng)
            pygame.draw.line(screen, (100, 5, 135), (self.center.x, self.center.y),
                                                    ((self.center.x + entPt.x), (self.center.y + entPt.y)), 2)

    # Update method used to return a direction vector
    def update(self, velocity):

        # Create direction vector
        dir = Vector(0,0)

        # Get the keys that the player are pressing and add to the vector accordingly
        keys = pygame.key.get_pressed()
      
        if keys[pygame.K_a]:

            dir = dir + Vector(-1,0)   
          
        if keys[pygame.K_d]:
          
            dir = dir + Vector(1,0)   
         
        if keys[pygame.K_w]:

            dir = dir + Vector(0,-1)   
          
        if keys[pygame.K_s]:

            dir = dir + Vector(0,1)   

        # Normalize and scale vector
        dir = dir.normalize()
        dir = dir.scale(velocity)

        # Return scaled direction vector
        return dir
