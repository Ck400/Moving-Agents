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

        self.speed = Constants.PLAYER_MOVESPEED

        # Create direction vector
        self.dir = Vector(0,0)

        if len(other) != 0:     

            close = other[0]
            dist = (self.center - close.center).length()

            for item in other:
            
                if (self.center - item.center).length() < dist :
                    close = item
                    dist =  (self.center - item.center).length()

                self.dir = item.position - self.position

        super().update(other)

        return self.dir