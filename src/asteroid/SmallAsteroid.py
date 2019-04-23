import pygame
import random
import Constants
from Constants import *
import os

"""
This asteroid is spawned when a larger asteroid is destroyed
"""


class SmallAsteroid(pygame.sprite.Sprite):

    # small asteroid takes in the x and y position as a starting location
    def __init__(self, in_x, in_y, in_dx, in_dy):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(os.path.join(Constants.IMG_DIR, "Small_Asteroid.PNG")).convert_alpha()
        self.rect = self.image.get_rect()

        # Set start location and speeds
        self.rect.x = in_x # random.randrange(Constants.WIN_WIDTH - self.rect.width)
        self.rect.y = in_y    # random.randrange(-100, -50)

        self.speed_x = in_dx + self.random_speed(-1, 1)

        self.speed_y = in_dy + self.random_speed(-1, 1)

        Constants.GAME_SPRITES.add(self)
        Constants.ASTEROIDS.add(self)

    def random_speed(self, in_min, in_max):
        value = random.randrange(in_min, in_max)
        while 0 == value:
            value = random.randrange(in_min, in_max)
        return value

    def update(self):
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

