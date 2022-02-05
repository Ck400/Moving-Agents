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

    def draw(self, dir, screen, leng):
        self.type = Constants.EDIS_VECTOR_COLOR
        self.thick = Constants.EDIS_VECTOR_THICKNESS
        super().draw(dir, screen, leng)

    # Update method used to return a direction vector
    def update(self, player):

        random.seed();

        self.speed = Constants.ENEMY_MOVESPEED

        dist = self.calcDist(player)

        if dist < Constants.ENEMY_RANGE:
            self.dir = self.center - player.center
            self.focus = player
        else:
            self.dir += Vector(random.uniform(-.1,.1), random.uniform(-.1,.1))
            self.focus = self

        super().update(player)

        return self.dir
