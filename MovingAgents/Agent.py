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
        self.focus = self

    # Overload string method to print out important agent characteristics
    def __str__(self):
        return (f"Size is {self.size}\n"
                 f"Position is {self.position}\n"
                 f"Velocity is {self.speed}\n"
                 f"Center is {self.center}")

    
    # Draw Method to draw the agent
    def draw(self, dir, screen, leng):

        # Calculate new player position
        self.position = self.position + dir
        self.calcCenter()

        # Draw the player and their hitbox on screen
        pygame.draw.rect(screen, self.color, self.hitbox)

        # Only draw move vector line when vector is greater than 0
        if dir.length() != 0:
            entPt = dir.scale(leng)
            pygame.draw.line(screen, Constants.MOVE_VECTOR_COLOR, (self.center.x, self.center.y),
                                                                 ((self.center.x + entPt.x), (self.center.y + entPt.y)), 2)

        # Draw line pointing to its current target
        if self.focus != self and dir.length() != 0:
            pygame.draw.line(screen, self.type, (self.center.x, self.center.y),
                                                     ((self.focus.center.x), (self.focus.center.y)), self.thick)

    # Update method used to return a direction vector
    def update(self, other, worldWidth, worldHeight):

        # Normalize and scale vector
        self.dir = self.dir.normalize()
        self.dir = self.dir.scale(self.speed)

        # Create the rectangle used for pygame
        self.hitbox = pygame.Rect(self.center.x - self.size/2, self.center.y - self.size/2,  self.size, self.size)
        
        # World clamping
        if (self.center + self.dir).x > (worldWidth - self.size/2) or (self.center + self.dir).x < 0 + self.size/2:
            self.dir.x *= -1

        if (self.center + self.dir).y > (worldHeight - self.size/2) or (self.center + self.dir).y < 0 + self.size/2:
            self.dir.y *= -1

        # Return scaled direction vector
        return self.dir

    # Calculate and set the objects center
    def calcCenter(self):
        self.center = Vector(self.position.x + self.size/2, self.position.y + self.size/2)

    # Calculate and set self center
    def calcDist(self, other):
        return (self.center - other.center).length()

    # Detect if a collision between two pygame.Rects occured
    def collision(self, hitbox):
        return pygame.Rect.colliderect(self.hitbox, hitbox)

