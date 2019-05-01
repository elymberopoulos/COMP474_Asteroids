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
# define initial screen font
initial_font = pygame.font.SysFont("monospace", 50)

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

def initial_screen():
    initial_counter = 1
    while 0 != initial_counter:
        # advance the clock
        clock.tick(FPS)
        # start screen
        window.fill(BLACK)
        # display the number of lives
        start_label = initial_font.render("ASTEROIDS", 1, (255, 255, 255))
        window.blit(start_label, (WIN_WIDTH * .5, WIN_HEIGHT * .25))

        start_label = font.render("PRESS ENTER TO START GAME", 1, (255, 255, 255))
        window.blit(start_label, (WIN_WIDTH * .5, WIN_HEIGHT * .5))

        start_label = font.render("PRESS ESCAPE TO EXIT", 1, (255, 255, 255))
        window.blit(start_label, (WIN_WIDTH * .5, WIN_HEIGHT * .55))

        start_label = font.render("PRESS P TO PAUSE", 1, (255, 255, 255))
        window.blit(start_label, (WIN_WIDTH * .5, WIN_HEIGHT * .6))

        start_label = font.render("PRESS SPACE TO FIRE", 1, (255, 255, 255))
        window.blit(start_label, (WIN_WIDTH * .5, WIN_HEIGHT * .65))

        start_label = font.render("PRESS ARROW KEYS FOR MOVEMENT", 1, (255, 255, 255))
        window.blit(start_label, (WIN_WIDTH * .5, WIN_HEIGHT * .7))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                # check for return key for exiting initial screen
                if event.key == pygame.K_RETURN:
                    initial_counter = 0
                # check for the escape key press to quit the game
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                    # exit the game
                    game_manager.game_exit()

#start the inital screen
initial_screen()

player.invincible = True
player.safe_timer = PLAYER_SAFETY_TIME_INITIAL

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
    score_label = font.render("SCORE: " + str(collider.score), 1, (255, 255, 255))
    window.blit(score_label, (WIN_WIDTH * .75, 20))

    # display the number of lives
    lives_label = font.render("LIVES: " + str(collider.lives), 1, (255, 255, 255))
    window.blit(lives_label, (WIN_WIDTH * .25, 20))

    # display the number of lives
    # asteroids_label = font.render("ASTEROIDS: " + str(ASTEROIDS.__len__()), 1, (255, 255, 255))
    # window.blit(asteroids_label, (WIN_WIDTH * .5, 20))

    pygame.display.flip()


