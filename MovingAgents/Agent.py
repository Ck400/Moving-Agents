import pygame
import Constants

from Constants import *
from pygame.locals import *

# Player class
class Agent(object):

    # Called on initilization
    def __init__(self, position, size, speed, image):

        self.position = position
        self.size = size
        self.speed = speed
        self.color = Constants.DEFAULT_COLOR
        self.dir = (0,0)
        self.focus = self
        self.weight = 1
        self.boundaryForces = []
        self.updateCenter()
        self.updateRect()
        self.image = image
        self.angle = 0

    # Overload string method to print out important agent characteristics
    def __str__(self):
        return (f"Size is {self.size}\n"
                 f"Position is {self.position}\n"
                 f"Velocity is {self.speed}\n"
                 f"Center is {self.center}")

    def updateVelocity(self, velocity):
        self.velocity = velocity.normalize()

    def updateRect(self):
        self.hitbox = pygame.Rect(self.position.x, self.position.y,  self.size.x, self.size.y)

    # Calculate and set the objects center
    def updateCenter(self):
        self.center = Vector(self.position.x + self.size.x/2, self.position.y + self.size.y/2)

    
    # Detect if a collision between two pygame.Rects occured
    def collision(self, hitbox):
        return pygame.Rect.colliderect(self.hitbox, hitbox)

    
    # Calculate and set self center
    def calcDist(self, other):
        return (self.center - other.center).length()

    # Update method used to return a direction vector
    def update(self, other, worldWidth, worldHeight, deltaTime):

        # Normalize and scale vector according to weight 
        self.updateVelocity(self.velocity.scale(self.weight))

        if deltaTime != 0:
            self.updateVelocity(self.velocity.scale(deltaTime))
        
        # Boundary Force
        
        # Right
        if (self.center + self.velocity).x > worldWidth - Constants.BOUND_RADIUS:

            self.boundaryForces.append(Vector(-1,0))

        # Left 
        elif (self.center + self.velocity).x < 0 + Constants.BOUND_RADIUS:

            self.boundaryForces.append(Vector(1,0))

        # Bottom
        if (self.center + self.velocity).y > worldHeight - Constants.BOUND_RADIUS:

            self.boundaryForces.append(Vector(0,1))

        # Top
        elif (self.center + self.velocity).y < 0 + Constants.BOUND_RADIUS:

            self.boundaryForces.append(Vector(0,-1))


        # World clamping

        # Left or Right
        if (self.center + self.velocity).x > (worldWidth - self.size.x/2) or (self.center + self.velocity).x < 0 + self.size.x/2:
            self.velocity.x *= -1

        # Top of Bottom
        if (self.center + self.velocity).y > (worldHeight - self.size.y/2) or (self.center + self.velocity).y < 0 + self.size.y/2:
            self.velocity.y *= -1

        # Calculate new player position
        self.position = self.position + self.velocity.scale(self.speed)
        self.updateRect()
        self.updateCenter()


    # Draw Method to draw the agent
    def draw(self, screen, leng):


        # Draw the player and their hitbox on screen
        pygame.draw.rect(screen, self.color, self.hitbox, 2)
  
        self.surf = pygame.transform.rotate(self.image, self.angle)
        upperLeft = Vector((self.center.x + self.size.x/2) - self.surf.get_width(), (self.center.y + self.size.y/2) - self.surf.get_height())
        screen.blit(self.surf,  [upperLeft.x, upperLeft.y])

        # Only draw move vector line when vector is greater than 0
        if self.velocity.length() != 0:
            entPt = self.velocity.scale(leng)
            pygame.draw.line(screen, Constants.MOVE_VECTOR_COLOR, (self.center.x, self.center.y),
                                                                 ((self.center.x + entPt.x), (self.center.y + entPt.y)), 2)

        # Draw line pointing to its current target
        if self.focus != self and self.velocity.length() != 0:
            pygame.draw.line(screen, self.type, (self.center.x, self.center.y),
                                                     ((self.focus.center.x), (self.focus.center.y)), self.thick)



