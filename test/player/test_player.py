from unittest import TestCase
from src.player import Player
from Constants import *
from WeaponList import *
import pygame

class TestPlayer(TestCase):

    def test_StartPosition(self):
        pygame.init()
        window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        player = Player.Player()

        #Test start position of the player
        self.assertEqual(player.pos, (WIN_WIDTH/2, WIN_HEIGHT/2))

        #BVA tests for player start position
        self.assertNotEqual(player.pos, (WIN_WIDTH/2 + 1, WIN_HEIGHT/2 + 1))
        self.assertNotEqual(player.pos, (WIN_WIDTH/2 - 1, WIN_HEIGHT/2 - 1))


    #Not working Try to fix
    # def test_Shoot(self):
    #     pygame.init()
    #     window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    #     player = Player.Player()
    #     player.fire_weapon(WeaponGun())
    #     self.assertEqual(len(PROJECTILES), 1)

