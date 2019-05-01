import unittest

from src.gameManager import Manager
from WeaponList import *
import pygame
vec = pygame.math.Vector2

class TestGameManager(unittest.TestCase):

    def test_createOneAlien(self):
        # Test that the game manager creates one alien by measuring the length of the game sprites group
        pygame.init()
        window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

        manager = Manager.Manager()
        manager.create_alien(1)
        self.assertEqual(1, len(GAME_SPRITES.sprites()))
        GAME_SPRITES.empty()
        pygame.quit()

    def test_createTwoAliens(self):
        # Test that the game manager creates two aliens by measuring the length of the game sprites group
        pygame.init()
        window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

        manager = Manager.Manager()
        manager.create_alien(2)
        self.assertEqual(2, len(GAME_SPRITES.sprites()))
        GAME_SPRITES.empty()
        pygame.quit()

    def test_createOneAsteroid(self):
        # Test that the game manager creates one asteroid by measuring the length of the game sprites group
        pygame.init()
        window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

        manager = Manager.Manager()
        manager.create_asteroid(1)
        self.assertEqual(1, len(GAME_SPRITES.sprites()))
        GAME_SPRITES.empty()
        pygame.quit()

    def test_createTwoAsteroids(self):
        # Test that the game manager creates two asteroids by measuring the length of the game sprites group
        pygame.init()
        window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

        manager = Manager.Manager()
        manager.create_asteroid(2)
        self.assertEqual(2, len(GAME_SPRITES.sprites()))
        GAME_SPRITES.empty()
        pygame.quit()