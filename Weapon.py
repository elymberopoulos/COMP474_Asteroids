
from Constants import *
import random

vec = pygame.math.Vector2


class Weapon(pygame.sprite.Sprite):

    # name of the weapon
    WEAPON_NAME = "NONE"
    # speed of the projectile
    WEAPON_PROJECTILE_SPEED = 10
    # cooldown time to control the firing rate
    WEAPON_COOLDOWN_TIME = 100
    # sets the life time in ms
    WEAPON_LIFE_TIME = 1000
    # sets the projectile color
    WEAPON_PROJECTILE_COLOR = WHITE
    # sets the maximum number of projectiles allowed on screen
    WEAPON_MAX_PROJECTILES = 10
    # sets the angular spread of the weapon
    WEAPON_ANGULAR_SPREAD = 5
    # sets the size of the sprite in x
    WEAPON_SPRITE_SIZE_X = 5
    # sets the size of the sprite in y
    WEAPON_SPRITE_SIZE_Y = 5
    # accumulator to keep of the total number of current projectiles on screen
    WEAPON_PROJECTILES = 0
    # flag to act as a marker after firing to control cooldown
    WEAPON_COOL_BEGIN = 0

    # Weapons take a copy of the initial position, velocity, and direction to keep up with the ship
    def __init__(self, in_pos, in_vel, in_dir, IN_SPRITE_LIST):
        if type(self).WEAPON_PROJECTILES > type(self).WEAPON_MAX_PROJECTILES:
            self.kill()
            return

        pygame.sprite.Sprite.__init__(self)

        # adds itself to the game sprites
        GAME_SPRITES.add(self)

        # add to projectile group for collision detection
        PROJECTILES.add(self)

        # additional sprite list
        IN_SPRITE_LIST.add(self)

        # sprite image of the projectile
        self.image = pygame.Surface((self.WEAPON_SPRITE_SIZE_X, self.WEAPON_SPRITE_SIZE_Y))
        self.image.fill(self.WEAPON_PROJECTILE_COLOR)

        self.rect = self.image.get_rect()
        self.rect.center = in_pos

        # position
        self.pos = in_pos
        # velocity with angular spread
        if 0 == self.WEAPON_ANGULAR_SPREAD:
            self.vel = in_vel + (in_dir.normalize() * self.WEAPON_PROJECTILE_SPEED)
        else:
            self.vel = in_vel + (in_dir.rotate(random.randrange(-self.WEAPON_ANGULAR_SPREAD, self.WEAPON_ANGULAR_SPREAD, 1)).normalize()*self.WEAPON_PROJECTILE_SPEED)
        # acceleration
        self.acc = vec(0.0, 0.0)
        # direction
        self.dir = in_dir

        self.projectile_start_time = pygame.sprite.get_ticks()

        # keeps track of how many projectiles of this weapon type are on the screen
        type(self).WEAPON_PROJECTILES += 1

    def update(self, *args):
        # handles the screen wrapping
        if self.pos.x > WIN_WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIN_WIDTH
        if self.pos.y > WIN_HEIGHT:
            self.pos.y = 0
        if self.pos.y < 0:
            self.pos.y = WIN_HEIGHT

        # removal of a projectile based on time
        if pygame.sprite.get_ticks() - self.projectile_start_time > self.WEAPON_LIFE_TIME:
            # decrement the number of projectiles of this weapon class
            type(self).WEAPON_PROJECTILES -= 1
            # tell pygame to kill this object
            self.kill()

        # apply friction
        # self.acc += self.vel * PLAYER_FRICTION

        # motion equations
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        # update the position
        self.rect.center = self.pos

