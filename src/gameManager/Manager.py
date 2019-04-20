import sys
from src.asteroid.Asteroid import Asteroid
from src.asteroid.Asteroid2 import Asteroid2
from src.asteroid.Asteroid3 import Asteroid3
from Weapon import *
import pygame
from src.alien.Alien import Alien

class Manager:
    def __init__(self):
        self

    def startMusic(self):
        music = pygame.mixer.music.load(os.path.join(AUDIO_DIR, 'beat1.wav'))
        pygame.mixer.music.set_volume(0.1)
        pygame.mixer.music.play(loops=-1)


    def AstroidInit(self):
        for i in range(7):
            if i < 3:
                Asteroid()
                # Asteroid.Asteroid()
            elif i < 6:
                Asteroid2()
                # Asteroid2.Asteroid2()
            else:
                Asteroid3()
                # Asteroid3.Asteroid3()

    def Alien(self):
        Alien()

    # function to exit the game
    def game_exit(self):
        pygame.quit()
        sys.exit()