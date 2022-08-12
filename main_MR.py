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
colour_custom_1 = (10,145,80)  # creating a custom color

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

# creating a class for button
class Button:
    
    # constructor
    def __init__(self, colour, x, y, width, height):
        self.colour = colour
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    # rectangular button with specs
    def create(self, screen):
        pygame.draw.rect(screen, self.colour, [self.x, self.y, self.width, self.height])


# in order to point inside the display
def point_inside_game(x, y):
    
    # checking if inside the x bounds
    if x > gameX + gameBorder and x < gameX + gameWidth - gameBorder:

        # checking if inside the y bounds
        if y > gameY + gameBorder and y < gameY + gameHeight - gameBorder:
            return(True)

    return (False)

# to generate and return random point coordinates in (x,y)
def random_point():
    x_random = randint(gameX + gameBorder, gameX + gameWidth - gameBorder - 1)
    y_random = randint(gameY + gameBorder, gameY + gameHeight - gameBorder - 1)

    return (x_random, y_random)

# get the point inside the rectangle and return boolean False
def point_inside_rec(xr, yr, wr, hr, x, y):

    # checking x bounds
    if x > xr and x < xr + wr:

        # checking y bounds
        if y > yr and y < yr + hr:
            return(True)

    return(False)

