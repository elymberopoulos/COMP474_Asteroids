import unittest

from src.asteroid import Asteroid
from Constants import *
import pygame

class TestAsteroid(unittest.TestCase):

    def test_size(self):
        # Test that the asteroid sprites are the correct size
        pygame.init()
        window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        asteroid = Asteroid.Asteroid()
        height = asteroid.image.get_height()
        width = asteroid.image.get_width()
        self.assertEqual(50, height)
        self.assertEqual(50, width)
        GAME_SPRITES.empty()
        # pygame.quit()

    def test_incorrectSizes(self):
        # Test the BVA values for asteroid sizes and assert they are not equal
        pygame.init()
        window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        asteroid = Asteroid.Asteroid()
        height = asteroid.image.get_height()
        width = asteroid.image.get_width()

        #BVA test for asteroid sizes
        self.assertNotEqual(49, height)
        self.assertNotEqual(51, height)
        self.assertNotEqual(49, width)
        self.assertNotEqual(51, width)
        GAME_SPRITES.empty()
        # pygame.quit()

    def test_startLocation(self):
        pygame.init()
        window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        for i in range(100):
            asteroid = Asteroid.Asteroid()
            self.assertFalse(asteroid.rect.x < 0)
            self.assertFalse(asteroid.rect.x > (WIN_WIDTH - asteroid.rect.width) + 1)
            GAME_SPRITES.empty()
        # pygame.quit()

    def test_startLocation(self):
        pygame.init()
        window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        for i in range(100):
            asteroid = Asteroid.Asteroid()
            self.assertFalse(asteroid.rect.x < 0)
            self.assertFalse(asteroid.rect.x > WIN_WIDTH)
            GAME_SPRITES.empty()
        pygame.quit()


    def test_update(self):
        #Test that the asteroid is moving as expected.
        #Save start location update a frame then assert that the new location has changed

        pygame.init()
        window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        asteroid = Asteroid.Asteroid()
        starting_y = asteroid.rect.y
        for i in range(5):
            asteroid.update()
        new_y = asteroid.rect.y
        self.assertTrue(new_y != starting_y)

        GAME_SPRITES.empty()
        # pygame.quit()

    def test_X_AxisSpeed(self):
        # this test is for making sure that the x-axis movement of the asteroid is within its accepted bounds
        pygame.init()
        window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        asteroid = Asteroid.Asteroid()
        starting_x = asteroid.speed_x

        # Update the frame for the asteroid once
        asteroid.update()
        new_x = asteroid.speed_x
        # Assert that the x-axis is not greater than or less than its allowed bounds
        self.assertFalse(new_x < starting_x - 2)
        self.assertFalse(new_x > starting_x + 2)
        GAME_SPRITES.empty()
        # pygame.quit()



