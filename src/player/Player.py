from WeaponList import *
from Constants import *
import copy
import os

vec = pygame.math.Vector2


class Player(pygame.sprite.Sprite):

    def __init__(self):
        # Import the weapon sound effect
        self.weapon_sound = pygame.mixer.Sound(os.path.join(AUDIO_DIR, 'fire.wav'))

        pygame.sprite.Sprite.__init__(self)

        # ship without engine
        self.ship_without_engine = pygame.image.load(os.path.join(IMG_DIR, "Ship_Without_Engine.png")).convert_alpha()
        # ship without engine reference image of the player for rotation
        self.ship_without_engine_ref = pygame.image.load(os.path.join(IMG_DIR, "Ship_Without_Engine.png")).convert_alpha()

        # ship without engine
        self.ship_with_engine = pygame.image.load(os.path.join(IMG_DIR, "Ship_With_Engine.png")).convert_alpha()
        # ship with engine reference image of the player for rotation
        self.ship_with_engine_ref = pygame.image.load(os.path.join(IMG_DIR, "Ship_With_Engine.png")).convert_alpha()

        # sprite image of the player
        self.image = self.ship_without_engine
        # reference image of the player for rotation
        self.reference_image = self.ship_without_engine_ref

        # get the current rectangle from the sprite
        self.rect = self.image.get_rect()

        # set the center of the sprite
        self.rect.center = (WIN_WIDTH / 2, WIN_HEIGHT / 2)

        # position
        self.pos = vec(WIN_WIDTH / 2, WIN_HEIGHT / 2)
        # velocity
        self.vel = vec(0, 0)
        # acceleration
        self.acc = vec(0, 0)
        # direction
        self.dir = vec(1, 0)
        # angle of the player
        self.angle = 0

        self.invincible = False
        self.invincible_timer = 0
        self.safe_timer = 0

        # add the player to the current game sprites
        GAME_SPRITES.add(self)

    def fire_weapon(self, in_weapon):
        # check if the number of projectiles on the screen is less than the number of max projectiles
        if in_weapon.WEAPON_PROJECTILES < in_weapon.WEAPON_MAX_PROJECTILES:
            # check if the weapon has cooled down
            if pygame.sprite.get_ticks() - in_weapon.WEAPON_COOL_BEGIN > in_weapon.WEAPON_COOLDOWN_TIME:
                # create a new projectile. The projectile starting conditions are the same as the ship's
                # position, velocity, and direction. A deep copy was used to affect a pass by value rather than a
                # pass by reference.
                current_weapon = in_weapon(copy.deepcopy(self.pos), copy.deepcopy(self.vel), vec(0, -1).rotate(-self.angle), PLAYER_PROJECTILES)
                in_weapon.WEAPON_COOL_BEGIN = pygame.sprite.get_ticks()
                # print(in_weapon.WEAPON_NAME + " : " + in_weapon.WEAPON_PROJECTILES.__str__())

                self.weapon_sound.play()

    def rotate(self, angle):
        self.image = pygame.transform.rotate(self.reference_image, angle)
        self.rect = self.image.get_rect()
        self.dir = vec(0, 1).rotate(angle)

    def update(self, *args):

        # set the default sprite to the ship without engine
        self.image = self.ship_without_engine
        self.reference_image = self.ship_without_engine_ref

        # reset the acceleration to zero
        self.acc = vec(0, 0)

        # collect the key presses
        keys = pygame.key.get_pressed()

        # check left key press
        if keys[pygame.K_LEFT]:
            self.angle += PLAYER_ANGLE_VEL

        # check the right key press
        if keys[pygame.K_RIGHT]:
            self.angle -= PLAYER_ANGLE_VEL

        # check the up key press to see if we need to swap the ship's sprite out for the one with the engine
        if keys[pygame.K_UP]:
            self.image = self.ship_with_engine
            self.reference_image = self.ship_with_engine_ref

        # rotate the ship's direction and sprite which needs to be resolved before we calculate the linear motion
        self.rotate(self.angle)

        # check the up key press again to resolve the acceleration after rotation
        if keys[pygame.K_UP]:
            self.acc.x += PLAYER_ACC * self.dir.x
            self.acc.y += -PLAYER_ACC * self.dir.y

        # check the space bar
        if keys[pygame.K_SPACE]:
            self.fire_weapon(WeaponGun)
        # apply friction
        self.acc += self.vel * PLAYER_FRICTION

        # motion equations
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        # wrap around the sides of the screen
        if self.pos.x > WIN_WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIN_WIDTH
        if self.pos.y > WIN_HEIGHT:
            self.pos.y = 0
        if self.pos.y < 0:
            self.pos.y = WIN_HEIGHT

        # update the position
        self.rect.center = self.pos










