import pygame
import random
import Constants
import os

"""

******************************************************************************** |
THE CODE FOR THIS CLASS NEEDS TO BE ALTERED TO SPAWN ON A DESTROYED BIG ASTEROID |
******************************************************************************** |

"""


class SmallAsteroid(pygame.sprite.Sprite):

    # small asteroid takes in the x and y position as a starting location
    def __init__(self, in_x, in_y):
        pygame.sprite.Sprite.__init__(self)

        # self.asteroidImage = pygame.image.load(os.path.join(Constants.IMG_DIR, "Asteroid_1.PNG")).convert_alpha()
       # self.image = self.asteroidImage

        self.image = pygame.Surface((10, 10))

        self.image.fill((150, 150, 150))
        self.rect = self.image.get_rect()

        # Set start location and speeds
        self.rect.x = in_x # random.randrange(Constants.WIN_WIDTH - self.rect.width)
        self.rect.y = in_y    # random.randrange(-100, -50)
        self.speed_y = random.randrange(1, 4)
        self.speed_x = random.randrange(-2, 2)

        Constants.GAME_SPRITES.add(self)
        Constants.ASTEROIDS.add(self)

    def update(self):
        # self.image = self.asteroidImage
        self.rect.y += self.speed_y
        self.rect.x += self.speed_x

        if self.rect.top > Constants.WIN_HEIGHT + 15 or self.rect.left < -15 or self.rect.right > Constants.WIN_WIDTH:
            self.rect.x = random.randrange(
                Constants.WIN_WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -50)
            self.speed_y = random.randrange(1, 4)
            self.speed_x = random.randrange(-2, 2)

