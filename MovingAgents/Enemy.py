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
        self.tagged = False
        self.tag_timer = 0
        
        self.type = Constants.EDIS_VECTOR_COLOR
        self.thick = Constants.EDIS_VECTOR_THICKNESS

    # Update method used to return a direction vector
    def update(self, player, worldWidth, worldHeight):

        if self.tagged == True:

            if self.tag_timer > 0 :
                self.tag_timer -= 1
                self.color = Constants.ENEMY_TCOLOR

            else:
                self.tagged = False
                self.color = Constants.ENEMY_COLOR

        self.speed = Constants.ENEMY_MOVESPEED

        dist = self.calcDist(player)

        if dist < Constants.ENEMY_RANGE:
            self.dir = self.center - player.center
            self.focus = player
        else:
            self.dir += Vector(random.uniform(-.1,.1), random.uniform(-.1,.1))
            self.focus = self

        super().update(player, worldWidth, worldHeight)

        return self.dir
