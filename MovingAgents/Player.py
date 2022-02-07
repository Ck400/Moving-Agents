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

    # Draw Method to draw the agent
    def draw(self, dir, screen, leng):

        super().draw(dir, screen, leng)
        
        # If a collision occurs with the target object, set its tagged to true and start tag cd
        if self.collision(self.focus.hitbox):
            self.focus.tagged = True
            self.focus.tag_timer = Constants.ENEMY_TAG_TIME

    # Update method used to return a direction vector
    def update(self, other, worldWidth, worldHeight):

        # Setmovespeed to player
        self.speed = Constants.PLAYER_MOVESPEED

        # Create direction vector
        self.dir = Vector(0,0)     
        self.dist = 99999

        # If the enemy list exists
        if len(other) != 0:            

            # Parse the list for each item and set direction to the closest one
            for item in other:

                # Ignore anything thats already tagged
                if item.tagged == False:

                    iDist = self.calcDist(item)

                    if  iDist < self.dist:
                        self.close = item
                        self.dist =  iDist

                        self.dir = item.position - self.position
                        self.focus = self.close

        super().update(other, worldWidth, worldHeight)

        return self.dir