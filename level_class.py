import pygame
from settings import *
from button import *

class Level():
    w_img = pygame.image.load('no_Level.JPG')
    def __init__(self, text, level_img, text_file):
        self.text = text
        self.level_img = pygame.image.load(level_img)
        self.text_file = text_file
        

L1 = Level("Level 1", 'tech_maze.001.jpg', 'level_4.txt')
L2 = Level("Level 2", 'tech_maze.002.jpg', 'level_2.txt')
L3 = Level("Level 3", 'tech_maze.003.jpg', 'level_3.txt')
L4 = Level("Level 4", 'maze_4.jpg', 'level_4.txt')
L5 = Level("Level 5", 'tech_maze.005.jpg', 'level_5.txt')
L6 = Level("Level 6", 'tech_maze.006.jpg', 'level_6.txt')
L7 = Level("Level 7", 'tech_maze.007.jpg', 'level_7.txt')
L8 = Level("Level 8", 'tech_maze.008.jpg', 'level_8.txt')
L9 = Level("Level 9", 'tech_maze.009.jpg', 'level_9.txt')
L10 = Level("Level 10", 'tech_maze.010.jpg', 'level_10.txt')
L11 = Level("Level 11", 'tech_maze.011.jpg', 'level_11.txt')
L12 = Level("Level 12", 'tech_maze.012.jpg', 'level_12.txt')
L13 = Level("Level 13", 'tech_maze.013.jpg', 'level_13.txt')
L14 = Level("Level 14", 'tech_maze.014.jpg', 'level_14.txt')
L15 = Level("Level 15", 'tech_maze.015.jpg', 'level_15.txt')
L16 = Level("Level 16", 'tech_maze.016.jpg', 'level_16.txt')