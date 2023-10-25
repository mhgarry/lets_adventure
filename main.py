import pygame # import library pygame to make our game
import sys # import sys to use exit function 
import os # import os to use path function and get the path of our game

'''
Variables
'''
# Game variables here
world_x = 960 # width of the game display
world_y = 720 # height of the game display

fps = 60 # frames per second of the game
ani = 4 # animation cycles of the game (used to animate the sprites)

world = pygame.display.set_mode([world_x,world_y]) # create the game display
ALPHA = (0,255,0) # set the color of the background to green (used to make the background transparent)

'''
Objects
'''
# Classes and functions here
class Player(pygame.sprite.Sprite): # player class to create the player sprite and controls
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) # initialize the sprite
        self.move_x = 0 # set the default x movement of the sprite
        self.move_y = 0 # set the default y movement of the sprite
        self.frame = 0 # set the default frame of the sprite
        self.images = [] # create an empty list to store the sprite images
        for i in range(1,6): # create loop to loop through images and create a sprite animation
            img = pygame.image.load(os.path.join('images', 'hero' + str(i) + '.png'))
            img.convert_alpha() # convert and optimize the image
            img.set_colorkey((ALPHA)) # set the colorkey of the image to white
            self.images.append(img) # add the image to the list
            self.image = self.images[0] # set the default image of the sprite
            self.rect = self.image.get_rect() # get the dimensions of the sprite
        
    def control(self, x, y):
        '''
        Control player movement
        '''
        self.move_x += x # add movement to the x axis of the sprite by the amount of x
        self.move_y += y # add movement to the y axis of the sprite by the amount of y
        
    def update(self):
        '''
        Update sprite position
        '''
        self.rect.x = self.rect.x + self.move_x # update the x position of the sprite by the amount of x
        self.rect.y = self.rect.y + self.move_y # update the y position of the sprite by the amount of y
        
        # moving left
        if self.move_x < 0:
            self.frame += 1 # add 1 to the frame
            if self.frame > 3 * ani: # if the frame is greater than 3 * ani then set the frame to 0
                self.frame = 0 # set the frame to 0 to start the animation over
            self.image = pygame.transform.flip(self.images[self.frame // ani], True, False) # flip the image to the left 
        
        # moving right
        if self.move_x > 0:
            self.frame += 1 # add 1 to the frame
            if self.frame > 3 * ani: # if the frame is greater than 3 * ani then set the frame to 0
                self.frame = 0 # set the frame to 0 to start the animation over
            self.image = self.images[self.frame // ani] # set the image back to default the right
            
class Enemy(pygame.sprite.Sprite): #create an enemy class
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) # initialize the sprite
        self.move_x = 0 # set the default x movement of the sprite
        self.move_y = 0 # set the default y movement of the sprite
        self.frame = 0 # set the default frame of the sprite
        self.images = []
        for i in range(1,8):
            img = pygame.image.load(os.path.join('images', 'enemy' + str(i) + '.png'))
            img.convert_alpha()
            img.set_colorkey((ALPHA))
            self.images.append(img)
            self.image = self.images[0]
            self.rect = self.image.get_rect()
'''
Setup
'''
# Run once code here
backdrop = pygame.image.load(os.path.join('images', 'Battleground1.png')) # load the background image
clock = pygame.time.Clock() # create a clock to control time in our game
pygame.init() # initialize pygame 
backdropbox = world.get_rect() # get the dimensions of the game display
main = True # game loop set to true as default to run the game


player = Player() # spawn the player
player.rect.x = 0 # set the x position of the player
player.rect.y = 0  # set the y position of the player
player_list = pygame.sprite.Group() # create a sprite group to store the player
player_list.add(player) # add the player to the sprite group
steps = 10 # pixels to move the sprite by each step

enemy = Enemy() # spawn the enemy
enemy_list = pygame.sprite.Group() # create a sprite group to store the enemy
enemy_list.add(enemy) # add the enemy to the sprite group

'''
Main Loop
'''
# Run every frame code here
# Run every frame code here
while main:
    for event in pygame.event.get():  # get and loop through all events in code
        if event.type == pygame.QUIT:  # if the user quits the game then run the following code
            pygame.quit()  # quit the game
            try:
                sys.exit()  # exit the game
            finally:
                main = False  # set main to false to stop the game loop

        if event.type == pygame.KEYDOWN:  # if the user presses a key then run the following code
            if event.key == ord('q'):  # defines actions for the q key
                pygame.quit()
                try:
                    sys.exit()
                finally:
                    main = False
            if event.key == pygame.K_LEFT or event.key == ord('a'):  # defines actions for the left arrow key and the a key
                player.control(-steps, 0)  # move the player to the left by the amount of steps
            if event.key == pygame.K_RIGHT or event.key == ord('d'):  # defines actions for the right arrow key and the d key
                player.control(steps, 0)  # move the player to the right by the amount of steps
            if event.key == pygame.K_UP or event.key == ord('w'):  # defines actions for the up arrow key and the w key
                print('jump')

        if event.type == pygame.KEYUP:  # if the user releases a key then run the following code
            if event.key == pygame.K_LEFT or event.key == ord('a'):  # defines actions for the left arrow key and the a key
                player.control(steps, 0)
            if event.key == pygame.K_RIGHT or event.key == ord('d'):  # defines actions for the right arrow key and the d key
                player.control(-steps, 0)

    world.blit(backdrop, backdropbox)  # draw the background image on the game display
    player.update()  # updates the player sprite
    player_list.draw(world)  # draw the player sprite on the game display
    enemy_list.draw(world)  # draw the enemy sprite on the game display
    pygame.display.flip()  # update the game display
    clock.tick(fps)  # set the fps of the game
