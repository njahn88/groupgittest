
import pygame
import settings as set
vec = pygame.math.Vector2

class Player:
    def __init__(self,app, pos):
        self.app = app
        self.grid_pos = pos
        self.pix_pos = self.get_pix_pos()
        self.direction = vec(1,0)
        self.stored_direction = None
        self.able_to_move = True
        self.lives = 5
        


    def update(self):
        if self.able_to_move:
            self.pix_pos += self.direction
        if self.time_to_move():
                if self.stored_direction != None:
                    self.direction = self.stored_direction
                self.able_to_move = self.can_move()
        # if self.can_power_up():
        #     set.PLAYER_SPEED += 50
        # if self.next_level():
        #     self.draw(self.app.screen)
        if self.previous_level():
            self.direction = (1,0)

    
        

        # setting grid position in reference to pixel position
        self.grid_pos[0] = ((self.pix_pos[0]-self.app.cell_width//2)//self.app.cell_width+1)
        self.grid_pos[1] = ((self.pix_pos[1]-self.app.cell_height//2)//self.app.cell_height+1)

    def draw(self, screen):

        player = pygame.image.load('bulldog.png')
        player = pygame.transform.scale(player, (self.app.cell_width-1, self.app.cell_height-1))
        screen.blit(player, self.pix_pos)

        # drawing player lives
        for x in range(self.lives):
            pygame.draw.circle(self.app.screen, set.PLAYER_COLOR, (20 + 18*x, set.HEIGHT -15), 8)
        # pygame.draw.circle(self.app.screen, PLAYER_COLOR, self.pix_pos, self.app.cell_width//2-2 )

        # drawing the grid_pos rectangle
        #pygame.draw.rect(self.app.screen, RED, (self.grid_pos[0]*self.app.cell_width + TOP_BOTTOM_BUFFER//2,
         #self.grid_pos[1]* self.app.cell_height + TOP_BOTTOM_BUFFER//2,
         #self.app.cell_width, self.app.cell_height), 1)

    def move(self, direction):
        self.stored_direction = direction

    def get_pix_pos(self):
        return vec((self.grid_pos.x *self.app.cell_width)- self.app.cell_width//2,
         (self.grid_pos.y * self.app.cell_height)  - self.app.cell_height)

    def time_to_move(self):
        if int(self.pix_pos.x) % self.app.cell_width == 0:
            if self.direction == vec(1,0) or self.direction == vec (-1,0) or self.direction == vec(0,0):
                return True
        if int(self.pix_pos.y) % self.app.cell_height == 0:
            if self.direction == vec(0,1) or self.direction == vec (0,-1) or self.direction == vec(0,0):
                return True
       
    def can_move(self):
        for wall in self.app.walls:
            if vec(self.grid_pos+self.direction) == wall:
                return False
        return True

    def can_power_up(self):
        for bone in self.app.bones:
            if vec(self.grid_pos+self.direction) == bone:
                return True
        return False

    def is_hole(self):
        for hole in self.app.holes:
            if vec(self.grid_pos+self.direction) == hole:
                return True
        return False

    def next_level(self):
        if self.grid_pos[0] > 20 or self.grid_pos[1] > 14:
            print(True)
            return True
        return False
    
    def previous_level(self):
        if self.grid_pos[0] < 0 or self.grid_pos[1] < 0:
            return True
        return False
