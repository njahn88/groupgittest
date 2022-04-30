from pygame.math import Vector2 as vec
import level_class as l

# screen settings
WIDTH, HEIGHT = 800, 600
level_objects = [l.L1, l.L2,l.L3, l.L4, l.L5, l.L6, l.L7, l.L8, l.L9, l.L10, l.L11, l.L12, l.L13, l.L14, l.L15, l.L16]
# Frames per second (clock)
FPS = 120

MAZE_WIDTH,MAZE_HEIGHT = WIDTH, HEIGHT
BUTTON_SIZE = (100,50)
WYLY_SIZE = (300,500)

# colour settings
BLACK = (0,0,0)
RED = (208,22,22)
GREY = (107,107,107)
WHITE = (225,225,225)
PURPLE = (70,29,124)
PLAYER_COLOR = (0,98,255)

# font settings
START_FONT = 'arial black'
START_TEXT_SIZE = 16

# Player Settings
PLAYER_START_POS = vec(0,12)
PLAYER_SPEED = 1


