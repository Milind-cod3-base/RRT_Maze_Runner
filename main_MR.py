# importing important libraries
from trace import Trace
import pygame 
import time
from random import randint

import RRT_algo


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



# to get the text on the button
def clickText():
    font = pygame.font.Font('arial.ttf', 12)
    text = font.render('CLICK HERE', True, WHITE)
    textRect = text.get_rect()
    textRect.center = (75, 495)
    screen.blit(text, textRect)

# for the game description text
def desText(s, x=315, y=485):
    pygame.draw.rect(screen, WHITE, (125, 470, 500, 30))
    font = pygame.font.SysFont('segoeuisemilight', 15)
    text = font.render('%s'%(s), True, BLACK )
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

clickText()
desText("Instruction: ", y=460)
desText("Draw the Obstacles, then CLICK BLACK Button")

# looping for running
while running:
    for event in pygame.event.get():

        # to quit the game
        if event.type == pygame.QUIT:
            running = False
            break

        # if game is not running
        if running == False:
            break

        # taking input from the mouse
        m = pygame.mouse.get_pressed()
        # storing the mouse coordinates
        x,y = pygame.mouse.get_pos()

        if m[0]==1:
            if point_inside_rec(B1.x, B1.y, B1.width, B1.height, x, y):

                """
                 
                 Changing button color and description at each level

                """    
                if level ==1 and Start == []:
                    level +=1
                    B1.colour = RED # button in red color
                    desText(" Draw the starting point, then CLICK RED button")

                elif level ==2 and Start:
                    level +=1
                    B1.colour = GREEN # button in green color
                    desText(" Draw the Destination point, then CLICK GREEN button")
                
                elif level ==3 and End!=set():
                    level +=1
                    B1.color = BLUE # button in blue color
                    desText("Path is going to be explored using RRT Algorithm")


                B1.create(screen)
                clickText()
                continue

            # make the maze
            elif level ==1:
                if point_inside_game(x,y):
                    OBS[(x,y)] =1 
                    pygame.draw.circle( screen,  BLACK, (x,y), 10)
            
            # make the starting point
            elif level == 2 and Start==[]:
                if point_inside_game(x,y):
                    Start = (x,y)
                    pygame.draw.circle(screen, RED, (x,y), 5)
            
            # make the destination point
            elif level ==3:
                if point_inside_game(x,y):
                    End.add((x,y))
                    pygame.draw.circle(screen, GREEN, (x,y), 10)

        # if level is more than 3, stop asking for inputs    
        if level >=4:
            running = False
            break
    
    # update the display
    pygame.display.update()

# running the game for the algorithm
running = True
parent[Start] = (-1, -1)
Trace = []
Timer = time.time()

while running:
    for event in pygame.event.get():
        # to quit the game
        if event.type == pygame.QUIT:
            running = False
            break

    # gettin the cordinates of the random points
    x,y = random_point() 
    
    if (time.time() - Timer) > 5:
        Step = 5
    
    # calling module RRT_algo
    good, x_m, y_m, ans= RRT_algo.rrt(x,y,parent)


    if good and ans:
        x_cur = ans[0]
        y_cur = ans[1]

        # 255 value of alpha is fully opaque
        if screen.get_at((x_cur, y_cur)) != (0, 0, 0, 255 ) and (x_cur, y_cur) not in parent:
            parent[(x_cur, y_cur)] = (x_m, y_m)

            # tracing the path
            if screen.get_at((x_cur, y_cur)) == (0, 255, 0, 255):
                Trace = (x_cur, y_cur)

                # kill the running
                running = False

            # draw the other possible routes
            pygame.draw.line(screen, BLUE, (x_cur, y_cur), (x_m, y_m), 2)

    # update the display
    pygame.display.update()

running = True

# This loop gets the route back to start point
while (Trace and running):
    
    # checking for quit command
    if event.type == pygame.QUIT:
        running = False
        break
    
    # loop to keep the screen on until player restarts the game
    while Trace!=Start:
        x,y = parent[Trace]
        pygame.draw.line(screen, GREEN, (x,y), Trace, 2)
        Trace = (x,y)

    desText("Green coloured path is the optimised path")
    pygame.display.update()


# Quit the game
pygame.quit()
