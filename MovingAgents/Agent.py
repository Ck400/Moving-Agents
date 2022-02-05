import pygame
import Vector
import Constants

from pygame.locals import *
from Vector import *

# Player class
class Agent(object):

    # Called on initilization
    def __init__(self, position, size, speed):
        self.position = position
        self.size = size
        self.center = (position.x + size/2, position.y + size/2)
        self.speed = speed
        self.color = Constants.DEFAULT_COLOR;

    def __str__(self):
        return (f"Size is {self.color}\n" 
                f"Position is {self.position\n"
                f"Velocity is {self.speed}\n"
                f"Center is {self.center}")

    
    # Draw Method to draw the players square and also the vector lines
    def draw(self, dir, screen, leng):

        # Draw new player position
        self.center =  self.center + dir
        pygame.draw.rect(screen, self.color, pygame.Rect(self.center.x - self.size/2, self.center.y - self.size/2,  self.size, self.size))

        # Only draw move vector line when vector is greater than 0
        if dir.length() != 0:
            entPt = dir.scale(leng)
            pygame.draw.line(screen, Constants.MOVE_VECTOR_COLOR, (self.center.x, self.center.y),
                                                                 ((self.center.x + entPt.x), (self.center.y + entPt.y)), 2)

    # Update method used to return a direction vector
    def update(self, other):

        # Create direction vector
        dir = Vector(0,0)

       
        # Normalize and scale vector
        dir = dir.normalize()
        dir = dir.scale(velocity)

        # Return scaled direction vector
        return dir

    def calcCenter(self):
        self.center = (position.x + size/2, position.y + size/2)

