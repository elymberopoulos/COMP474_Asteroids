import unittest
from src import Player
from Constants import *
from WeaponList import *
import pygame
import time

class TestPlayer(unittest.TestCase):

    def test_StartPosition(self):
        pygame.init()
        window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        player = Player.Player()

        #Test start position of the player
        self.assertEqual(player.pos, (WIN_WIDTH/2, WIN_HEIGHT/2))
        GAME_SPRITES.empty()
        pygame.quit()


    def test_Shoot(self):
        #Check that one projectile has been added to the PROJECTILES list after firing the weapon

        pygame.init()
        window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        player = Player.Player()
        player.fire_weapon(Weapon)
        self.assertEqual(1, len(PROJECTILES.sprites()))
        GAME_SPRITES.update()
        GAME_SPRITES.empty()
        PROJECTILES.empty()
        pygame.quit()

    def test_ShootLimit(self):
        # Test that projectile limit is being limited correctly

        pygame.init()
        window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        player = Player.Player()

        #Fire the weapon 5 times. The projectiles group should still be 3.
        for i in range(5):
            time.sleep(.05)
            player.fire_weapon(Weapon)
            GAME_SPRITES.update()
            PROJECTILES.update()

        self.assertEqual(3, len(PROJECTILES.sprites()))

        GAME_SPRITES.empty()
        PROJECTILES.empty()
        pygame.quit()
