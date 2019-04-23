import sys
from src.player import Player
from Weapon import *
from src.collision.Collider import Collider
from src.gameManager import Manager
from Constants import *
from src.alien.Alien import Alien
from Score import Score

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

# Variables to keep track of sprites on the screen


# Game management functions have been abstracted out to their own class for organization
gameManager = Manager.Manager()
gameManager.startMusic()
gameManager.AstroidInit()

collider = Collider(player, PLAYER_LIVES)

rand = random.randint(0, 1000)
counter = 0
print(rand)
totalscore = 0
# main game loop
while True:
    counter += 1
    if counter == rand:
        gameManager.Alien()
        rand = random.randint(0,1000)
        counter = 0

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
    font = pygame.font.SysFont("monospace", 15)

    # imported module for collision detection and asteroid respawn
    collider.check_collisions()

    # display the score
    score_label = font.render("Score: " + str(collider.score), 1, (255, 255, 255))
    window.blit(score_label, (WIN_WIDTH*.75, 20))

    # display the number of lives
    lives_label = font.render("LIVES: " + str(collider.lives), 1, (255, 255, 255))
    window.blit(lives_label, (WIN_WIDTH*.25, 20))

    # update the sprites
    GAME_SPRITES.update()
    # draw the game sprites in the window
    GAME_SPRITES.draw(window)

    pygame.display.flip()
