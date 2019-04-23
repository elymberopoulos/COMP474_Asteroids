import sys
from src.asteroid.Asteroid import Asteroid
from Weapon import *
import pygame
from src.alien.Alien import Alien


class Manager:
    def __init__(self):
        pass

    def start_music(self):
        music = pygame.mixer.music.load(os.path.join(AUDIO_DIR, 'beat1.wav'))
        pygame.mixer.music.set_volume(0.05)
        pygame.mixer.music.play(loops=-1)

    def create_asteroid(self, in_asteroids):
        for i in range(in_asteroids):
            Asteroid()

    def create_alien(self, in_aliens):
        for i in range(in_aliens):
            Alien()

    # function to exit the game
    def game_exit(self):
        pygame.quit()
        sys.exit()
