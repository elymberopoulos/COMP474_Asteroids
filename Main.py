import sys
from src.asteroid import Asteroid, Asteroid2, Asteroid3
from Player import Player
from Constants import *

# start the pygame engine
pygame.init()
# create the pygame window with the specified dimentions
window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
# set the window title
pygame.display.set_caption(TITLE)
# start the game clock
clock = pygame.time.Clock()
# create the player
player = Player()

# function to exit the game
def game_exit():
    pygame.quit()
    sys.exit()

#Variables to keep track of sprites on the screen

for i in range(10):
    if i <= 2:
        Asteroid.Asteroid()
    elif i <= 6:
        Asteroid2.Asteroid2()
    else:
        Asteroid3.Asteroid3()




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
                game_exit()

    # update the sprites
    GAME_SPRITES.update()
    # draw the game sprites in the window
    GAME_SPRITES.draw(window)
    pygame.display.flip()

