import unittest

from src.player import Player
from WeaponList import *
import pygame
import time
vec = pygame.math.Vector2


class TestPlayer(unittest.TestCase):

    def test_StartPosition(self):
        pygame.init()
        window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        player = Player.Player()
        #Test start position of the player
        self.assertEqual(player.pos, (WIN_WIDTH/2, WIN_HEIGHT/2))
        GAME_SPRITES.empty()
        # pygame.quit()

    def test_StartVelocity(self):
        #Test that a player's initial velocity is (0,0) with its vector
        pygame.init()
        window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        player = Player.Player()
        self.assertEqual(vec(0,0), player.vel)
        GAME_SPRITES.empty()
        # pygame.quit()


    def test_StartVelocity(self):
        #Test that a player's initial velocity is (0,0) with its vector
        pygame.init()
        window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        player = Player.Player()
        self.assertEqual(vec(0,0), player.vel)
        GAME_SPRITES.empty()
        pygame.quit()

    def test_StartAcceleration(self):
        #Test that a player's initial acceleration is (0,0) with its vector
        pygame.init()
        window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        player = Player.Player()
        self.assertEqual(vec(0,0), player.acc)
        GAME_SPRITES.empty()
        pygame.quit()

    def test_StartDirection(self):
        #Test that a player's initial acceleration is (0,0) with its vector
        pygame.init()
        window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        player = Player.Player()
        self.assertEqual(vec(1,0), player.dir)
        GAME_SPRITES.empty()

        pygame.quit()

    def test_PlayerRotation(self):
        #Test that a player's rotation is handled correctly.
        #A rotation of 10 degrees will result in a 2d vector of (-0.173648,0.984808)
        pygame.init()
        window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        player = Player.Player()
        #The default direction for the player.
        self.assertEqual(vec(1,0), player.dir)
        #Rotate the player
        player.rotate(10)
        #The direction of the player after rotation by 10 degrees
        self.assertEqual(vec(-0.173648,0.984808), player.dir)

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
            time.sleep(.07)
            player.fire_weapon(Weapon)
            GAME_SPRITES.update()
            PROJECTILES.update()

        self.assertEqual(3, len(PROJECTILES.sprites()))

        GAME_SPRITES.empty()
        PROJECTILES.empty()
        pygame.quit()
