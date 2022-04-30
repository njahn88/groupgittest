import queue
import pygame
from settings import *
# import random

vec = pygame.math.Vector2

class Enemy:
    def __init__(self, app, pos):
        self.app = app
        self.grid_pos = pos
        self.pix_pos = self.get_pix_pos()
        self.radius = int(self.app.cell_width//2.3)
        self.direction = vec(1,0)
        self.target = None
        

    def update(self):
        self.target = self.app.player.grid_pos
        if self.target != self.grid_pos:
                self.pix_pos += self.direction
                if self.time_to_move():
                    self.move()


        # setting grid_pos in reference to pixel position
        self.grid_pos[0] = ((self.pix_pos[0]-self.app.cell_width//2)//self.app.cell_width+1)
        self.grid_pos[1] = ((self.pix_pos[1]-self.app.cell_height//2)//self.app.cell_height+1)


    def draw(self):

        pygame.draw.circle(self.app.screen, PURPLE, (int(self.pix_pos.x),int(self.pix_pos.y)), self.radius)

    def get_pix_pos(self):
        return vec((self.grid_pos.x *self.app.cell_width)- self.app.cell_width//2,
         (self.grid_pos.y * self.app.cell_height)  - self.app.cell_height//2)

    def move(self):
        self.direction = self.get_path_direction(self.target)
    
    def get_path_direction(self,target):
        next_cell = self.find_next_cell(target)
        x_dir = next_cell[0] - self.grid_pos[0]
        y_dir = next_cell[1] - self.grid_pos[1]
        return vec(x_dir, y_dir)
    
    def find_next_cell(self,target):
        path = self.BFS([int(self.grid_pos.x), int(self.grid_pos.y)],
         [int(target[0]), int(target[1])])


        return path[1]
    
    def BFS(self,start,target):
        grid = [[0 for x in range(21)] for x in range(15)]
        for cell in self.app.walls:
            if cell.x < 21 and cell.y < 15:
                grid[int(cell.y)][int(cell.x)] = 1
        queue = [start]
        path = []
        visited = []
        while queue:
            current = queue[0]
            queue.remove(queue[0])
            visited.append(current)
            if current == target:
                break
            else:
                neighbors = [[0,-1],[1,0],[0,1],[-1,0]]
                for n in neighbors:
                    if n[0]+ current[0] >= 0 and n[0]+ current[0] < len(grid[0]):
                        if n[1]+ current[1] >= 0 and n[1]+ current[1] < len(grid):
                            next_cell = [n[0]+current[0], n[1]+current[1]]
                            if next_cell not in visited:
                                if grid[next_cell[1]][next_cell[0]] != 1:
                                    queue.append(next_cell)
                                    path.append({"Current": current, "Next": next_cell})
        shortest = [target]
        while target != start:
            for step in path:
                if step["Next"]== target:
                    target = step["Current"]
                    shortest.insert(0,step["Current"]) 
        return shortest                  

    # def get_random_direction(self):
    #     while True:
    #         number = random.randint(-2,1)
    #         if number == -2:
    #             x_dir, y_dir = 1,0
    #         elif number == -1:
    #             x_dir, y_dir = 0,1
    #         elif number == 0:
    #             x_dir, y_dir = -1,0
    #         else:
    #             x_dir, y_dir = 0,-1
    #         next_pos = vec(self.grid_pos.x+x_dir, self.grid_pos.y+y_dir)
    #         if next_pos not in self.app.walls:
    #             break
    #         # if vec(dir.x+x_dir, dir.y+y_dir) in self.app.walls:
    #         #     break
    #     return vec(x_dir,y_dir)


    def time_to_move(self):
        if int(self.pix_pos.x-self.radius) % self.app.cell_width == 0:
            if self.direction == vec(1,0) or self.direction == vec (-1,0) or self.direction == vec(0,0):
                return True
        if int(self.pix_pos.y-self.radius) % self.app.cell_height == 0:
            if self.direction == vec(0,1) or self.direction == vec (0,-1) or self.direction == vec(0,0):
                return True
        return False
    


    

        

        
