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
        self.calcCenter()
        self.speed = speed
        self.color = Constants.DEFAULT_COLOR

    def __str__(self):
        return (f"Size is {self.size}\n"
                 f"Position is {self.position}\n"
                 f"Velocity is {self.speed}\n"
                 f"Center is {self.center}")

    
    # Draw Method to draw the players square and also the vector lines
    def draw(self, dir, screen, leng):

        # Draw new player position
        self.center =  self.center + dir
        self.position = self.position + dir

        pygame.draw.rect(screen, self.color, pygame.Rect(self.center.x - self.size/2, self.center.y - self.size/2,  self.size, self.size))

        # Only draw move vector line when vector is greater than 0
        if dir.length() != 0:
            entPt = dir.scale(leng)
            pygame.draw.line(screen, Constants.MOVE_VECTOR_COLOR, (self.center.x, self.center.y),
                                                                 ((self.center.x + entPt.x), (self.center.y + entPt.y)), 2)

    # Update method used to return a direction vector
    def update(self, other):

        # Normalize and scale vector
        self.dir = self.dir.normalize()
        self.dir = self.dir.scale(self.speed)

        # Return scaled direction vector
        return self.dir

    def calcCenter(self):
        self.center = Vector(self.position.x + self.size/2, self.position.y + self.size/2)

