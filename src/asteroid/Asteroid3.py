import pygame, random
import Constants
"""
This class of asteroids spawn at the right side of the screen and move to the left side of the window.
"""

class Asteroid3(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        if self.randomSize():
            self.image = pygame.Surface((20,20))
        else:
            self.image = pygame.Surface((35,35))
        self.image.fill((150,150,150))
        self.rect = self.image.get_rect()
        #Set start location and speeds
        self.rect.x = Constants.WIN_WIDTH + 20
        self.rect.y = random.randrange(0, Constants.WIN_HEIGHT-100)
        self.speed_y = random.randrange(-2,2)
        self.speed_x = random.randrange(-3,-1)

        Constants.GAME_SPRITES.add(self)
        Constants.ASTEROIDS.add(self)

    def update(self):
        self.rect.y += self.speed_y
        self.rect.x += self.speed_x

        if self.rect.top > Constants.WIN_HEIGHT + 15 or self.rect.left < -15 or self.rect.right > Constants.WIN_WIDTH:
            self.rect.x = Constants.WIN_WIDTH - 35
            self.rect.y = random.randrange(0, Constants.WIN_HEIGHT-100)
            self.speed_y = random.randrange(-2,2)
            self.speed_x = random.randrange(-3,-1)

    def randomSize(self):
        percent = 50
        return random.randrange(100) < percent