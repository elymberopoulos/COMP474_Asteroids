import unittest

from test.asteroid import test_asteroid, test_smallAsteroid
from test.player import test_player
from test.alien import test_alien
from test.gameManager import test_gameManager
from test.spriteCount import test_spriteCount

"""
This is a test suite for this project.
The different test classes are loaded from their respective sub-directories
and added to the suite variable. The suite variable is then run. This provides
a centralized way to run all tests through the command line.
"""

loader = unittest.TestLoader()
suite = unittest.TestSuite()

suite.addTests(loader.loadTestsFromModule(test_asteroid))
suite.addTests(loader.loadTestsFromModule(test_smallAsteroid))
suite.addTests(loader.loadTestsFromModule(test_player))
suite.addTests(loader.loadTestsFromModule(test_alien))
suite.addTests(loader.loadTestsFromModule(test_spriteCount))
suite.addTests(loader.loadTestsFromModule(test_gameManager))

runner = unittest.TextTestRunner(verbosity=3)
runner.run(suite)