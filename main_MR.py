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

# using Euclidean distance formula to get point to point distance
def p2p_dist(p1,p2):

    x1,y1 = p1 # getting x and y coordinates
    x2,y2 = p2
    
    return( ( (x1 - x2)**2 + (y1 - y2)**2 )**0.5 )

# to get the text on the button
def clickText():
    font = pygame.font.Font('freeansbold.ttf', 12)
    text = font.render('CLICK HERE', antialias= True, color= WHITE)
    textRect = text.get_rect()
    textRect.center = (75, 495)
    screen.blit(text, textRect)

# for the game description text
def desText(s, x=315, y=485):
    pygame.draw.rect(screen, WHITE, (125, 470, 500, 30))
    font = pygame.font.SysFont('segoeuisemilight', 15)
    text = font.render(text='%s'%(s), antialias= True, color= BLACK )
    textRect = text.get_rect()
    textRect.center = (x,y)
    screen.blit(source= text, dest= textRect)

running = True

# Button for game
pygame.draw.rect(screen, BLACK, (gameX, gameY, gameWidth, gameHeight), width=gameBorder)

B1 = Button(BLACK, 25, 470, 100, 50)
B1.create(screen)

OBS = dict() # creating instance

# number of forward steps towards random sampled point
Step = 10


# Start stores Starting Point (single point in RED)
Start = []

# End variable stores a set of Destination points (GREEN)
# Multiple points allowed to make the point appear bigger, and fast discovery
# due to huge number of pixels in this game
End = set() 

# parent for storing graph
parent = dict()
level = 1
