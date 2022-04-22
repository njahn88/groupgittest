from pygame.math import Vector2 as vec

# screen settings
WIDTH, HEIGHT = 850, 650
# Frames per second (clock)
FPS = 100
TOP_BOTTOM_BUFFER = 50
MAZE_WIDTH,MAZE_HEIGHT = WIDTH - TOP_BOTTOM_BUFFER, HEIGHT-TOP_BOTTOM_BUFFER

# colour settings
BLACK = (0,0,0)
RED = (208,22,22)
GREY = (107,107,107)
WHITE = (225,225,225)
PLAYER_COLOR = (190,194,15)

# font settings
START_FONT = 'arial black'
START_TEXT_SIZE = 16

# Player Settings
PLAYER_START_POS = vec(1,1)

