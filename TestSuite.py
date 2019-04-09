import unittest

from test.asteroid import test_asteroid, test_asteroid2, test_asteroid3
from test.player import test_player

loader = unittest.TestLoader()
suite = unittest.TestSuite()

suite.addTests(loader.loadTestsFromModule(test_asteroid))
suite.addTests(loader.loadTestsFromModule(test_asteroid2))
suite.addTests(loader.loadTestsFromModule(test_asteroid3))
suite.addTests(loader.loadTestsFromModule(test_player))

runner = unittest.TextTestRunner(verbosity=3)
runner.run(suite)