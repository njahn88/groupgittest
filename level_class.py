import pygame
from settings import *
from button import *
from pygame.math import Vector2 as vec


class Level():
    w_img = pygame.image.load('no_Level.JPG')
    def __init__(self, text, level_img, text_file, start_pos, end_pos, enemy_pos):
        self.text = text
        self.level_img = level_img
        self.text_file = text_file
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.enemy_pos = enemy_pos

        

L1 = Level("Level 1", 'tech_maze.001.jpg', 'Level_1.txt', vec(0,12), vec(20,2) , vec(10,3) )
L2 = Level("Level 2", 'tech_maze.002.jpg', 'Level_2.txt', vec(0,2), vec(20,14), vec(6,4))
L3 = Level("Level 3", 'tech_maze.003.jpg', 'Level_3.txt', vec(6,2), vec(13,14), vec(7,8))
L4 = Level("Level 4", 'maze_4.jpg', 'level_4.txt',vec(0,2), vec(20,14), vec(12,2))
L5 = Level("Level 5", 'tech_maze.005.jpg', 'Level_5.txt',vec(0,12), vec(20,14), vec(1,4))
L6 = Level("Level 6", 'tech_maze.006.jpg', 'Level_6.txt',vec(9,1), vec(19,12), vec(11,2))
L7 = Level("Level 7", 'tech_maze.007.jpg', 'Level_7.txt',vec(11,2), vec(9,12), vec(1,2))
L8 = Level("Level 8", 'tech_maze.008.jpg', 'Level_8.txt',vec(1,14), vec(20,2), vec(9,2))
L9 = Level("Level 9", 'tech_maze.009.jpg', 'Level_9.txt',vec(0,6), vec(20,8), vec(15,14))
L10 = Level("Level 10", 'tech_maze.010.jpg', 'Level_10.txt',vec(12,2), vec(7,14), vec(1,4))
L11 = Level("Level 11", 'tech_maze.011.jpg', 'Level_11.txt',vec(0,2), vec(20,14), vec(5,2))
L12 = Level("Level 12", 'tech_maze.012.jpg', 'Level_12.txt',vec(0,14), vec(20,8), vec(1,2))
L13 = Level("Level 13", 'tech_maze.013.jpg', 'Level_13.txt',vec(0,8), vec(20,10), vec(6,4))
L14 = Level("Level 14", 'tech_maze.014.jpg', 'Level_14.txt',vec(1,2), vec(13,12), vec(5,6))
L15 = Level("Level 15", 'tech_maze.015.jpg', 'Level_15.txt',vec(0,2), vec(20,10), vec(1,14))
L16 = Level("Level 16", 'tech_maze.016.jpg', 'Level_16.txt',vec(0,14), vec(20,2), vec(5,2))