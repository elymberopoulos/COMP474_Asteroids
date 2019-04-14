import unittest

from test.asteroid import test_asteroid, test_asteroid2, test_asteroid3
from test.player import test_player
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
suite.addTests(loader.loadTestsFromModule(test_asteroid2))
suite.addTests(loader.loadTestsFromModule(test_asteroid3))
suite.addTests(loader.loadTestsFromModule(test_player))
suite.addTests(loader.loadTestsFromModule(test_spriteCount))

runner = unittest.TextTestRunner(verbosity=3)
runner.run(suite)