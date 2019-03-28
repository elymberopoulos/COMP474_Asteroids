import pygame
import random
from Constants import *


class Asteroid(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20, 20))
        self.image.fill((150, 150, 150))
        self.rect = self.image.get_rect()

        # Set start location and speeds
        self.rect.x = random.randrange(WIN_WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -50)
        self.speed_y = random.randrange(1, 4)
        self.speed_x = random.randrange(-2, 2)

        GAME_SPRITES.add(self)
        ASTEROIDS.add(self)

    def update(self):
        self.rect.y += self.speed_y
        self.rect.x += self.speed_x

        if self.rect.top > WIN_HEIGHT + 15 or self.rect.left < -15 or self.rect.right > WIN_WIDTH:
            self.rect.x = random.randrange(WIN_WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -50)
            self.speed_y = random.randrange(1, 4)
            self.speed_x = random.randrange(-2, 2)
