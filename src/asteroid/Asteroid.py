import pygame, random
 

"""
This class of asteroids spawn at the top of the screen and move to the bottom side of the window.
"""

class Asteroid(pygame.sprite.Sprite):
    def __init__(self, windowWidth, windowHeight):
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20,20))
        self.image.fill((150,150,150))
        self.rect = self.image.get_rect()
        #Set start location and speeds
        self.rect.x = random.randrange(windowWidth - self.rect.width)
        self.rect.y = random.randrange(-100, -50)
        self.speed_y = random.randrange(1,4)
        self.speed_x = random.randrange(-2,2)

    def update(self):
        self.rect.y += self.speed_y
        self.rect.x += self.speed_x

        if self.rect.top > self.windowHeight + 15 or self.rect.left < -15 or self.rect.right > self.windowWidth:
            self.rect.x = random.randrange(self.windowWidth - self.rect.width)
            self.rect.y = random.randrange(-100, -50)
            self.speed_y = random.randrange(1,4)
            self.speed_x = random.randrange(-2,2)