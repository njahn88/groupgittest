import pygame, sys
from pygame.locals import *
from settings import *
from player_class import *
from enemy_class import *
from new_menu import *





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
        self.cell_width = WIDTH//21
        self.cell_height = HEIGHT//15
        self.p_pos = vec(level_objects[self.level].start_pos[0],level_objects[self.level].start_pos[1])
        self.player = Player(self,self.p_pos)
        self.enemy = Enemy(self, level_objects[self.level].enemy_pos)
        self.walls = []
        self.bones = []
        self.holes = []
        self.menu = Menu(self)
        self.score = 0
        self.highscore = self.readFile()
        

        
        
    def readFile(self,fileLocation = 'highscore.txt'):
        # load high score
        file = open(fileLocation, 'r')
        return file.read()

    def writeToFile(self,fileLocation, data):
        file = open(fileLocation, 'w')
        file.write(str(data))

            


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
                    elif char == 'X':
                        self.holes.append(vec(xidx,yidx))
        
    def start_level(self):
        self.player.grid_pos = level_objects[self.level].start_pos
        self.player.pix_pos = self.player.get_pix_pos()
        self.enemy.grid_pos = level_objects[self.level].enemy_pos
        self.enemy.pix_pos = self.enemy.get_pix_pos()

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
                    self.player.move(vec(-1,0))
 
                if (keys[K_RIGHT]):
                    self.player.move(vec(1,0))
 
                if (keys[K_UP]):
                    self.player.move(vec(0,-1))
 
                if (keys[K_DOWN]):
                    self.player.move(vec(0,1))
 
                if (keys[K_ESCAPE]):
                    self._running = False
            if self.enemy.grid_pos == self.player.grid_pos:
                self.player.lives -= 1
                if self.player.lives == 0:
                    self.state = 'game over'
                
                pygame.display.update()
            
                


    def level_update(self):
    
        
        if self.player.next_level():

            self.menu.running = True
            self.state = 'game over'
            
        

            pygame.display.update()            
        self.player.update()
        self.enemy.update()
                    
        pygame.display.update() 
                    

                
                
    
    def playing_update(self):


        if self.player.next_level():
            self.level += 1
            if self.level in range(14):
                self.player.direction = vec(1,0)
                self.player.grid_pos = level_objects[self.level].start_pos
                self.player.pix_pos = self.player.get_pix_pos()
                self.enemy.grid_pos = level_objects[self.level].enemy_pos
                self.enemy.pix_pos = self.enemy.get_pix_pos()
                self.enemy.target = self.player.grid_pos
            else:
                self.state = 'game over'
        self.player.update()
        self.enemy.update()

        pygame.display.update()
        



    def playing_draw(self):
        
        
        CURRENT_LEVEL = level_objects[self.level]

            
        self.screen.fill(BLACK)
        self.load(CURRENT_LEVEL.level_img,CURRENT_LEVEL.text_file)
        self.screen.blit(self.maze,(0,0))
        #self.draw_grid()
        self.draw_text(f'Current Score: {self.score}', self.screen, [60,1], 18, WHITE, START_FONT)
        self.draw_text(f'High Score: {self.highscore}', self.screen, [(WIDTH//2)+60,1], 18, WHITE, START_FONT)
        self.player.draw(self.screen)
        self.enemy.draw()

        if self.player.can_power_up():
                self.score += 1
        if self.player.is_hole():
                self.score -= 1
       
    
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
                self.menu.main_menu()
            elif self.state == 'playing':
                self.playing_events()
                self.playing_update()
                self.playing_draw()
            elif self.state == 'play level':
                self.playing_events()
                self.level_update()
                self.playing_draw()
            elif self.state == 'game over':
                if self.score > int(self.highscore):
                    self.writeToFile('highscore.txt', self.score)
                    self.highscore = self.readFile()
                self.menu.maze1()
                self._running = False
            else:
                self._running = False
            self.clock.tick(FPS)
            pygame.display.update()

            
 
        self.on_cleanup()

