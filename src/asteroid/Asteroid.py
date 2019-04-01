import pygame, random
import Constants

"""
This class of asteroids spawn at the top of the screen and move to the bottom side of the window.
"""

class Asteroid(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        if self.randomSize():
            self.image = pygame.Surface((20,20))
        else:
            self.image = pygame.Surface((35,35))
        self.image.fill((150, 150, 150))
        self.rect = self.image.get_rect()

        # Set start location and speeds
        self.rect.x = random.randrange(Constants.WIN_WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -50)
        self.speed_y = random.randrange(1, 4)
        self.speed_x = random.randrange(-2, 2)

        Constants.GAME_SPRITES.add(self)
        Constants.ASTEROIDS.add(self)

    def update(self):
        self.rect.y += self.speed_y
        self.rect.x += self.speed_x

        if self.rect.top > Constants.WIN_HEIGHT + 15 or self.rect.left < -15 or self.rect.right > Constants.WIN_WIDTH:
            self.rect.x = random.randrange(Constants.WIN_WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -50)
            self.speed_y = random.randrange(1, 4)
            self.speed_x = random.randrange(-2, 2)

    def randomSize(self):
        percent = 50
        return random.randrange(100) < percent