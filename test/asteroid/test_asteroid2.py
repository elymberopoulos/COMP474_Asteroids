from unittest import TestCase
from src.asteroid import Asteroid2
from Constants import *
import pygame

class TestAsteroid2(TestCase):

    def test_size(self):
        pygame.init()
        window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        asteroid = Asteroid2.Asteroid2()
        height = asteroid.image.get_height()
        width = asteroid.image.get_width()
        self.assertEqual(40, height)
        self.assertEqual(40, width)

    def test_incorrectSizes(self):
        pygame.init()
        window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        asteroid = Asteroid2.Asteroid2()
        height = asteroid.image.get_height()
        width = asteroid.image.get_width()

        #BVA test for asteroid sizes
        self.assertNotEqual(39, height)
        self.assertNotEqual(41, height)
        self.assertNotEqual(39, width)
        self.assertNotEqual(41, height)

    def test_update(self):
        #Test that the asteroid is moving as expected.
        #Save start location update a frame then assert that the new location has changed
        pygame.init()
        window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        asteroid = Asteroid2.Asteroid2()
        starting_y = asteroid.rect.y
        starting_x = asteroid.rect.x
        asteroid.update()
        new_x = asteroid.rect.x
        new_y = asteroid.rect.y
        self.assertTrue(new_x > starting_x)
        #Moves randomly in y-axis direction but it should not be the same as the previous frame
        self.assertNotEqual(starting_y, new_y)

