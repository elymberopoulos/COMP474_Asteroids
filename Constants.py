
import os
import pygame

# game constants
TITLE = "Classic Asteroids"

# window width
WIN_WIDTH = 800

# window height
WIN_HEIGHT = 600

# frames per second
FPS = 60

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# game assets
GAME_DIR = os.path.dirname(__file__)
# relative path to assets dir
ASSETS_DIR = os.path.join(GAME_DIR, "assets")
# relative path to image dir
IMG_DIR = os.path.join(ASSETS_DIR, "images")
# relative path to audio dir
AUDIO_DIR = os.path.join(ASSETS_DIR, "audio")


# player constants
PLAYER_ACC = .5
PLAYER_FRICTION = -0.05
PLAYER_ANGLE_VEL = 3

# standard lists
GAME_SPRITES = pygame.sprite.Group()
PROJECTILES = pygame.sprite.Group()
ASTEROIDS = pygame.sprite.Group()
PLAYER_PROJECTILES = pygame.sprite.Group()
ALIEN_PROJECTILES = pygame.sprite.Group()
ALIEN = pygame.sprite.Group()
