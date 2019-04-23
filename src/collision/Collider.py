import sys
from src.asteroid.Asteroid import Asteroid
from src.asteroid.Asteroid2 import Asteroid2
from src.asteroid.Asteroid3 import Asteroid3
from Weapon import *
from Constants import *
import random
import os
from Score import Score


class Collider:

    def __init__(self, in_player, in_player_lives):

        self.score = 0
        self.score_board(0)

        # initialize the player
        self.player = in_player

        # initialise the number of player lives
        self.lives = in_player_lives

    def check_collisions(self):

        # collision between asteroids and projectiles
        asteroid_bullet_collision = pygame.sprite.groupcollide(ASTEROIDS, PROJECTILES, True, False)

        # collision between alien and player projectiles
        alien_player_projectile_collision = pygame.sprite.groupcollide(ALIEN, PLAYER_PROJECTILES, True, False)

        # explosion sound effect
        explosion_effect = pygame.mixer.Sound(os.path.join(AUDIO_DIR, 'explosion.wav'))

        # classic wilhelm scream because why not?
        wilhelm_scream = pygame.mixer.Sound(os.path.join(AUDIO_DIR, 'wilhelm_scream.wav'))

        for collision in asteroid_bullet_collision:

            # incrament score
            self.score += 10

            # play explosion sound effect
            explosion_effect.play()

            # update score board
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
        player_asteroid_collisions = pygame.sprite.spritecollide(self.player, ASTEROIDS, False, pygame.sprite.collide_circle)
        # Check for player collisions with aliens
        player_alien_collisions = pygame.sprite.spritecollide(self.player, ALIEN_PROJECTILES, False, pygame.sprite.collide_circle)

        if player_asteroid_collisions or player_alien_collisions:
            self.print_score()

            self.lives -= 1
            wilhelm_scream.play()
            self.player.pos = vec(WIN_WIDTH/2, WIN_HEIGHT/2)

            #self.game_exit()

        if alien_player_projectile_collision:
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
