import pygame
import pygame.event
from src.ship import Ship
import sys
import random

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

class Asteroid2(pygame.sprite.Sprite):
    def __init__(self, windowWidth, windowHeight):
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20,20))
        self.image.fill((150,150,150))
        self.rect = self.image.get_rect()
        #Set start location and speeds
        self.rect.x = -20
        self.rect.y = random.randrange(0, windowHeight-100)
        self.speed_y = random.randrange(-2,2)
        self.speed_x = random.randrange(1,3)

    def update(self):
        self.rect.y += self.speed_y
        self.rect.x += self.speed_x

        if self.rect.top > self.windowHeight + 15 or self.rect.left < -15 or self.rect.right > self.windowWidth:
            self.rect.x = random.randrange(-20, -10)
            self.rect.y = random.randrange(0, self.windowHeight-100)
            self.speed_y = random.randrange(1,4)
            self.speed_x = random.randrange(1,3)

def gameExit():
    pygame.quit()
    sys.exit()

def main():
    #Setup basic variables and methods for pygame
    pygame.init()
    windowWidth = 800
    windowHeight = 700
    fps = 45
    clock = pygame.time.Clock()
    gameWindow = pygame.display.set_mode((windowWidth, windowHeight))
    pygame.display.set_caption("Asteroids")
    surface = pygame.Surface((50,50))
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    #SHIP POSITION
    shipX = windowWidth/2
    shipY = windowWidth/2
    shipSpeed = 4

    #Variables to keep track of sprites on the screen
    game_sprites = pygame.sprite.Group()
    asteroidsOnScreen = pygame.sprite.Group()
    for i in range(10):
        if i % 2 == 0:
            asteroid = Asteroid(windowWidth, windowHeight)
            game_sprites.add(asteroid)
            asteroidsOnScreen.add(asteroid)
        else:
            asteroid = Asteroid2(windowWidth, windowHeight)
            game_sprites.add(asteroid)
            asteroidsOnScreen.add(asteroid)

        

    while(True):
        
        #Possible bounding box for initial ship
        pygame.draw.ellipse(gameWindow, WHITE, (shipX, shipY, 20, 30))
        game_sprites.draw(gameWindow)
        game_sprites.update()
        #Draw Triangle
        # pygame.draw.lines(gameWindow, WHITE, True, ((400, 350), (450, 400), (350, 400), 1))
        pygame.display.update()

        #Monitor the FPS of the game
        clock.tick(fps)

        for event in pygame.event.get():
            # ________________________________________
            if event.type == pygame.QUIT:
                gameExit()
        
        rotate = 0
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]: shipY -= shipSpeed
        if pressed[pygame.K_DOWN]: shipY += shipSpeed
        if pressed[pygame.K_LEFT]: shipX -= shipSpeed
        if pressed[pygame.K_RIGHT]: shipX += shipSpeed
        if pressed[ord('a')]: rotate = pygame.transform.rotate(surface, -20)
        if pressed[ord('d')]: rotate = pygame.transform.rotate(surface, 20)

        gameWindow.fill(BLACK)
        # 'flip' display - always after drawing...
        pygame.display.flip()


if __name__ == '__main__':
    main()