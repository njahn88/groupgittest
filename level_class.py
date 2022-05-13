import pygame
from settings import *
from button import *
from pygame.math import Vector2 as vec


class Level():
    def __init__(self, text, level_img, text_file, start_pos, end_pos, enemy_pos):
        self.text = text
        self.level_img = level_img 
        self.text_file = text_file 
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.enemy_pos = enemy_pos

# All levels as objects so attributes can be called more easily        

L1 = Level("Level 1", 'maze_bmp\maze.001.bmp', 'Level_1.txt', vec(0,12), vec(20,2) , vec(10,3))
L2 = Level("Level 2", 'maze_bmp\maze.002.bmp', 'Level_2.txt', vec(0,2), vec(20,14), vec(6,4))
L3 = Level("Level 3", 'maze_bmp\maze.003.bmp', 'Level_3.txt', vec(6,2), vec(13,14), vec(7,8))
L4 = Level("Level 4", 'maze_bmp\maze.004.bmp', 'level_4.txt',vec(0,2), vec(20,14), vec(12,2))
L5 = Level("Level 5", 'maze_bmp\maze.005.bmp', 'Level_5.txt',vec(0,12), vec(20,14), vec(1,4))
L6 = Level("Level 6", 'maze_bmp\maze.006.bmp', 'Level_6.txt',vec(9,1), vec(19,12), vec(11,2))
L7 = Level("Level 7", 'maze_bmp\maze.007.bmp', 'Level_7.txt',vec(11,2), vec(9,12), vec(1,2))
L8 = Level("Level 8", 'maze_bmp\maze.008.bmp', 'Level_8.txt',vec(1,14), vec(20,2), vec(9,2))
L9 = Level("Level 9", 'maze_bmp\maze.009.bmp', 'Level_9.txt',vec(0,6), vec(20,8), vec(15,14))
L10 = Level("Level 10", 'maze_bmp\maze.010.bmp', 'Level_10.txt',vec(12,2), vec(7,14), vec(1,4))
L11 = Level("Level 11", 'maze_bmp\maze.011.bmp', 'Level_11.txt',vec(0,2), vec(20,14), vec(5,2))
L12 = Level("Level 12", 'maze_bmp\maze.012.bmp', 'Level_12.txt',vec(0,14), vec(20,8), vec(1,2))
L13 = Level("Level 13", 'maze_bmp\maze.013.bmp', 'Level_13.txt',vec(0,8), vec(20,10), vec(6,4))
L14 = Level("Level 14", 'maze_bmp\maze.014.bmp', 'Level_14.txt',vec(1,2), vec(13,12), vec(5,6))
L15 = Level("Level 15", 'maze_bmp\maze.015.bmp', 'Level_15.txt',vec(0,2), vec(20,10), vec(1,14))
L16 = Level("Level 16", 'maze_bmp\maze.016.bmp', 'Level_16.txt',vec(0,14), vec(20,2), vec(5,2))