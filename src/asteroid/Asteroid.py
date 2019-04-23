import pygame
import random
import Constants
from Constants import *
import os
from src.asteroid.SmallAsteroid import SmallAsteroid

"""
This class of asteroids spawn at the top of the screen and move to the bottom side of the window.
"""


class Asteroid(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.asteroidImage = pygame.image.load(os.path.join(Constants.IMG_DIR, "Asteroid_1.PNG")).convert_alpha()
        self.image = self.asteroidImage
        self.image = pygame.Surface((40, 40))
        self.image.fill((150, 150, 150))
        self.rect = self.image.get_rect()

        # Set start location and speeds
        self.rect.x = random.randrange(Constants.WIN_WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -50)
        self.speed_y = random.randrange(1, 4) * ASTEROID_SPEED
        self.speed_x = random.randrange(-2, 2) * ASTEROID_SPEED

        Constants.GAME_SPRITES.add(self)
        Constants.ASTEROIDS.add(self)

    def update(self):
        self.image = self.asteroidImage
        self.rect.y += self.speed_y
        self.rect.x += self.speed_x

        if self.rect.top > Constants.WIN_HEIGHT + 15 or self.rect.left < -15 or self.rect.right > Constants.WIN_WIDTH:
            self.rect.x = random.randrange(
                Constants.WIN_WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -50)
            self.speed_y = random.randrange(-2, 2) * ASTEROID_SPEED
            self.speed_x = random.randrange(-2, 2) * ASTEROID_SPEED

    # on destruction, spawn 3 small asteroids
    def __del__(self):
        Constants.GAME_SPRITES.remove(self)
        Constants.ASTEROIDS.remove(self)
        SmallAsteroid(self.rect.x, self.rect.y)
        SmallAsteroid(self.rect.x, self.rect.y)
        SmallAsteroid(self.rect.x, self.rect.y)
