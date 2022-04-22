from pygame.locals import *
import pygame
from app_class import *


 # Class allows for player movement in the up, down, left, and right directions
 # Sets the speed for the player
# class Player:
#     x = 44
#     y = 44
#     speed = 0.25
 
#     def moveRight(self):
#         self.x = self.x + self.speed
 
#     def moveLeft(self):
#         self.x = self.x - self.speed
 
#     def moveUp(self):
#         self.y = self.y - self.speed
 
#     def moveDown(self):
#         self.y = self.y + self.speed
 
# # Class builds the maze with a large array
# # 1's are wall components
# # 0's are open space
# # 2's are bones (intended to be collectable for the player)
# class Maze:
#     def __init__(self):
#        self.M = 20
#        self.N = 15
#        self.maze = [ 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
#                      1,0,0,0,0,0,0,0,1,0,1,1,1,0,0,0,1,1,0,0,
#                      1,0,1,1,1,0,0,1,1,0,0,0,0,0,0,0,0,1,0,1,
#                      1,0,1,2,1,0,0,0,1,0,0,1,1,0,0,1,0,1,0,1,
#                      1,0,0,0,0,0,1,1,1,1,1,1,0,0,1,1,0,0,0,1,
#                      1,0,0,1,1,0,0,0,0,0,0,0,0,1,1,2,0,1,1,1,
#                      1,0,0,0,1,0,0,0,1,1,1,0,0,0,0,0,1,1,0,1,
#                      1,0,1,1,1,0,1,0,0,0,1,1,1,1,0,1,1,0,0,1,
#                      1,0,1,0,0,0,1,0,1,0,1,0,1,0,0,0,1,1,0,1,
#                      1,0,1,0,1,0,1,0,1,1,1,0,0,0,1,0,0,0,0,1,
#                      1,0,1,0,1,0,1,0,1,0,1,0,0,1,1,1,0,0,0,1,
#                      0,0,1,0,1,0,1,0,2,0,0,0,1,0,1,0,0,0,1,1,
#                      1,0,1,1,1,0,0,0,1,1,1,1,1,0,0,0,1,1,1,1,
#                      1,0,0,0,2,0,0,0,0,0,0,0,1,0,0,0,0,0,2,1,
#                      1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

#     # Draws the maze and displays appropriate image for each maze component
#     def draw(self,display_surf,image_surf, bone_surf):
#        bx = 0
#        by = 0
#        for i in range(0,self.M*self.N):
#            # Add a wall component
#            if self.maze[ bx + (by*self.M) ] == 1:
#                display_surf.blit(image_surf,( bx *  40, by * 40))

#             # Add a bone to the maze
#            if self.maze[ bx + (by*self.M) ] == 2:
#                display_surf.blit(bone_surf,( bx *  40, by * 40) )

#             # changes rows in array when row is complete
#            bx = bx + 1
#            if bx > self.M-1:
#                bx = 0 
#                by = by + 1 


# class App:
 
#     windowWidth = 800
#     windowHeight = 600
#     player = 0
    
#     # initiallizes variables with Player and Maze classes
#     def __init__(self):
#         self._running = True
#         self._display_surf = None
#         self._image_surf = None
#         self._block_surf = None
#         self.player = Player()
#         self.maze = Maze()


#     # initiallizes pygame and loads all of the images
#     # sets the sizes of the images
#     def on_init(self):
#         pygame.init()
#         # sets the display width and height
#         self._display_surf = pygame.display.set_mode((self.windowWidth,self.windowHeight), pygame.HWSURFACE)
        
#         pygame.display.set_caption('Level One')
#         self._running = True
#         self._image_surf = pygame.image.load("bulldog.png").convert()
#         self._image_surf = pygame.transform.scale(self._image_surf, (30, 30))
#         self._block_surf = pygame.image.load("block.png").convert()
#         self._block_surf = pygame.transform.scale(self._block_surf, (35, 35))
#         self._bone_surf = pygame.image.load("bone.PNG").convert()
#         self._bone_surf = pygame.transform.scale(self._bone_surf, (30,30))


#         self.clock = pygame.time.Clock()


#     # When player presses escape key the program stops
#     def on_event(self, event):
#         if event.type == QUIT:
#             self._running = False
    
#     # Collision detection will be implemented here
#     def on_loop(self):
#             pass

#     # adds all images to the pygame display
#     def on_render(self):
#         self._display_surf.fill((0,0,0))
#         self._display_surf.blit(self._image_surf,(self.player.x,self.player.y))
#         self.maze.draw(self._display_surf, self._block_surf, self._bone_surf)

#         pygame.display.flip()
 
#     def on_cleanup(self):
#         pygame.quit()
    

#     def run(self):
#         if self.on_init() == False:
#             self._running = False

#         # Sets keys for player movement
#         # will later be changed to joystick movement
#         while( self._running ):
#             pygame.event.pump()
#             keys = pygame.key.get_pressed()
            
#             if (keys[K_RIGHT]):
#                 self.player.moveRight()
 
#             if (keys[K_LEFT]):
#                 self.player.moveLeft()
 
#             if (keys[K_UP]):
#                 self.player.moveUp()
 
#             if (keys[K_DOWN]):
#                 self.player.moveDown()
 
#             if (keys[K_ESCAPE]):
#                 self._running = False
 
#             self.on_loop()
#             self.on_render()
#         self.on_cleanup()
 
if __name__ == "__main__" :
    theApp = App()
    theApp.run()