<<<<<<< HEAD
import pygame, pygame.event, sys
from src.asteroid import Asteroid
from src.asteroid import Asteroid2
from src.asteroid import Asteroid3
from src.player import Player

def gameExit():
    pygame.quit()
    sys.exit()

def main():
    #Setup basic variables and methods for pygame
    pygame.init()
    windowWidth = 800
    windowHeight = 700
    fps = 45
    clock = pygame.time.Clock()
    gameWindow = pygame.display.set_mode((windowWidth, windowHeight))
    pygame.display.set_caption("Asteroids")
    surface = pygame.Surface((50,50))
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    #SHIP POSITION
    shipX = windowWidth/2
    shipY = windowWidth/2
    shipSpeed = 4

    #Variables to keep track of sprites on the screen
    game_sprites = pygame.sprite.Group()
    asteroidsOnScreen = pygame.sprite.Group()
    for i in range(10):
        if i <= 2:
            asteroid = Asteroid.Asteroid(windowWidth, windowHeight)
            game_sprites.add(asteroid)
            asteroidsOnScreen.add(asteroid)
        elif i <= 6:
            asteroid = Asteroid2.Asteroid2(windowWidth, windowHeight)
            game_sprites.add(asteroid)
            asteroidsOnScreen.add(asteroid)
        else:
            asteroid = Asteroid3.Asteroid3(windowWidth, windowHeight)
            game_sprites.add(asteroid)
            asteroidsOnScreen.add(asteroid) 

        

    while(True):
        
        #Possible bounding box for initial ship
        pygame.draw.ellipse(gameWindow, WHITE, (shipX, shipY, 20, 30))
        game_sprites.draw(gameWindow)
        game_sprites.update()
        #Draw Triangle
        # pygame.draw.lines(gameWindow, WHITE, True, ((400, 350), (450, 400), (350, 400), 1))
        pygame.display.update()

        #Monitor the FPS of the game
        clock.tick(fps)

        for event in pygame.event.get():
            # ________________________________________
            if event.type == pygame.QUIT:
                gameExit()
        
        rotate = 0
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]: shipY -= shipSpeed
        if pressed[pygame.K_DOWN]: shipY += shipSpeed
        if pressed[pygame.K_LEFT]: shipX -= shipSpeed
        if pressed[pygame.K_RIGHT]: shipX += shipSpeed
        if pressed[ord('a')]: rotate = pygame.transform.rotate(surface, -20)
        if pressed[ord('d')]: rotate = pygame.transform.rotate(surface, 20)

        gameWindow.fill(BLACK)
        # 'flip' display - always after drawing...
        pygame.display.flip()
=======
import sys
from Asteroid import *
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

>>>>>>> Jay_Branch

#Variables to keep track of sprites on the screen

for i in range(10):
    asteroid = Asteroid()
    '''
    elif i <= 6:
        asteroid = Asteroid2.Asteroid2(windowWidth, windowHeight)
        game_sprites.add(asteroid)
        asteroidsOnScreen.add(asteroid)
    else:
        asteroid = Asteroid3.Asteroid3(windowWidth, windowHeight)
        game_sprites.add(asteroid)
        asteroidsOnScreen.add(asteroid)
    '''


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

