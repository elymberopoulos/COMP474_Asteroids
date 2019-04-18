import unittest
from src.asteroid import Asteroid3
from Constants import *
import pygame

class TestAsteroid3(unittest.TestCase):

    def test_size(self):
        # Test that the asteroid sprites are the correct size
        pygame.init()
        window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        asteroid = Asteroid3.Asteroid3()
        height = asteroid.image.get_height()
        width = asteroid.image.get_width()
        self.assertEqual(40, height)
        self.assertEqual(40, width)
        GAME_SPRITES.empty()
        # pygame.quit()

    def test_incorrectSizes(self):
        # Test the BVA values for asteroid sizes and assert they are not equal
        pygame.init()
        window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        asteroid = Asteroid3.Asteroid3()
        height = asteroid.image.get_height()
        width = asteroid.image.get_width()

        #BVA test for asteroid sizes
        self.assertNotEqual(39, height)
        self.assertNotEqual(41, height)
        self.assertNotEqual(39, width)
        self.assertNotEqual(41, width)
        GAME_SPRITES.empty()
        # pygame.quit()

    def test_startLocation(self):
        pygame.init()
        window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        for i in range(100):
            asteroid = Asteroid3.Asteroid3()
            self.assertFalse(asteroid.rect.y < 0)
            self.assertFalse(asteroid.rect.y > (WIN_HEIGHT - 100) + 1)
            GAME_SPRITES.empty()
        # pygame.quit()

    def test_update(self):
        #Test that the asteroid is moving as expected.
        #Save start location update a frame then assert that the new location has changed

        pygame.init()
        window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        asteroid = Asteroid3.Asteroid3()
        starting_y = asteroid.rect.y
        starting_x = asteroid.rect.x
        for i in range(5):
            asteroid.update()
        new_x = asteroid.rect.x
        new_y = asteroid.rect.y
        self.assertTrue(new_x < starting_x)

        GAME_SPRITES.empty()
        # pygame.quit()

    def test_Y_AxisSpeed(self):
        # this test is for making sure that the x-axis movement of the asteroid is within its accepted bounds
        pygame.init()
        window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        asteroid = Asteroid3.Asteroid3()
        starting_y = asteroid.speed_y

        # Update the frame for the asteroid once
        asteroid.update()
        new_y = asteroid.speed_y
        # Assert that the y-axis is not greater than or less than its allowed bounds
        self.assertFalse(new_y < starting_y - 2)
        self.assertFalse(new_y > starting_y + 3)
        GAME_SPRITES.empty()
        # pygame.quit()


