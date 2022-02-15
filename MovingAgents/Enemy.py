import Agent
import random

from Agent import *

# Player class
class Enemy(Agent):

    # Called on initilization
    def __init__(self, position, size, speed, image):

        super().__init__(position, size, speed, image)
        self.color = Constants.ENEMY_COLOR
        self.velocity = Vector(random.uniform(-1,1),random.uniform(-1,1))
        self.tagged = False
        self.tag_timer = 0
        self.wander = 0        
        self.type = Constants.EDIS_VECTOR_COLOR
        self.thick = Constants.EDIS_VECTOR_THICKNESS

    # Update method used to return a direction vector
    def update(self, player, worldWidth, worldHeight, deltaTime):

        # Set movespeed for enemy
        self.speed = Constants.SHEEP_MOVESPEED

        # If the enemy is tagged, start tag timer
        if self.tagged == True:

            if self.tag_timer > 0 :

                self.tag_timer -= 1
                self.color = Constants.ENEMY_TCOLOR

            else:

                self.tagged = False
                self.color = Constants.ENEMY_COLOR

        # Calculate distance to player
        dist = self.calcDist(player)

        # If player is in range, run, if not wander
        if dist < Constants.ENEMY_RANGE and self.tagged == False:

            self.velocity = self.center - player.center
            self.focus = player

        else:
        
            self.focus = self

            if self.wander > 0 :

                self.wander -= 1                

            else:

                self.velocity += Vector(random.uniform(-.5,.5),random.uniform(-.5,.5))
                self.wander = Constants.ENEMY_WANDER_TIMER

        super().update(player, worldWidth, worldHeight, deltaTime)
