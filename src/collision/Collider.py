import sys
from Weapon import *
from Constants import *
import os


class Collider:

    def __init__(self, in_player, in_player_lives, in_game_manager):
        # get the current game manager
        self.game_manager = in_game_manager
        # the player's score!
        self.score = 0
        # initialize the player
        self.player = in_player
        # initialise the number of player lives
        self.lives = in_player_lives
        # the number of asteroids to spawn once all asteroids have been destroyed
        self.number_of_asteroids_to_spawn = ASTEROIDS_AT_START

        # sounds
        # explosion sound effect
        self.EXPLOSION_EFFECT = pygame.mixer.Sound(os.path.join(AUDIO_DIR, 'explosion.wav'))
        # classic wilhelm scream because why not?
        self.WILHELM_SCREAM = pygame.mixer.Sound(os.path.join(AUDIO_DIR, 'wilhelm_scream.wav'))

    def check_collisions(self):

        # --------------------------------------------------------------------------------------------------------------
        # collision between alien projectiles and asteroids
        asteroid_alien_bullet_collision = pygame.sprite.groupcollide(ASTEROIDS, ALIEN_PROJECTILES, True, True)

        # --------------------------------------------------------------------------------------------------------------
        # collision between alien and player projectiles
        alien_player_projectile_collision = pygame.sprite.groupcollide(ALIEN, PLAYER_PROJECTILES, True, True)

        for collision in alien_player_projectile_collision:
            # increment score
            self.score += 10
            # play explosion sound effect
            self.EXPLOSION_EFFECT.play()

        # --------------------------------------------------------------------------------------------------------------
        # collision between asteroids and projectiles
        asteroid_player_bullet_collision = pygame.sprite.groupcollide(ASTEROIDS, PLAYER_PROJECTILES, True, True)

        for collision in asteroid_player_bullet_collision:
            # increment score
            self.score += 10
            # play explosion sound effect
            self.EXPLOSION_EFFECT.play()
            # if 0 is greater than or equal to the number of asteroids then we need to spawn more asteroids!
            if 0 >= ASTEROIDS.__len__():
                # the number of asteroids to spawn increases
                self.number_of_asteroids_to_spawn += ASTEROIDS_INCREMENT
                # use the game manager to spawn the number of asteroids we want
                self.game_manager.create_asteroid(self.number_of_asteroids_to_spawn)

                # TODO kill all aliens on screen

        if not self.player.invincible:
            # Check for player collisions with asteroids
            player_asteroid_collisions = pygame.sprite.spritecollide(self.player, ASTEROIDS, False, pygame.sprite.collide_circle)
            # Check for player collisions with aliens
            player_alien_collisions = pygame.sprite.spritecollide(self.player, ALIEN_PROJECTILES, False, pygame.sprite.collide_circle)

            if player_asteroid_collisions or player_alien_collisions:

                # player looses a life
                self.lives -= 1

                # play the wilhelm scream!
                self.WILHELM_SCREAM.play()

                # if 0 is greater than or equal to the number of lives
                if 0 >= self.lives:
                    # exit the game
                    self.game_exit()

                # the player is now invincible
                self.player.invincible = True
                # set the amount of time the player is invincible for
                self.player.invincible_timer = PLAYER_INVINCIBILITY_TIME
                # remove the player from the game sprites
                GAME_SPRITES.remove(self.player)

            if alien_player_projectile_collision:
                self.score += 50
                self.EXPLOSION_EFFECT.play()

        # if the player is invincible and zero is less than or equal to the invincible_timer
        elif self.player.invincible and 0 < self.player.invincible_timer:
            # decrement the invincibility timer
            self.player.invincible_timer -= 1

            # if zero is greater than or equal to the invincibility timer
            if 0 >= self.player.invincible_timer:
                # set the player to be no longer invincible
                # self.player.invincible = False
                # start the safe timer for safey after respawn
                self.player.safe_timer = PLAYER_SAFETY_TIME
                # add the player back to the game sprites
                GAME_SPRITES.add(self.player)
                # set the player's speed to zero
                self.player.vel = vec(0, 0)
                # set the player to be at the center of the screen
                self.player.pos = vec(WIN_WIDTH/2, WIN_HEIGHT/2)

        # if the player is invincible and zero is less than or equal to the safe_timer
        elif self.player.invincible and 0 < self.player.safe_timer:
            # decrement the safe timer
            self.player.safe_timer -= 1

            # check if the timer has elapsed
            if 0 >= self.player.safe_timer:
                # set the player to be no longer invincible
                self.player.invincible = False

    def game_exit(self):
        pygame.quit()
        sys.exit(0)
