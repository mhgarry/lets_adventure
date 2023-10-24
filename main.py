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
backdrop = pygame.image.load(os.path.join('pictures', 'mountain_background.svg')).convert() # load the background image
backdropbox = world.get_rect() # get the dimensions of the game display

main = True # game loop set to true as default to run the game

'''
Objects
'''

# Classes and functions here
class Player(pygame.sprite.Sprite):
    '''
    Player class
    '''
    def __init__(self):
        pygame.sprite.Sprite__init__(self) # initialize the sprite class
        self.images = [] # create a list to store the images of the sprite
        for i in range(1,6):
            img = pygame.image.load(os.path.join('images', 'hero' + str(i) + '.png')).convert() # load the sprite images from the images folder
            self.images.append(img) # append each image to the list of images
            self.image = self.images[0] # set the image of the sprite to the first index of the list of images
            self.rect = self.image.get_rect() # get the dimensions of the sprite image
'''
Setup
'''

clock = pygame.time.Clock() # create a clock object to control time in our game
pygame.init() # initialize pygame
# Run once code here
player = Player() # spawn the player
player.rect.x = 0 # set the x position of the player
player.rect.y = 0  # set the y position of the player
player_list = pygame.sprite.Group() # create a sprite group to store the player
player_list.add(player) # add the player to the sprite group

'''
Main Loop
'''
# Run every frame code here
while main: # while main is true run the game
    for event in pygame.event.get(): # get and loop through all events in game
        if event.type == pygame.QUIT: # if the event is quit then run the following code
            pygame.quit() # quit the game
            try:
                sys.exit() # exit the game
            finally:
                main = False # set main to false to stop the game loop
        if event.type == pygame.KEYDOWN:
            if event.key == ord('q'): # keydown on q key ends the game
                pygame.quit()
            try: 
                sys.exit()
            finally:
                main = False
    world.blit(backdrop, backdropbox) # draw background image on game display 
    player_list.draw(world) # draw the player on the game display
    pygame.display.flip() # update the game display 
    clock.tick(fps) # set the fps of the game