# importing important libraries
import pygame 
import time
from random import randint

pygame.init()   # Initialize all imported pygame modules

# setting colors
WHITE = (255,255,255)
BLUE = (0,0,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
color_custom_1 = (10,145,80)  # creating a custom color

# setting game parameters
screen = pygame.display.set_mode([500,500]) # gives a surface
gameX = 20
gameY = 40
gameWidth = 440  # window width
gameHeight = 400  # window height
gameBorder = 3    # window border width

# screen background setting
screen.fill(WHITE)

INT_MAX = 100000000000000

