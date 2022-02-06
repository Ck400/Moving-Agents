import Agent

from Agent import *

# Player class
class Player(Agent):

    # Called on initilization
    def __init__(self, position, size, speed):
        super().__init__(position, size, speed)
        self.color = Constants.PLAYER_COLOR
        self.type = Constants.PDIS_VECTOR_COLOR
        self.thick = Constants.PDIS_VECTOR_THICKNESS

    def draw(self, dir, screen, leng):

        super().draw(dir, screen, leng)
        
        if self.collision(self.focus.hitbox):
            self.focus.tagged = True
            self.focus.tag_timer = Constants.ENEMY_TAG_TIME

    # Update method used to return a direction vector
    def update(self, other, worldWidth, worldHeight):

        self.speed = Constants.PLAYER_MOVESPEED

        # Create direction vector
        self.dir = Vector(0,0)     
        self.dist = 99999

        if len(other) != 0:            

            for item in other:
                if item.tagged == False:

                    iDist = self.calcDist(item)

                    if  iDist < self.dist:
                        self.close = item
                        self.dist =  iDist

                        self.dir = item.position - self.position
                        self.focus = self.close

        super().update(other, worldWidth, worldHeight)

        return self.dir