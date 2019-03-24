import pygame
import random

class Asteroid(pygame.sprite.Sprite):
    def __init__(self, windowWidth):
        self.windowWidth = windowWidth
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20,20))
        self.image.fill((0,0,0))
        self.rect = self.image.get_rect()
        #Set start location and speeds
        self.rect.x = random.randrange(windowWidth - self.rect.width)
        self.rect.y = random.randrange(-100, -50)
        self.speed_y = random.randrange(1,10)

    def update(self):
        self.rect.y += self.speed_y

        if self.rect.top > self.windowHeight + 15:
            self.rect.x = random.randrange(self.windowWidth - self.rect.width)
            self.rect.y = random.randrange(-100, -50)
            self.speed_y = random.randrange(1,10)