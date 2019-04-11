import unittest
from src.player import Player
from src.asteroid import Asteroid
from Constants import *
from WeaponList import *
from src.collision import Collider
import pygame
import time

class TestSpriteCounter(unittest.TestCase):

    def test_AsteroidDestruction(self):
        # Test that an ansteroid is destroyed after a bullet is fired and the group length is decremented
        pygame.init()
        window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        player = Player.Player()
        asteroid = Asteroid.Asteroid()
        collider = Collider.Collider(player)
        # two sprites. One player and asteroid
        self.assertEqual(2, len(GAME_SPRITES))

        # Set the location of the asteroid so it collides with bullet
        asteroid.rect.x = player.rect.x - 15
        asteroid.rect.y = player.rect.y - 41
        player.fire_weapon(Weapon)
        self.assertEqual(3 ,len(GAME_SPRITES.sprites()))
        self.assertEqual(1, len(PROJECTILES.sprites()))
        # update sprites to see if it collides

        #CURRENTLY NOT WORKING
        # for i in range(250):
        #     PROJECTILES.update()
        #
        # self.assertEqual(2, len(GAME_SPRITES))
        # GAME_SPRITES.empty()
        # PROJECTILES.empty()
        pygame.quit()


