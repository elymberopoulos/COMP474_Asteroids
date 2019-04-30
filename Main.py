import sys
from src.player import Player
from Weapon import *
from src.collision.Collider import Collider
from src.gameManager import Manager
from Constants import *
from src.alien.Alien import Alien


# start the pygame engine
pygame.init()
# create the pygame window with the specified dimensions
window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
# set the window title
pygame.display.set_caption(TITLE)
# start the game clock
clock = pygame.time.Clock()
# create the player
player = Player.Player()




# Game management functions have been abstracted out to their own class for organization
game_manager = Manager.Manager()
game_manager.start_music()
game_manager.create_asteroid(ASTEROIDS_AT_START)

# instantiate the collider
collider = Collider(player, PLAYER_LIVES, game_manager)

# define the basic font
font = pygame.font.SysFont("monospace", 15)

# function to manage pause
def pause():
    # boolean to control the loop
    pause_game = True
    # while loop occupies game while paused
    while pause_game:
        # check for quit event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # exit the game
                game_manager.game_exit()
            # check for keydown events
            if event.type == pygame.KEYDOWN:
                # check for p key to end pause
                if event.key == pygame.K_p:
                    # boolean is set to false to break the loop
                    pause_game = False
                # check for escape or q key to quit
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                    # exit the game
                    game_manager.game_exit()


def random_alien(in_range):
    # generate the first random value
    first_value = random.randint(0, in_range)
    # generate the second random value
    second_value = random.randint(0, in_range)
    # if the values match, then create an alien
    if first_value == second_value:
        game_manager.create_alien(1)


# main game loop
while True:

    # create random aliens
    random_alien(1000)

    # advance the clock
    clock.tick(FPS)
    # set the background to black
    window.fill(BLACK)

    # check for events
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            # check for the escape key press
            if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                # exit the game
                game_manager.game_exit()
            # check for P key for pause
            if event.key == pygame.K_p:
                pause()

    # imported module for collision detection and asteroid respawn
    collider.check_collisions()

    # update the sprites
    GAME_SPRITES.update()
    # draw the game sprites in the window
    GAME_SPRITES.draw(window)

    # display the score
    score_label = font.render("Score: " + str(collider.score), 1, (255, 255, 255))
    window.blit(score_label, (WIN_WIDTH * .75, 20))

    # display the number of lives
    lives_label = font.render("LIVES: " + str(collider.lives), 1, (255, 255, 255))
    window.blit(lives_label, (WIN_WIDTH * .25, 20))

    # display the number of lives
    asteroids_label = font.render("ASTEROIDS: " + str(ASTEROIDS.__len__()), 1, (255, 255, 255))
    window.blit(asteroids_label, (WIN_WIDTH * .5, 20))

    pygame.display.flip()


