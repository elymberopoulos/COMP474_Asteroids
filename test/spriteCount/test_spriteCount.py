import unittest

from src.gameManager import Manager
from WeaponList import *



class TestSpriteCounter(unittest.TestCase):

    # The below test was an attempt to implement collision detection within the game

    # def test_AsteroidDestruction(self):
    #     # Test that an ansteroid is destroyed after a bullet is fired and the group length is decremented
    #     pygame.init()
    #     window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    #     player = Player.Player()
    #     asteroid = Asteroid.Asteroid()
    #     collider = Collider.Collider(player)
    #     asteroidLIST = ASTEROIDS.sprites()
    #     gameSpriteLIST = GAME_SPRITES.sprites()
    #     # two sprites. One player and asteroid
    #     self.assertEqual(2, len(GAME_SPRITES))
    #
    #
    #     # GAME_SPRITES.update()
    #     player.fire_weapon(Weapon)
    #     self.assertEqual(3 ,len(GAME_SPRITES.sprites()))
    #     self.assertEqual(1, len(PROJECTILES.sprites()))
    #     bullets = PROJECTILES
    #     firedBullet = PROJECTILES.sprites()[0]
    #     # Set the location of the asteroid so it collides with bullet
    #     asteroid.rect.x = 120
    #     asteroid.rect.y = 120
    #     firedBullet.pos.x = 130
    #     firedBullet.pos.y = 135
    #     for i in range(100):
    #         PROJECTILES.update()
    #         GAME_SPRITES.update()
    #         ASTEROIDS.update()
    #         collider.check_collisions()
    #         # update sprites to see if it collides
    #
    #     self.assertEqual(3, len(ASTEROIDS.sprites()))
    #     GAME_SPRITES.empty()
    #     ASTEROIDS.empty()
    #     PROJECTILES.empty()
    #     pygame.quit()

    def test_AsteroidInit(self):
        #Tests that the game manager is adding the correct amount of asteroids to the game.
        pygame.init()
        window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        gameManager = Manager.Manager()
        gameManager.create_asteroid(7)
        self.assertEqual(7, len(GAME_SPRITES.sprites()))
        GAME_SPRITES.empty()
        pygame.quit()

    def test_AsteroidInitBVA(self):
        #BVA test to make sure that the game manager is not adding any extra or fewer asteroids to the game.
        pygame.init()
        window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        gameManager = Manager.Manager()
        gameManager.create_asteroid(10)
        self.assertNotEqual(9, len(GAME_SPRITES.sprites()))
        self.assertNotEqual(11, len(GAME_SPRITES.sprites()))
        GAME_SPRITES.empty()
        pygame.quit()
