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

        if not self.player.invincible:
            # Check for player collisions with asteroids
            player_asteroid_collisions = pygame.sprite.spritecollide(self.player, ASTEROIDS, False, pygame.sprite.collide_circle)
            # Check for player collisions with aliens
            player_alien_collisions = pygame.sprite.spritecollide(self.player, ALIEN_PROJECTILES, False, pygame.sprite.collide_circle)

            if player_asteroid_collisions or player_alien_collisions:
                # self.print_score()

                # player looses a life
                self.lives -= 1

                # play the wilhelm scream!
                wilhelm_scream.play()

                # if 0 is greater than or equal to the number of lives
                if 0 >= self.lives:
                    # exit the game
                    self.game_exit()

                # the player is now invincible
                self.player.invincible = True
                # set the amount of time the player is invincible for
                self.player.invincible_timer = 100
                # remove the player from the game sprites
                GAME_SPRITES.remove(self.player)

            if alien_player_projectile_collision:
                self.score += 50
                explosion_effect.play()

        # if the player is invincible
        elif self.player.invincible:
            # deccrament the invinciblity timer
            self.player.invincible_timer -= 1

            # if zero is greater than or equal to the invinciblity timer
            if 0 >= self.player.invincible_timer:
                # set the player to be no longer invincible
                self.player.invincible = False
                # add the player back to the game sprites
                GAME_SPRITES.add(self.player)
                # set the player's speed to zero
                self.player.vel = vec(0, 0)
                # set the player to be at the center of the screen
                self.player.pos = vec(WIN_WIDTH/2, WIN_HEIGHT/2)


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
