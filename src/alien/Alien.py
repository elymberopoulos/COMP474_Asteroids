import Constants
from WeaponList import *
import copy
import os
vec = pygame.math.Vector2


class Alien(pygame.sprite.Sprite):

    def __init__(self):

        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(os.path.join(Constants.IMG_DIR, "AlienShip.PNG")).convert()

        self.rect = self.image.get_rect()

        # position
        self.pos = vec(0, random.randrange(0, WIN_HEIGHT))

        # set the center of the sprite
        self.rect.center = (self.pos.x, self.pos.y)

        self.vel = vec(1, random.randrange(1, 4))

        self.angle = 0

        GAME_SPRITES.add(self)
        ALIEN.add(self)

    def fire_weapon(self, in_weapon):
        # check if the number of projectiles on the screen is less than the number of max projectiles
        if in_weapon.WEAPON_PROJECTILES < in_weapon.WEAPON_MAX_PROJECTILES:
            # check if the weapon has cooled down
            if pygame.sprite.get_ticks() - in_weapon.WEAPON_COOL_BEGIN > in_weapon.WEAPON_COOLDOWN_TIME:
                # create a new projectile. The projectile starting conditions are the same as the ship's
                # position, velocity, and direction. A deep copy was used to affect a pass by value rather than a
                # pass by reference.
                current_weapon = in_weapon(copy.deepcopy( copy.deepcopy(self.pos) ), copy.deepcopy(self.vel), vec(0, -1).rotate(-self.angle), ALIEN_PROJECTILES)
                in_weapon.WEAPON_COOL_BEGIN = pygame.sprite.get_ticks()
                # print(in_weapon.WEAPON_NAME + " : " + in_weapon.WEAPON_PROJECTILES.__str__())

                # self.weapon_sound.play()

    def update(self, *args):

        # motion equations
        self.pos += self.vel

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

        self.fire_weapon(WeaponGunAlien)
