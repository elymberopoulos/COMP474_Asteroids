import unittest
from src.player import Player
from src.asteroid import Asteroid
from Constants import *
from WeaponList import *
import pygame
import time

class TestSpriteCounter(unittest.TestCase):

    def test_AsteroidDestruction(self):
        pygame.init()
        window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        player = Player.Player()
        asteroid = Asteroid.Asteroid()
        self.assertEqual(len(GAME_SPRITES), 2)

        # Set the location of the asteroid so it collides with bullet
        asteroid.rect.x = player.rect.x - 15
        asteroid.rect.y = player.rect.y - 45
        player.fire_weapon(WeaponGun)
        self.assertEqual(len(GAME_SPRITES), 3)
        # update sprites to see if it collides
        # for i in range(100):
        #     GAME_SPRITES.update()
        #     PROJECTILES.update()
        # self.assertEqual(len(GAME_SPRITES), 2)
        GAME_SPRITES.empty()
        PROJECTILES.empty()
        pygame.quit()


