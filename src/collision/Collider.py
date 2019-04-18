import sys
from src.asteroid.Asteroid import Asteroid
from src.asteroid.Asteroid2 import Asteroid2
from src.asteroid.Asteroid3 import Asteroid3
from Weapon import *
import random
import os
from Score import Score


class Collider:

    def __init__(self, in_player):

        self.score = 0
        self.score_board(0)
        self.player = in_player

    def check_collisions(self):

        bulletCollide = pygame.sprite.groupcollide(ASTEROIDS, PROJECTILES, True, False)
        alienTakedown = pygame.sprite.groupcollide(ALIEN, PLAYER_PROJECTILES, True, False)
        explosion_effect = pygame.mixer.Sound(os.path.join(AUDIO_DIR, 'explosion.wav'))
        self.PLAYER_LIVES = 3

        for collision in bulletCollide:

            self.score += 10
            explosion_effect.play()
            self.score_board(self.score)
            # Randomly spawn new asteroid from different sides of the screen
            newAstroid = random.randrange(0, 3)
            if newAstroid == 0:
                asteroid = Asteroid()
                # asteroid = Asteroid.Asteroid()
                ASTEROIDS.add(asteroid)
                GAME_SPRITES.add(asteroid)

            elif newAstroid == 1:
                asteroid = Asteroid2()
                # asteroid = Asteroid2.Asteroid2()
                ASTEROIDS.add(asteroid)
                GAME_SPRITES.add(asteroid)

            else:
                asteroid = Asteroid3()
                # asteroid = Asteroid3.Asteroid3()
                ASTEROIDS.add(asteroid)
                GAME_SPRITES.add(asteroid)

        # Check for player collisions with asteroids
        collisions = pygame.sprite.spritecollide(self.player, ASTEROIDS, False, pygame.sprite.collide_circle)
        aliencollide = pygame.sprite.spritecollide(self.player, ALIEN_PROJECTILES, False, pygame.sprite.collide_circle)

        if collisions or aliencollide:
            self.print_score()
            self.game_exit()
        if alienTakedown:
            self.score += 50
            explosion_effect.play()

    def game_exit(self):
        pygame.quit()
        sys.exit(0)

    def score_board(self, points):
        text_file = open("Score_tracker.txt", "a")
        text_file.writelines(str(points) + "\n")
        text_file.close()

    def print_score(self):
        score = Score()
        # score = Score.Score()
        score.print_score()
        score.clear_score()
