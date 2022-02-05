import pygame
import Agent

from Agent import *

# Player class
class Player(Agent):

    # Called on initilization
    def __init__(self, position, size, speed):
        super().__init__(position, size, speed)
        self.color = Constants.PLAYER_COLOR

    # Update method used to return a direction vector
    def update(self, other):

        self.velocity = Constants.PLAYER_MOVESPEED

        # Create direction vector
        self.dir = Vector(0,0)

        if len(other) != 0:     

            close = other[0]
            dist = Vector(self.center - close.center).length

            for item in other:
            
                if Vector.self.position - item.position < dist :
                    close = item
                    dist =  Vector(self.center - close.center).length

                self.dir = self.position - item.position

        super().update(other)

        return self.dir