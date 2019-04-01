import sys
from src.asteroid import Asteroid, Asteroid2, Asteroid3
from src.player import Player
from Constants import *
from Weapon import *
import random

class Collider:
    def __init__(self, player):
        bulletCollide = pygame.sprite.groupcollide(ASTEROIDS, PROJECTILES, True, False)
        for collision in bulletCollide:
            # Randomly spawn new asteroid from different sides of the screen
            newAstroid = random.randrange(0, 3)
            if newAstroid == 0:
                asteroid = Asteroid.Asteroid()
                ASTEROIDS.add(asteroid)
                GAME_SPRITES.add(asteroid)

            elif newAstroid == 1:
                asteroid = Asteroid2.Asteroid2()
                ASTEROIDS.add(asteroid)
                GAME_SPRITES.add(asteroid)

            else:
                asteroid = Asteroid3.Asteroid3()
                ASTEROIDS.add(asteroid)
                GAME_SPRITES.add(asteroid)

        # Check for player collisions with asteroids
        collisions = pygame.sprite.spritecollide(player, ASTEROIDS, False, pygame.sprite.collide_circle)
        if collisions:
            self.game_exit()

    def game_exit(slef):
        pygame.quit()
        sys.exit()