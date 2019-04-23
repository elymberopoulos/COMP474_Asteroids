import pygame
import random
import Constants
from Constants import *
import os
from src.asteroid.SmallAsteroid import SmallAsteroid

"""
Asteroids class
"""


class Asteroid(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        # random value between 1 and 3 to select asteroid sprite
        random_asteroid_sprite = random.randrange(1, 4, 1)

        # associate with the sprite
        self.image = pygame.image.load(os.path.join(IMG_DIR, "Asteroid_" + str(random_asteroid_sprite) + ".PNG")).convert_alpha()




        # get the rectangular size of the sprite
        self.rect = self.image.get_rect()

        # Set start location and speeds
        self.rect.x = random.randrange(0, WIN_WIDTH)
        self.rect.y = random.randrange(0, WIN_HEIGHT)

        self.speed_y = self.random_speed(-4, 4) * ASTEROID_SPEED
        self.speed_x = self.random_speed(-4, 4) * ASTEROID_SPEED

        # add self to the general game sprites
        GAME_SPRITES.add(self)
        # add self to the asteroids game sprites
        ASTEROIDS.add(self)

    # returns a random range of numbers excluding zero
    def random_speed(self, in_min, in_max):
        value = random.randrange(in_min, in_max)
        while 0 == value:
            value = random.randrange(in_min, in_max)
        return value

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

    # on destruction, spawn 3 small asteroids
    def __del__(self):
        # remove self form game sprites
        GAME_SPRITES.remove(self)
        # remove self from asteroids
        ASTEROIDS.remove(self)
        #spawn 3 small asteroids
        SmallAsteroid(self.rect.x, self.rect.y, self.speed_x, self.speed_y)
        SmallAsteroid(self.rect.x, self.rect.y, self.speed_x, self.speed_y)
        SmallAsteroid(self.rect.x, self.rect.y, self.speed_x, self.speed_y)
