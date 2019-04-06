import sys
from src.asteroid import Asteroid, Asteroid2, Asteroid3
from src.player import Player
from Constants import *
from Weapon import *
import random
import os
import Score
class Collider:
    def __init__(self, player):

        bulletCollide = pygame.sprite.groupcollide(ASTEROIDS, PROJECTILES, True, False)
        explosion_effect = pygame.mixer.Sound(os.path.join(AUDIO_DIR, 'explosion.wav'))
        self.PLAYER_LIVES = 3
        for collision in bulletCollide:
            explosion_effect.play()
            self.score_board(10)
            # Randomly spawn new asteroid from different sides of the screen
            newAstroid = random.randrange(0, 3)
            if newAstroid == 0:
                asteroid = Asteroid.Asteroid()
                ASTEROIDS.add(asteroid)
                GAME_SPRITES.add(asteroid)

            elif newAstroid == 1:
                asteroid = Asteroid2.Asteroid2()
                ASTEROIDS.add(asteroid)
                GAME_SPRITES.add(asteroid)

            else:
                asteroid = Asteroid3.Asteroid3()
                ASTEROIDS.add(asteroid)
                GAME_SPRITES.add(asteroid)

        # Check for player collisions with asteroids
        collisions = pygame.sprite.spritecollide(player, ASTEROIDS, False, pygame.sprite.collide_circle)
        if collisions: 
            self.print_score()
            self.game_exit()
            

    def game_exit(self):
        pygame.quit()
        sys.exit(0)
    def score_board(self,points):
        text_file = open("Score_tracker.txt","a")
        text_file.writelines(str(points) + "\n")
        text_file.close()
    def print_score(self):
        score = Score.Score()
        score.print_score()
        score.clear_score()