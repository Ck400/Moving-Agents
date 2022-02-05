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
            dist = self.calcDist(close)
            self.focus = close

            for item in other:
            
                iDist = self.calcDist(item)

                if  iDist < dist :
                    close = item
                    dist =  iDist
                    self.focus = item


        else:
             self.focus = self

        self.dir = item.position - self.position

        super().update(other)

        return self.dir