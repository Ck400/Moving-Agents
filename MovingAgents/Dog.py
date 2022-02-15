import Agent

from Agent import *

# Player class
class Dog(Agent):

    # Called on initilization
    def __init__(self, position, size, speed):

        super().__init__(position, size, speed)

        self.color = Constants.DOG_COLOR
        self.type = Constants.DOG_DIS_VECTOR_COLOR
        self.thick = Constants.DOG_DIS_VECTOR_THICKNESS
        self.weight = Constants.DOG_WEIGHT
        self.focus = None

    # Draw Method to draw the agent
    def draw(self, screen, leng):

        super().draw(screen, leng)
        
        # If a collision occurs with the target object, set its tagged to true and start tag cd
        if self.collision(self.focus.hitbox):
            self.focus.tagged = True
            self.focus.tag_timer = Constants.ENEMY_TAG_TIME

    # Update method used to return a direction vector
    def update(self, other, worldWidth, worldHeight, deltaTime):

        # Setmovespeed to player
        self.speed = Constants.DOG_MOVESPEED

        # Create direction vector
        self.velocity = Vector(0,0)     
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

                        self.velocity = item.position - self.position
                        self.focus = self.close

        super().update(other, worldWidth, worldHeight, deltaTime)