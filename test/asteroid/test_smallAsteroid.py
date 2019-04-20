import unittest

from src.asteroid import Asteroid, SmallAsteroid
from Constants import *
import pygame

class TestSmallAsteroid(unittest.TestCase):

    def test_size(self):
        # Test that the asteroid sprites are the correct size
        pygame.init()
        window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        asteroid = SmallAsteroid.SmallAsteroid(WIN_WIDTH / 2, WIN_HEIGHT / 2)
        height = asteroid.image.get_height()
        width = asteroid.image.get_width()
        self.assertEqual(10, height)
        self.assertEqual(10, width)
        GAME_SPRITES.empty()
        pygame.quit()

    def test_incorrectSizes(self):
        # Test the BVA values for asteroid sizes and assert they are not equal
        pygame.init()
        window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        asteroid = SmallAsteroid.SmallAsteroid(WIN_WIDTH / 2, WIN_HEIGHT / 2)
        height = asteroid.image.get_height()
        width = asteroid.image.get_width()

        #BVA test for asteroid sizes
        self.assertNotEqual(9, height)
        self.assertNotEqual(11, height)
        self.assertNotEqual(9, width)
        self.assertNotEqual(11, width)
        GAME_SPRITES.empty()
        ASTEROIDS.empty()
        pygame.quit()

    def test_smallAsteroidSpawn(self):
        #Spawn one main asteroid then delete it. The asteroid sprite list should have a length of three.
        pygame.init()
        window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

        asteroid = Asteroid.Asteroid()
        asteroid.__del__()
        self.assertEqual(3, len(GAME_SPRITES.sprites()))

        GAME_SPRITES.empty()
        pygame.quit()


    def test_Y_AxisSpeed(self):
        # this test is for making sure that the x-axis movement of the asteroid is within its accepted bounds
        pygame.init()
        window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        asteroid = SmallAsteroid.SmallAsteroid(WIN_WIDTH / 2, WIN_HEIGHT / 2)
        starting_y = asteroid.speed_y

        # Update the frame for the asteroid once
        asteroid.update()
        new_y = asteroid.speed_y
        # Assert that the x-axis is not greater than or less than its allowed bounds
        self.assertFalse(new_y < starting_y - 2)
        self.assertFalse(new_y > starting_y + 2)
        GAME_SPRITES.empty()
        # pygame.quit()

    def test_X_AxisSpeed(self):
        # this test is for making sure that the x-axis movement of the asteroid is within its accepted bounds
        pygame.init()
        window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        asteroid = SmallAsteroid.SmallAsteroid(WIN_WIDTH / 2, WIN_HEIGHT / 2)
        starting_x = asteroid.speed_x

        # Update the frame for the asteroid once
        asteroid.update()
        new_x = asteroid.speed_x
        # Assert that the x-axis is not greater than or less than its allowed bounds
        self.assertFalse(new_x < starting_x - 2)
        self.assertFalse(new_x > starting_x + 2)
        GAME_SPRITES.empty()
        # pygame.quit()