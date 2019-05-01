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

        # initialize the sprite
        self.image = pygame.image.load(os.path.join(IMG_DIR, "Asteroid_" + str(random.randrange(1, 5, 1)) + ".png")).convert_alpha()
        # scale the sprite to the appropriate size
        self.image = pygame.transform.smoothscale(self.image, (20, 20))
        # get the rectangular size of the sprite
        self.rect = self.image.get_rect()
        # Set start location and speeds
        self.rect.x = in_x + random.randrange(-20, 20, 1)
        self.rect.y = in_y + random.randrange(-20, 20, 1)

        self.speed_x = in_dx + random.randrange(-2, 2, 1)
        self.speed_y = in_dy + random.randrange(-2, 2, 1)

        # add self to sprite lists
        GAME_SPRITES.add(self)
        ASTEROIDS.add(self)

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

    def kill(self):
        # remove self form game sprites
        GAME_SPRITES.remove(self)
        # remove self from asteroids
        ASTEROIDS.remove(self)

