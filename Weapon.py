
from Constants import *
import random

vec = pygame.math.Vector2


class Weapon(pygame.sprite.Sprite):

    WEAPON_NAME = "NONE"
    WEAPON_PROJECTILE_SPEED = 10
    WEAPON_COOLDOWN_TIME = 100
    WEAPON_LIFE_TIME = 1000
    WEAPON_PROJECTILE_COLOR = WHITE
    WEAPON_MAX_PROJECTILES = 10
    WEAPON_ANGULAR_SPREAD = 5
    WEAPON_SPRITE_SIZE_X = 5
    WEAPON_SPRITE_SIZE_Y = 5
    WEAPON_PROJECTILES = 0
    WEAPON_COOL_BEGIN = 0

    # Weapons take a copy of the initial position, velocity, and direction to keep up with the ship
    def __init__(self, in_pos, in_vel, in_dir):
        if Weapon.WEAPON_PROJECTILES > Weapon.WEAPON_MAX_PROJECTILES:
            self.kill()
            return

        pygame.sprite.Sprite.__init__(self)

        # adds itself to the game sprites
        GAME_SPRITES.add(self)

        # sprite image of the projectile
        self.image = pygame.Surface((self.WEAPON_SPRITE_SIZE_X, self.WEAPON_SPRITE_SIZE_Y)) # pygame.image.load(os.path.join(IMG_DIR, "Bullet.png")).convert()
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
        Weapon.WEAPON_PROJECTILES += 1

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
            Weapon.WEAPON_PROJECTILES -= 1
            # tell pygame to kill this object
            self.kill()

        # apply friction
        # self.acc += self.vel * PLAYER_FRICTION

        # motion equations
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        self.rect.center = self.pos

