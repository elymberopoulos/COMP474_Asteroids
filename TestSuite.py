import unittest

from test.asteroid import test_asteroid, test_asteroid2, test_asteroid3
from test.player import test_player
from test.spriteCount import test_spriteCount

loader = unittest.TestLoader()
suite = unittest.TestSuite()

suite.addTests(loader.loadTestsFromModule(test_asteroid))
suite.addTests(loader.loadTestsFromModule(test_asteroid2))
suite.addTests(loader.loadTestsFromModule(test_asteroid3))
suite.addTests(loader.loadTestsFromModule(test_player))
suite.addTests(loader.loadTestsFromModule(test_spriteCount))

runner = unittest.TextTestRunner(verbosity=3)
runner.run(suite)