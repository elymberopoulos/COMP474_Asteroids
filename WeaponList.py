from Weapon import *
from Constants import *
import os
import pygame

class WeaponGun(Weapon):
    WEAPON_NAME = "GUN"
    WEAPON_PROJECTILE_SPEED = 10
    WEAPON_COOLDOWN_TIME = 200
    WEAPON_LIFE_TIME = 500
    WEAPON_PROJECTILE_COLOR = WHITE
    WEAPON_MAX_PROJECTILES = 3
    WEAPON_ANGULAR_SPREAD = 0
    WEAPON_SPRITE_SIZE_X = 2
    WEAPON_SPRITE_SIZE_Y = 2



