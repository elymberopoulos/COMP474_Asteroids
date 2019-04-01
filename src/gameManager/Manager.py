import sys
from src.asteroid import Asteroid, Asteroid2, Asteroid3
from src.player import Player
from Constants import *
from Weapon import *

class Manager:
    def __init__(self):
        self

    def AstroidInit(self):
        for i in range(10):
            if i <= 2:
                Asteroid.Asteroid()
            elif i <= 6:
                Asteroid2.Asteroid2()
            else:
                Asteroid3.Asteroid3()

    # function to exit the game
    def game_exit(self):
        pygame.quit()
        sys.exit()