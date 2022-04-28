from tkinter import CURRENT
import pygame, sys
from pygame.locals import *
from settings import *
from player_class import *
from button import *
import level_class as level



pygame.init()
vec = pygame.math.Vector2

class App:

    
    # initiallizes variables with Player and Maze classes
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self._running = True
        self.state = 'start'
        self.level = 0
        self.player_pos = level_objects[self.level].start_pos
        self.cell_width = WIDTH//21
        self.cell_height = HEIGHT//15
        self.player = Player(self,PLAYER_START_POS)
        self.walls = []
        self.bones = []
        
        



    # When player presses escape key the program stops
    def on_event(self, event):
        if event.type == QUIT:
            self._running = False

########################## Helper functions ############################

    def draw_text(self, text, screen, pos, size, color, font_name, centered = False):
        font = pygame.font.SysFont(font_name, size)
        var_text = font.render(text, False, color)
        text_size = var_text.get_size()
        if centered:
            pos[0] = pos[0]-text_size[0]//2
        screen.blit(var_text,pos)

    def load(self, maze, text):
        self.walls.clear()
        self.bones.clear()
        self.maze = pygame.image.load(maze)
        self.maze = pygame.transform.scale(self.maze, (WIDTH,HEIGHT))

        # opening walls file and creating walls list
        # with coords of walls
        with open (text,'r') as file:
            for yidx, line in enumerate(file):
                for xidx, char in enumerate(line):
                    if char == '1':
                        self.walls.append(vec(xidx,yidx))
                    elif char == '2':
                        self.bones.append(vec(xidx,yidx))


    def draw_grid(self):
        for x in range(WIDTH//self.cell_width):
            pygame.draw.line(self.maze, GREY, (x*self.cell_width,0), (x*self.cell_width, HEIGHT))
        for x in range(HEIGHT//self.cell_height):
            pygame.draw.line(self.maze, GREY, (0,x*self.cell_height), (WIDTH, x*self.cell_height))

        for wall in self.walls:
            pygame.draw.rect(self.maze, (112, 55, 163), (wall.x*self.cell_width, wall.y*self.cell_height,
            self.cell_width, self.cell_height) )

########################## start functions ###########################

    def start_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._running = False
            if event.type == KEYDOWN and event.key == K_SPACE:
                self.state = 'playing'
        pygame.display.update()
    
    def start_update(self):
        pass
    


    def start_draw(self):
            

            self.draw_text('Menu',self.screen,[WIDTH//2,HEIGHT//2],
            START_TEXT_SIZE, (255,255,255), START_FONT, centered = True)


            pygame.display.update()

############################### playing functions ###############################
    def playing_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._running = False
            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
            
                if (keys[K_LEFT]):
                    self.player.move(vec(-PLAYER_SPEED,0))
 
                if (keys[K_RIGHT]):
                    self.player.move(vec(PLAYER_SPEED,0))
 
                if (keys[K_UP]):
                    self.player.move(vec(0,-PLAYER_SPEED))
 
                if (keys[K_DOWN]):
                    self.player.move(vec(0,PLAYER_SPEED))
 
                if (keys[K_ESCAPE]):
                    self._running = False
                
                if self.player.next_level():
                    self.level += 1
                    self.player = Player(self, level_objects[self.level].start_pos)

                    
                    

                
                
    
    def playing_update(self):
        self.player.update()



    def playing_draw(self):

        CURRENT_LEVEL = level_objects[self.level]
            
        self.screen.fill(BLACK)
        self.load(CURRENT_LEVEL.level_img,CURRENT_LEVEL.text_file)
        self.screen.blit(self.maze,(0,0))
        #self.draw_grid()
        self.draw_text(f'Current Score: {0}', self.screen, [60,1], 18, WHITE, START_FONT)
        self.draw_text(f'High Score: {0}', self.screen, [(WIDTH//2)+60,1], 18, WHITE, START_FONT)
        self.player.draw(self.screen)

        pygame.display.update()

###################################################################################

 
    def on_cleanup(self):
        pygame.quit()
        sys.exit()
    

    def run(self):

        # Sets keys for player movement
        # will later be changed to joystick movement
        while self._running:

            if self.state == 'start':
                self.start_events()
                self.start_update()
                self.start_draw()
            elif self.state == 'playing':
                self.playing_events()
                self.playing_update()
                self.playing_draw()
            else:
                self._running = False
            self.clock.tick(FPS)

            
 
        self.on_cleanup()

