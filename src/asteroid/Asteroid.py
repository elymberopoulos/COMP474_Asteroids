import pygame
import random
import Constants
from Constants import *
import os
from src.asteroid.SmallAsteroid import SmallAsteroid
import math

"""
Asteroids class
"""

class Asteroid(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        # associate with the sprite randomly by directly using the random number between 1 and 3
        self.image = pygame.image.load(os.path.join(IMG_DIR, "Asteroid_" + str(random.randrange(1, 4, 1)) + ".PNG")).convert_alpha()

        # get the rectangular size of the sprite
        self.rect = self.image.get_rect()

        # Set start location and speeds
        self.rect.x = random.randrange(0, WIN_WIDTH)
        self.rect.y = random.randrange(0, WIN_HEIGHT)

        self.speed_x = random.randrange(-3, 3, 1)
        self.speed_y = random.randrange(-3, 3, 1)

        # this is to keep the speed at a minimum value
        while .5 >= abs(self.speed_x):
            self.speed_x = random.randrange(-3, 3, 1)
        while .5 >= abs(self.speed_y):
            self.speed_y = random.randrange(-3, 3, 1)

        # add self to the general game sprites
        GAME_SPRITES.add(self)
        # add self to the asteroids game sprites
        ASTEROIDS.add(self)

    # pygame update function
    def update(self):
        # standard motion
        self.rect.y += self.speed_y
        self.rect.x += self.speed_x

        # wrap around the sides of the screen
        if self.rect.x > WIN_WIDTH:
            self.rect.x = 0
        if self.rect.x < 0:
            self.rect.x = WIN_WIDTH
        if self.rect.y > WIN_HEIGHT:
            self.rect.y = 0
        if self.rect.y < 0:
            self.rect.y = WIN_HEIGHT

    def kill(self):
        # remove self form game sprites
        GAME_SPRITES.remove(self)
        # remove self from asteroids
        ASTEROIDS.remove(self)
        # spawn 3 small asteroids
        SmallAsteroid(self.rect.x, self.rect.y, self.speed_x, self.speed_y)
        SmallAsteroid(self.rect.x, self.rect.y, self.speed_x, self.speed_y)
        SmallAsteroid(self.rect.x, self.rect.y, self.speed_x, self.speed_y)
