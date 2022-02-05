import Agent
import random

from Agent import *

# Player class
class Enemy(Agent):

    # Called on initilization
    def __init__(self, position, size, speed):
        super().__init__(position, size, speed)
        self.color = Constants.ENEMY_COLOR
        self.dir = Vector(0,0)

    # Update method used to return a direction vector
    def update(self, player):

        random.seed();

        self.speed = Constants.ENEMY_MOVESPEED

        dist = (self.center - player.center).length()

        if dist < Constants.ENEMY_RANGE:
            self.dir = self.center - player.center
        else:
            self.dir += Vector(random.uniform(-.1,.1), random.uniform(-.1,.1))

        super().update(player)

        return self.dir
