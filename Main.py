import sys
from src.asteroid import Asteroid, Asteroid2, Asteroid3
from src.player import Player
from Constants import *
from Weapon import *
from src.collision import Collider
from src.gameManager import Manager
import random

# start the pygame engine
pygame.init()
# create the pygame window with the specified dimentions
window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
# set the window title
pygame.display.set_caption(TITLE)
# start the game clock
clock = pygame.time.Clock()
# create the player
player = Player.Player()

#Variables to keep track of sprites on the screen


# Game management functions have been abstracted out to their own class for organization
gameManager = Manager.Manager()
gameManager.AstroidInit()

# main game loop
while True:
    # advance the clock
    clock.tick(FPS)
    # set the background to black
    window.fill(BLACK)

    # check for events
    for event in pygame.event.get():
         if event.type == pygame.KEYDOWN:

            # check for the escape key press
            if event.key == pygame.K_ESCAPE:
                # exit the game
                gameManager.game_exit()

    # update the sprites
    GAME_SPRITES.update()
    # draw the game sprites in the window
    GAME_SPRITES.draw(window)

    # imported module for collision detection and asteroid respawn
    Collider.Collider(player)

    pygame.display.flip()

