import Vector

from Vector import *

# Constants

# SCREEN
FRAME_RATE = 60
DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600
BACKGROUND_COLOR = (100,149,237)

# DOG
DOG_MOVESPEED = 5.5
DOG_SIZE = Vector(16,32)
DOG_COLOR = (255, 244, 128)
DOG_WEIGHT = 1;

# Dog Distance vectors
DOG_DIS_VECTOR_COLOR = (255, 64, 102)
DOG_DIS_VECTOR_THICKNESS = 1

# ENEMY
SHEEP_COUNT = 5
SHEEP_MOVESPEED = 5
SHEEP_SIZE = Vector(16,32)

# Enemy Color and tagged color
ENEMY_COLOR = (0, 255, 60)
ENEMY_TCOLOR = (1, 74, 20)

# Enemy scared range
ENEMY_RANGE = 200

# Timers are all in seconds i.e 1 = 1 second, .5 = half a second
ENEMY_WANDER_TIMER = FRAME_RATE * .3
ENEMY_TAG_TIME = FRAME_RATE * 5

# Enemy Distance vectors
EDIS_VECTOR_COLOR = (0, 0, 0)
EDIS_VECTOR_THICKNESS = 4

# OTHER
MOVE_VECTOR_COLOR = (0, 42, 255)
MOVE_VECTOR_DIR_LENG = 10
DEFAULT_COLOR = (255,255,255)
BOUND_FORCE = 1
BOUND_RADIUS = 32