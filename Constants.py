
import os
import pygame

# game constants
TITLE = "MEX"

# window width
WIN_WIDTH = 800

# window height
WIN_HEIGHT = 600

# frames per second
FPS = 60

# colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# game assets
GAME_DIR = os.path.dirname(__file__)
# relative path to assets dir
ASSETS_DIR = os.path.join(GAME_DIR, "assets")
# relative path to image dir
IMG_DIR = os.path.join(ASSETS_DIR, "images")

# player constants
PLAYER_ACC = .5
PLAYER_FRICTION = -.1
PLAYER_ANGLE_VEL = 1

GAME_SPRITES = pygame.sprite.Group()
PROJECTILES = pygame.sprite.Group()