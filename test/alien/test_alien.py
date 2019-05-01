import unittest

from src.asteroid import Asteroid, SmallAsteroid
from src.alien import Alien
from Constants import *
from WeaponList import *
import pygame
vec = pygame.math.Vector2

class TestAlien(unittest.TestCase):

    def test_alienVelocity(self):
        # BVA test for the alien ship's velocity.
        # It is ran through a loop for better coverage due to the random nature of the game
        pygame.init()
        window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

        for i  in range(50):

            alien = Alien.Alien()
            velocity = alien.vel
            self.assertNotEqual(vec(1,0), velocity)
            self.assertNotEqual(vec(1,5), velocity)
            alien.kill()

        GAME_SPRITES.empty()
        pygame.quit()

    def test_alienAngle(self):
        # Test for the alien ship's angle.
        # The angle should be 0
        pygame.init()
        window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        alien = Alien.Alien()
        self.assertEqual(0, alien.angle)

        GAME_SPRITES.empty()
        pygame.quit()

    def test_alienCenter(self):
        # Test for the alien ship's angle.
        # The angle should be 0
        pygame.init()
        window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        alien = Alien.Alien()
        self.assertEqual(0, alien.angle)

        GAME_SPRITES.empty()
        pygame.quit()

    def test_alienSpriteCount(self):
        #Spawn one alien ship and ensure the length of the game sprites group is one.
        pygame.init()
        window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

        alien = Alien.Alien()
        self.assertEqual(1, len(GAME_SPRITES.sprites()))

        GAME_SPRITES.empty()
        pygame.quit()

    def test_alienSpriteCount(self):
        # Spawn one alien ship and have it fire one projectile.
        # This will ensure that a bullet sprite is added to the game sprite group
        pygame.init()
        window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

        alien = Alien.Alien()
        alien.fire_weapon(Weapon)
        self.assertEqual(2, len(GAME_SPRITES.sprites()))
        self.assertEqual(1, len(PROJECTILES.sprites()))

        GAME_SPRITES.empty()
        pygame.quit()