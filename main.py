import pygame # import library pygame to make our game
import sys # import sys to use exit function 
import os # import os to use path function and get the path of our game

'''
Variables
'''
# Game variables here
world_x = 960 # width of the game display
world_y = 720 # height of the game display

fps = 40 # frames per second of the game
ani = 4 # animation cycles of the game (used to animate the sprites)

world = pygame.display.set_mode([world_x,world_y]) # create the game display
backdrop = pygame.image.load(os.path.join('pictures', 'mountain_background.svg')) # load the background image
backdropbox = world.get_rect() # get the dimensions of the game display

'''
Objects
'''

# Classes and functions here

'''
Setup
'''

clock = pygame.time.Clock() # create a clock object to control time in our game
pygame.init() # initialize pygame
# Run once code here

'''
Main Loop
'''

# Run every frame code here