import pygame, sys
from button import *

from settings import *

mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption('menu')
screen = pygame.display.set_mode((800, 600),0,32)

font = pygame.font.SysFont(None, 38)

class Menu:

    def __init__(self,app):
        self.app = app
        self.running = True

    def draw_text(self,text, font, color, surface, x, y):
        textobj = font.render(text, 1, color)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        surface.blit(textobj, textrect)

    #click = False

    mx, my = pygame.mouse.get_pos()

    def main_menu(self):
        self.running = True
        while self.running:
            bg = pygame.image.load('menu_bmp\wyly_0.bmp')
            screen.fill((0,0,0))
            screen.blit(bg, (0, 0))

            self.draw_text('Press any key to start', font, (252, 3, 3), screen, 440, 210)
            self.draw_text('LEFT and RIGHT arrow keys', font, (252, 3, 3), screen, 440, 305)
            self.draw_text('to switch levels', font, (252, 3, 3), screen, 470, 335)
            self.draw_text('ESCAPE key to go back', font, (252, 3, 3), screen, 440, 374)
            self.draw_text('to start page', font, (252, 3, 3), screen, 470, 404)
            self.draw_text('SPACE or RETURN key to go', font, (252, 3, 3), screen, 440, 440)
            self.draw_text('to selected level', font, (252, 3, 3), screen, 470, 470)
            
            button_play = Button(base_image=pygame.image.load("menu_bmp\playb.bmp"),
            hovering_image=pygame.image.load("menu_bmp\playb.bmp"),pos= (400,245))
            button_play.update(screen)

            click = False
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                if event.type == KEYDOWN:
                    self.lvl1()
                    
                if event.type == MOUSEBUTTONDOWN:
                    if button_play.checkForInput(pygame.mouse.get_pos()):
                        self.app.state = 'playing'
                        self.running = False


            pygame.display.update()
            mainClock.tick(60)

    def lvl1(self):
        self.running = True
        while self.running:
            bg = pygame.image.load('menu_bmp\lvl1.bmp')
            screen.fill((0,0,0))
            screen.blit(bg, (0, 0))

            button_play = Button(base_image=pygame.image.load("menu_bmp\playb.bmp"),
            hovering_image=pygame.image.load("menu/playb.png"),pos= (400,245))
            button_play.update(screen)

            button_goback = Button(base_image=pygame.image.load("menu_bmp\gobackb.bmp"),
            hovering_image=pygame.image.load("menu_bmp\gobackb.bmp"),pos= (280,245))
            button_goback.update(screen)

            button_next = Button(base_image=pygame.image.load("menu/extb.png"),
            hovering_image=pygame.image.load("menu/extb.png"),pos= (390,345))
            button_next.update(screen)



        #  draw_text('game', font, (255, 255, 255), screen, 20, 20)
            for event in pygame.event.get():
    ##            if event.type == MOUSEBUTTONUP:
    ##                print(event.pos)
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.main_menu()
                    #   running = False
                if event.type == KEYDOWN:
                    if event.key == K_RIGHT:
                        self.lvl2()
                if event.type == KEYDOWN:
                    if event.key == K_SPACE:
                         self.maze1()
                if event.type == KEYDOWN:
                    if event.key == K_RETURN:
                         self.maze1()
                if event.type == MOUSEBUTTONDOWN:
                    if button_play.checkForInput(pygame.mouse.get_pos()):
                        self.app.level = 0
                        self.app.start_level()
                        self.app.state = 'play level'
                        self.running = False
                    if button_goback.checkForInput(pygame.mouse.get_pos()):
                        self.main_menu()
                    if button_next.checkForInput(pygame.mouse.get_pos()):
                        self.lvl2()
                
                            

                pygame.display.update()
                mainClock.tick(60)

    def lvl2(self):
        self.running = True
        while self.running:
            bg = pygame.image.load("menu_bmp\lvl2.bmp")
            screen.fill((0,0,0))
            screen.blit(bg, (0, 0))

            button_play = Button(base_image=pygame.image.load("menu_bmp\playb.bmp"),
            hovering_image=pygame.image.load("menu_bmp\playb.bmp"), pos= (400,245))
            button_play.update(screen)

            button_goback = Button(base_image=pygame.image.load("menu_bmp\gobackb.bmp"),
            hovering_image=pygame.image.load("menu_bmp\gobackb.bmp"),pos= (280,245))
            button_goback.update(screen)

            button_next = Button(base_image=pygame.image.load("menu\extb.png"),
            hovering_image=pygame.image.load("menu\extb.png"),pos= (390,345))
            button_next.update(screen)

            button_previous = Button(base_image=pygame.image.load("menu_bmp\prevb.bmp"),
            hovering_image=pygame.image.load("menu_bmp\prevb.bmp"),pos= (293,345))
            button_previous.update(screen)
            

        #  draw_text('options', font, (255, 255, 255), screen, 20, 20)
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONUP:
                    print(event.pos)
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.main_menu()
                if event.type == KEYDOWN:
                    if event.key == K_RIGHT:
                        self.lvl3()
                if event.type == KEYDOWN:
                    if event.key == K_LEFT:
                        self.lvl1()
                if event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        self.maze2()
                if event.type == KEYDOWN:
                    if event.key == K_RETURN:
                        self.maze2()
                if event.type == MOUSEBUTTONDOWN:
                    if button_play.checkForInput(pygame.mouse.get_pos()):
                        self.app.level = 1
                        self.app.start_level()
                        self.app.state = 'play level'
                        self.running = False
                    if button_goback.checkForInput(pygame.mouse.get_pos()):
                        self.main_menu()
                    if button_next.checkForInput(pygame.mouse.get_pos()):
                        self.lvl3()
                    if button_previous.checkForInput(pygame.mouse.get_pos()):
                        self.lvl1()
            #1:  ul (upper left), ur, ll, lr (308,350) (388,350) (308,430) (388,430)
            #2: ul (upper left), ur, ll, lr (398,350) (475,350) (398,430) (475,430)
            pygame.display.update()
            mainClock.tick(60)

    def lvl3(self):
        self.running = True
        while self.running:
            bg = pygame.image.load("menu_bmp\lvl3.bmp")
            screen.fill((0,0,0))
            screen.blit(bg, (0, 0))

            button_play = Button(base_image=pygame.image.load("menu_bmp\playb.bmp"),
            hovering_image=pygame.image.load("menu_bmp\playb.bmp"), pos= (400,245))
            button_play.update(screen)

            button_goback = Button(base_image=pygame.image.load("menu_bmp\gobackb.bmp"),
            hovering_image=pygame.image.load("menu_bmp\gobackb.bmp"),pos= (280,245))
            button_goback.update(screen)

            button_next = Button(base_image=pygame.image.load("menu\extb.png"),
            hovering_image=pygame.image.load("menu\extb.png"),pos= (390,345))
            button_next.update(screen)
            
            button_previous = Button(base_image=pygame.image.load("menu_bmp\prevb.bmp"),
            hovering_image=pygame.image.load("menu_bmp\prevb.bmp"),pos= (293,345))
            button_previous.update(screen)
            
        #  draw_text('game', font, (255, 255, 255), screen, 20, 20)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.main_menu()
                if event.type == KEYDOWN:
                    if event.key == K_RIGHT:
                        self.lvl4()
                if event.type == KEYDOWN:
                    if event.key == K_LEFT:
                        self.lvl2()
                if event.type == KEYDOWN:
                    if event.key == K_SPACE:
                         self.maze1()
                if event.type == KEYDOWN:
                    if event.key == K_RETURN:
                         self.maze1()
                if event.type == MOUSEBUTTONDOWN:
                    if button_play.checkForInput(pygame.mouse.get_pos()):
                        self.app.level = 2
                        self.app.start_level()
                        self.app.state = 'play level'
                        self.running = False
                    if button_goback.checkForInput(pygame.mouse.get_pos()):
                        self.main_menu()
                    if button_next.checkForInput(pygame.mouse.get_pos()):
                        self.lvl4()
                    if button_previous.checkForInput(pygame.mouse.get_pos()):
                        self.lvl2()
            
            pygame.display.update()
            mainClock.tick(60)

    def lvl4(self):
        self.running = True
        while self.running:
            bg = pygame.image.load("menu_bmp\lvl4.bmp")
            screen.fill((0,0,0))
            screen.blit(bg, (0, 0))

            button_play = Button(base_image=pygame.image.load("menu_bmp\playb.bmp"),
            hovering_image=pygame.image.load("menu_bmp\playb.bmp"), pos= (400,245))
            button_play.update(screen)

            button_goback = Button(base_image=pygame.image.load("menu_bmp\gobackb.bmp"),
            hovering_image=pygame.image.load("menu_bmp\gobackb.bmp"),pos= (280,245))
            button_goback.update(screen)

            button_next = Button(base_image=pygame.image.load("menu\extb.png"),
            hovering_image=pygame.image.load("menu\extb.png"),pos= (390,345))
            button_next.update(screen)
            
            button_previous = Button(base_image=pygame.image.load("menu_bmp\prevb.bmp"),
            hovering_image=pygame.image.load("menu_bmp\prevb.bmp"),pos= (293,345))
            button_previous.update(screen)
            
        #  draw_text('game', font, (255, 255, 255), screen, 20, 20)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.main_menu()
                if event.type == KEYDOWN:
                    if event.key == K_RIGHT:
                        self.lvl5()
                if event.type == KEYDOWN:
                    if event.key == K_LEFT:
                        self.lvl3()
                if event.type == KEYDOWN:
                    if event.key == K_SPACE:
                         self.maze1()
                if event.type == KEYDOWN:
                    if event.key == K_RETURN:
                         self.maze1()
                if event.type == MOUSEBUTTONDOWN:
                    if button_play.checkForInput(pygame.mouse.get_pos()):
                        self.app.level = 3
                        self.app.start_level()
                        self.app.state = 'play level'
                        self.running = False
                    if button_goback.checkForInput(pygame.mouse.get_pos()):
                        self.main_menu()
                    if button_next.checkForInput(pygame.mouse.get_pos()):
                        self.lvl5()
                    if button_previous.checkForInput(pygame.mouse.get_pos()):
                        self.lvl3()
            
            pygame.display.update()
            mainClock.tick(60)

    def lvl5(self):
        self.running = True
        while self.running:
            bg = pygame.image.load("menu_bmp\lvl5.bmp")
            screen.fill((0,0,0))
            screen.blit(bg, (0, 0))

            button_play = Button(base_image=pygame.image.load("menu_bmp\playb.bmp"),
            hovering_image=pygame.image.load("menu_bmp\playb.bmp"), pos= (400,245))
            button_play.update(screen)

            button_goback = Button(base_image=pygame.image.load("menu_bmp\gobackb.bmp"),
            hovering_image=pygame.image.load("menu_bmp\gobackb.bmp"),pos= (280,245))
            button_goback.update(screen)

            button_next = Button(base_image=pygame.image.load("menu\extb.png"),
            hovering_image=pygame.image.load("menu\extb.png"),pos= (390,345))
            button_next.update(screen)
            
            button_previous = Button(base_image=pygame.image.load("menu_bmp\prevb.bmp"),
            hovering_image=pygame.image.load("menu_bmp\prevb.bmp"),pos= (293,345))
            button_previous.update(screen)
            
        #  draw_text('game', font, (255, 255, 255), screen, 20, 20)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.main_menu()
                if event.type == KEYDOWN:
                    if event.key == K_RIGHT:
                        self.lvl6()
                if event.type == KEYDOWN:
                    if event.key == K_LEFT:
                        self.lvl4()
                if event.type == KEYDOWN:
                    if event.key == K_SPACE:
                         self.maze1()
                if event.type == KEYDOWN:
                    if event.key == K_RETURN:
                         self.maze1()
                if event.type == MOUSEBUTTONDOWN:
                    if button_play.checkForInput(pygame.mouse.get_pos()):
                        self.app.level = 4
                        self.app.start_level()
                        self.app.state = 'play level'
                        self.running = False
                    if button_goback.checkForInput(pygame.mouse.get_pos()):
                        self.main_menu()
                    if button_next.checkForInput(pygame.mouse.get_pos()):
                        self.lvl6()
                    if button_previous.checkForInput(pygame.mouse.get_pos()):
                        self.lvl4()
            
            pygame.display.update()
            mainClock.tick(60)

    def lvl6(self):
        self.running = True
        while self.running:
            bg = pygame.image.load("menu_bmp\lvl6.bmp")
            screen.fill((0,0,0))
            screen.blit(bg, (0, 0))

            button_play = Button(base_image=pygame.image.load("menu_bmp\playb.bmp"),
            hovering_image=pygame.image.load("menu_bmp\playb.bmp"), pos= (400,245))
            button_play.update(screen)

            button_goback = Button(base_image=pygame.image.load("menu_bmp\gobackb.bmp"),
            hovering_image=pygame.image.load("menu_bmp\gobackb.bmp"),pos= (280,245))
            button_goback.update(screen)

            button_next = Button(base_image=pygame.image.load("menu\extb.png"),
            hovering_image=pygame.image.load("menu\extb.png"),pos= (390,345))
            button_next.update(screen)
            
            button_previous = Button(base_image=pygame.image.load("menu_bmp\prevb.bmp"),
            hovering_image=pygame.image.load("menu_bmp\prevb.bmp"),pos= (293,345))
            button_previous.update(screen)
            
        #  draw_text('game', font, (255, 255, 255), screen, 20, 20)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.main_menu()
                if event.type == KEYDOWN:
                    if event.key == K_RIGHT:
                        self.lvl7()
                if event.type == KEYDOWN:
                    if event.key == K_LEFT:
                        self.lvl5()
                if event.type == KEYDOWN:
                    if event.key == K_SPACE:
                         self.maze1()
                if event.type == KEYDOWN:
                    if event.key == K_RETURN:
                         self.maze1()
                if event.type == MOUSEBUTTONDOWN:
                    if button_play.checkForInput(pygame.mouse.get_pos()):
                        self.app.level = 5
                        self.app.start_level()
                        self.app.state = 'play level'
                        self.running = False
                    if button_goback.checkForInput(pygame.mouse.get_pos()):
                        self.main_menu()
                    if button_next.checkForInput(pygame.mouse.get_pos()):
                        self.lvl7()
                    if button_previous.checkForInput(pygame.mouse.get_pos()):
                        self.lvl5()
            
            pygame.display.update()
            mainClock.tick(60)

    def lvl7(self):
        self.running = True
        while self.running:
            bg = pygame.image.load("menu_bmp\lvl7.bmp")
            screen.fill((0,0,0))
            screen.blit(bg, (0, 0))

            button_play = Button(base_image=pygame.image.load("menu_bmp\playb.bmp"),
            hovering_image=pygame.image.load("menu_bmp\playb.bmp"), pos= (400,245))
            button_play.update(screen)

            button_goback = Button(base_image=pygame.image.load("menu_bmp\gobackb.bmp"),
            hovering_image=pygame.image.load("menu_bmp\gobackb.bmp"),pos= (280,245))
            button_goback.update(screen)

            button_next = Button(base_image=pygame.image.load("menu\extb.png"),
            hovering_image=pygame.image.load("menu\extb.png"),pos= (390,345))
            button_next.update(screen)
            
            button_previous = Button(base_image=pygame.image.load("menu_bmp\prevb.bmp"),
            hovering_image=pygame.image.load("menu_bmp\prevb.bmp"),pos= (293,345))
            button_previous.update(screen)
            
        #  draw_text('game', font, (255, 255, 255), screen, 20, 20)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.main_menu()
                if event.type == KEYDOWN:
                    if event.key == K_RIGHT:
                        self.lvl8()
                if event.type == KEYDOWN:
                    if event.key == K_LEFT:
                        self.lvl6()
                if event.type == KEYDOWN:
                    if event.key == K_SPACE:
                         self.maze1()
                if event.type == KEYDOWN:
                    if event.key == K_RETURN:
                         self.maze1()
                if event.type == MOUSEBUTTONDOWN:
                    if button_play.checkForInput(pygame.mouse.get_pos()):
                        self.app.level = 6
                        self.app.start_level()
                        self.app.state = 'play level'
                        self.running = False
                    if button_goback.checkForInput(pygame.mouse.get_pos()):
                        self.main_menu()
                    if button_next.checkForInput(pygame.mouse.get_pos()):
                        self.lvl8()
                    if button_previous.checkForInput(pygame.mouse.get_pos()):
                        self.lvl6()
            
            pygame.display.update()
            mainClock.tick(60)

    def lvl8(self):
        self.running = True
        while self.running:
            bg = pygame.image.load("menu_bmp\lvl8.bmp")
            screen.fill((0,0,0))
            screen.blit(bg, (0, 0))

            button_play = Button(base_image=pygame.image.load("menu_bmp\playb.bmp"),
            hovering_image=pygame.image.load("menu_bmp\playb.bmp"), pos= (400,245))
            button_play.update(screen)

            button_goback = Button(base_image=pygame.image.load("menu_bmp\gobackb.bmp"),
            hovering_image=pygame.image.load("menu_bmp\gobackb.bmp"),pos= (280,245))
            button_goback.update(screen)

            button_next = Button(base_image=pygame.image.load("menu\extb.png"),
            hovering_image=pygame.image.load("menu\extb.png"),pos= (390,345))
            button_next.update(screen)
            
            button_previous = Button(base_image=pygame.image.load("menu_bmp\prevb.bmp"),
            hovering_image=pygame.image.load("menu_bmp\prevb.bmp"),pos= (293,345))
            button_previous.update(screen)
            
        #  draw_text('game', font, (255, 255, 255), screen, 20, 20)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.main_menu()
                if event.type == KEYDOWN:
                    if event.key == K_RIGHT:
                        self.lvl9()
                if event.type == KEYDOWN:
                    if event.key == K_LEFT:
                        self.lvl7()
                if event.type == KEYDOWN:
                    if event.key == K_SPACE:
                         self.maze1()
                if event.type == KEYDOWN:
                    if event.key == K_RETURN:
                         self.maze1()
                if event.type == MOUSEBUTTONDOWN:
                    if button_play.checkForInput(pygame.mouse.get_pos()):
                        self.app.level = 7
                        self.app.start_level()
                        self.app.state = 'play level'
                        self.running = False
                    if button_goback.checkForInput(pygame.mouse.get_pos()):
                        self.main_menu()
                    if button_next.checkForInput(pygame.mouse.get_pos()):
                        self.lvl9()
                    if button_previous.checkForInput(pygame.mouse.get_pos()):
                        self.lvl7()
            pygame.display.update()
            mainClock.tick(60)

    def lvl9(self):
        self.running = True
        while self.running:
            bg = pygame.image.load("menu_bmp\lvl9.bmp")
            screen.fill((0,0,0))
            screen.blit(bg, (0, 0))

            button_play = Button(base_image=pygame.image.load("menu_bmp\playb.bmp"),
            hovering_image=pygame.image.load("menu_bmp\playb.bmp"), pos= (400,245))
            button_play.update(screen)

            button_goback = Button(base_image=pygame.image.load("menu_bmp\gobackb.bmp"),
            hovering_image=pygame.image.load("menu_bmp\gobackb.bmp"),pos= (280,245))
            button_goback.update(screen)

            button_next = Button(base_image=pygame.image.load("menu\extb.png"),
            hovering_image=pygame.image.load("menu\extb.png"),pos= (390,345))
            button_next.update(screen)
            
            button_previous = Button(base_image=pygame.image.load("menu_bmp\prevb.bmp"),
            hovering_image=pygame.image.load("menu_bmp\prevb.bmp"),pos= (293,345))
            button_previous.update(screen)
            
        #  draw_text('game', font, (255, 255, 255), screen, 20, 20)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.main_menu()
                if event.type == KEYDOWN:
                    if event.key == K_RIGHT:
                        self.lvl10()
                if event.type == KEYDOWN:
                    if event.key == K_LEFT:
                        self.lvl8()
                if event.type == KEYDOWN:
                    if event.key == K_SPACE:
                         self.maze1()
                if event.type == KEYDOWN:
                    if event.key == K_RETURN:
                         self.maze1()
                if event.type == MOUSEBUTTONDOWN:
                    if button_play.checkForInput(pygame.mouse.get_pos()):
                        self.app.level = 8
                        self.app.start_level()
                        self.app.state = 'play level'
                        self.running = False
                    if button_goback.checkForInput(pygame.mouse.get_pos()):
                        self.main_menu()
                    if button_next.checkForInput(pygame.mouse.get_pos()):
                        self.lvl10()
                    if button_previous.checkForInput(pygame.mouse.get_pos()):
                        self.lvl8()
            
            pygame.display.update()
            mainClock.tick(60)

    def lvl10(self):
        self.running = True
        while self.running:
            bg = pygame.image.load("menu_bmp\lvl10.bmp")
            screen.fill((0,0,0))
            screen.blit(bg, (0, 0))

            button_play = Button(base_image=pygame.image.load("menu_bmp\playb.bmp"),
            hovering_image=pygame.image.load("menu_bmp\playb.bmp"), pos= (400,245))
            button_play.update(screen)

            button_goback = Button(base_image=pygame.image.load("menu_bmp\gobackb.bmp"),
            hovering_image=pygame.image.load("menu_bmp\gobackb.bmp"),pos= (280,245))
            button_goback.update(screen)

            button_next = Button(base_image=pygame.image.load("menu\extb.png"),
            hovering_image=pygame.image.load("menu\extb.png"),pos= (390,345))
            button_next.update(screen)
            
            button_previous = Button(base_image=pygame.image.load("menu_bmp\prevb.bmp"),
            hovering_image=pygame.image.load("menu_bmp\prevb.bmp"),pos= (293,345))
            button_previous.update(screen)
            
        #  draw_text('game', font, (255, 255, 255), screen, 20, 20)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.main_menu()
                if event.type == KEYDOWN:
                    if event.key == K_RIGHT:
                        self.lvl11()
                if event.type == KEYDOWN:
                    if event.key == K_LEFT:
                        self.lvl9()
                if event.type == KEYDOWN:
                    if event.key == K_SPACE:
                         self.maze1()
                if event.type == KEYDOWN:
                    if event.key == K_RETURN:
                         self.maze1()
                if event.type == MOUSEBUTTONDOWN:
                    if button_play.checkForInput(pygame.mouse.get_pos()):
                        self.app.level = 9
                        self.app.start_level()
                        self.app.state = 'play level'
                        self.running = False
                    if button_goback.checkForInput(pygame.mouse.get_pos()):
                        self.main_menu()
                    if button_next.checkForInput(pygame.mouse.get_pos()):
                        self.lvl11()
                    if button_previous.checkForInput(pygame.mouse.get_pos()):
                        self.lvl9()
                
            
            pygame.display.update()
            mainClock.tick(60)

    def lvl11(self):
        self.running = True
        while self.running:
            bg = pygame.image.load("menu_bmp\lvl11.bmp")
            screen.fill((0,0,0))
            screen.blit(bg, (0, 0))

            button_play = Button(base_image=pygame.image.load("menu_bmp\playb.bmp"),
            hovering_image=pygame.image.load("menu_bmp\playb.bmp"), pos= (400,245))
            button_play.update(screen)

            button_goback = Button(base_image=pygame.image.load("menu_bmp\gobackb.bmp"),
            hovering_image=pygame.image.load("menu_bmp\gobackb.bmp"),pos= (280,245))
            button_goback.update(screen)

            button_next = Button(base_image=pygame.image.load("menu\extb.png"),
            hovering_image=pygame.image.load("menu\extb.png"),pos= (390,345))
            button_next.update(screen)
            
            button_previous = Button(base_image=pygame.image.load("menu_bmp\prevb.bmp"),
            hovering_image=pygame.image.load("menu_bmp\prevb.bmp"),pos= (293,345))
            button_previous.update(screen)
            
        #  draw_text('game', font, (255, 255, 255), screen, 20, 20)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.main_menu()
                if event.type == KEYDOWN:
                    if event.key == K_RIGHT:
                        self.lvl12()
                if event.type == KEYDOWN:
                    if event.key == K_LEFT:
                        self.lvl10()
                if event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        self.maze1()
                if event.type == KEYDOWN:
                    if event.key == K_RETURN:
                        self.maze1()
                if event.type == MOUSEBUTTONDOWN:
                    if button_play.checkForInput(pygame.mouse.get_pos()):
                        self.app.level = 10
                        self.app.start_level()
                        self.app.state = 'play level'
                        self.running = False
                    if button_goback.checkForInput(pygame.mouse.get_pos()):
                        self.main_menu()
                    if button_next.checkForInput(pygame.mouse.get_pos()):
                        self.lvl12()
                    if button_previous.checkForInput(pygame.mouse.get_pos()):
                        self.lvl10()
            
            pygame.display.update()
            mainClock.tick(60)

    def lvl12(self):
        self.running = True
        while self.running:
            bg = pygame.image.load("menu_bmp\lvl12.bmp")
            screen.fill((0,0,0))
            screen.blit(bg, (0, 0))
            
            button_play = Button(base_image=pygame.image.load("menu_bmp\playb.bmp"),
            hovering_image=pygame.image.load("menu_bmp\playb.bmp"), pos= (400,245))
            button_play.update(screen)

            button_goback = Button(base_image=pygame.image.load("menu_bmp\gobackb.bmp"),
            hovering_image=pygame.image.load("menu_bmp\gobackb.bmp"),pos= (280,245))
            button_goback.update(screen)

            button_next = Button(base_image=pygame.image.load("menu\extb.png"),
            hovering_image=pygame.image.load("menu\extb.png"),pos= (390,345))
            button_next.update(screen)
            
            button_previous = Button(base_image=pygame.image.load("menu_bmp\prevb.bmp"),
            hovering_image=pygame.image.load("menu_bmp\prevb.bmp"),pos= (293,345))
            button_previous.update(screen)
            
        #  draw_text('game', font, (255, 255, 255), screen, 20, 20)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.main_menu()
                if event.type == KEYDOWN:
                    if event.key == K_RIGHT:
                        self.lvl13()
                if event.type == KEYDOWN:
                    if event.key == K_LEFT:
                        self.lvl11()
                if event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        self.maze1()
                if event.type == KEYDOWN:
                    if event.key == K_RETURN:
                        self.maze1()
                if event.type == MOUSEBUTTONDOWN:
                    if button_play.checkForInput(pygame.mouse.get_pos()):
                        self.app.level = 1
                        self.app.start_level()
                        self.app.state = 'play level'
                        self.running = False
                    if button_goback.checkForInput(pygame.mouse.get_pos()):
                        self.main_menu()
                    if button_next.checkForInput(pygame.mouse.get_pos()):
                        self.lvl13()
                    if button_previous.checkForInput(pygame.mouse.get_pos()):
                        self.lvl11()
            
            pygame.display.update()
            mainClock.tick(60)

    def lvl13(self):
        self.running = True
        while self.running:
            bg = pygame.image.load("menu_bmp\lvl13.bmp")
            screen.fill((0,0,0))
            screen.blit(bg, (0, 0))

            button_play = Button(base_image=pygame.image.load("menu_bmp\playb.bmp"),
            hovering_image=pygame.image.load("menu_bmp\playb.bmp"), pos= (400,245))
            button_play.update(screen)

            button_goback = Button(base_image=pygame.image.load("menu_bmp\gobackb.bmp"),
            hovering_image=pygame.image.load("menu_bmp\gobackb.bmp"),pos= (280,245))
            button_goback.update(screen)

            button_next = Button(base_image=pygame.image.load("menu\extb.png"),
            hovering_image=pygame.image.load("menu\extb.png"),pos= (390,345))
            button_next.update(screen)
            
            button_previous = Button(base_image=pygame.image.load("menu_bmp\prevb.bmp"),
            hovering_image=pygame.image.load("menu_bmp\prevb.bmp"),pos= (293,345))
            button_previous.update(screen)

        #  draw_text('game', font, (255, 255, 255), screen, 20, 20)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.main_menu()
                if event.type == KEYDOWN:
                    if event.key == K_RIGHT:
                        self.lvl14()
                if event.type == KEYDOWN:
                    if event.key == K_LEFT:
                        self.lvl12()
                if event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        self.maze1()
                if event.type == KEYDOWN:
                    if event.key == K_RETURN:
                        self.maze1()
                if event.type == MOUSEBUTTONDOWN:
                    if button_play.checkForInput(pygame.mouse.get_pos()):
                        self.app.level = 12
                        self.app.start_level()
                        self.app.state = 'play level'
                        self.running = False
                    if button_goback.checkForInput(pygame.mouse.get_pos()):
                        self.main_menu()
                    if button_next.checkForInput(pygame.mouse.get_pos()):
                        self.lvl14()
                    if button_previous.checkForInput(pygame.mouse.get_pos()):
                        self.lvl12()
                        
            pygame.display.update()
            mainClock.tick(60)

    def lvl14(self):
        self.running = True
        while self.running:
            bg = pygame.image.load("menu_bmp\lvl14.bmp")
            screen.fill((0,0,0))
            screen.blit(bg, (0, 0))

            button_play = Button(base_image=pygame.image.load("menu_bmp\playb.bmp"),
            hovering_image=pygame.image.load("menu_bmp\playb.bmp"), pos= (400,245))
            button_play.update(screen)

            button_goback = Button(base_image=pygame.image.load("menu_bmp\gobackb.bmp"),
            hovering_image=pygame.image.load("menu_bmp\gobackb.bmp"),pos= (280,245))
            button_goback.update(screen)

            button_next = Button(base_image=pygame.image.load("menu\extb.png"),
            hovering_image=pygame.image.load("menu\extb.png"),pos= (390,345))
            button_next.update(screen)
            
            button_previous = Button(base_image=pygame.image.load("menu_bmp\prevb.bmp"),
            hovering_image=pygame.image.load("menu_bmp\prevb.bmp"),pos= (293,345))
            button_previous.update(screen)
            
        #  draw_text('game', font, (255, 255, 255), screen, 20, 20)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.main_menu()
                if event.type == KEYDOWN:
                    if event.key == K_RIGHT:
                        self.lvl15()
                if event.type == KEYDOWN:
                    if event.key == K_LEFT:
                        self.lvl13()
                if event.type == KEYDOWN:
                    if event.key == K_SPACE:
                         self.maze1()
                if event.type == KEYDOWN:
                    if event.key == K_RETURN:
                         self.maze1()
                if event.type == MOUSEBUTTONDOWN:
                    if button_play.checkForInput(pygame.mouse.get_pos()):
                        self.app.level = 13
                        self.app.start_level()
                        self.app.state = 'play level'
                        self.running = False
                    if button_goback.checkForInput(pygame.mouse.get_pos()):
                        self.main_menu()
                    if button_next.checkForInput(pygame.mouse.get_pos()):
                        self.lvl15()
                    if button_previous.checkForInput(pygame.mouse.get_pos()):
                        self.lvl13()
            
            pygame.display.update()
            mainClock.tick(60)

    def lvl15(self):
        self.running = True
        while self.running:
            bg = pygame.image.load("menu_bmp\lvl15.bmp")
            screen.fill((0,0,0))
            screen.blit(bg, (0, 0))

            button_play = Button(base_image=pygame.image.load("menu_bmp\playb.bmp"),
            hovering_image=pygame.image.load("menu_bmp\playb.bmp"), pos= (400,245))
            button_play.update(screen)

            button_goback = Button(base_image=pygame.image.load("menu_bmp\gobackb.bmp"),
            hovering_image=pygame.image.load("menu_bmp\gobackb.bmp"),pos= (280,245))
            button_goback.update(screen)

            button_next = Button(base_image=pygame.image.load("menu\extb.png"),
            hovering_image=pygame.image.load("menu\extb.png"),pos= (390,345))
            button_next.update(screen)
            
            button_previous = Button(base_image=pygame.image.load("menu_bmp\prevb.bmp"),
            hovering_image=pygame.image.load("menu_bmp\prevb.bmp"),pos= (293,345))
            button_previous.update(screen)
            
        #  draw_text('game', font, (255, 255, 255), screen, 20, 20)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.main_menu()
                if event.type == KEYDOWN:
                    if event.key == K_RIGHT:
                        self.lvl16()
                if event.type == KEYDOWN:
                    if event.key == K_LEFT:
                        self.lvl14()
                if event.type == KEYDOWN:
                    if event.key == K_SPACE:
                         self.maze1()
                if event.type == KEYDOWN:
                    if event.key == K_RETURN:
                         self.maze1()
                if event.type == MOUSEBUTTONDOWN:
                    if button_play.checkForInput(pygame.mouse.get_pos()):
                        self.app.level = 14
                        self.app.start_level()
                        self.app.state = 'play level'
                        self.running = False
                    if button_goback.checkForInput(pygame.mouse.get_pos()):
                        self.main_menu()
                    if button_next.checkForInput(pygame.mouse.get_pos()):
                        self.lvl16()
                    if button_previous.checkForInput(pygame.mouse.get_pos()):
                        self.lvl14()
            
            pygame.display.update()
            mainClock.tick(60)

    def lvl16(self):
        self.running = True
        while self.running:
            bg = pygame.image.load("menu_bmp\lvl16.bmp")
            screen.fill((0,0,0))
            screen.blit(bg, (0, 0))

            button_play = Button(base_image=pygame.image.load("menu_bmp\playb.bmp"),
            hovering_image=pygame.image.load("menu_bmp\playb.bmp"), pos= (400,245))
            button_play.update(screen)

            button_goback = Button(base_image=pygame.image.load("menu_bmp\gobackb.bmp"),
            hovering_image=pygame.image.load("menu_bmp\gobackb.bmp"),pos= (280,245))
            button_goback.update(screen)
            
            button_previous = Button(base_image=pygame.image.load("menu_bmp\prevb.bmp"),
            hovering_image=pygame.image.load("menu_bmp\prevb.bmp"),pos= (293,345))
            button_previous.update(screen)
            
        #  draw_text('game', font, (255, 255, 255), screen, 20, 20)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.main_menu()
                if event.type == KEYDOWN:
                    if event.key == K_LEFT:
                        self.lvl15()
                if event.type == KEYDOWN:
                    if event.key == K_SPACE:
                         self.maze1()
                if event.type == KEYDOWN:
                    if event.key == K_RETURN:
                         self.maze1()
                if event.type == MOUSEBUTTONDOWN:
                    if button_play.checkForInput(pygame.mouse.get_pos()):
                        self.app.level = 15
                        self.app.start_level()
                        self.app.state = 'play level'
                        self.running = False
                    if button_goback.checkForInput(pygame.mouse.get_pos()):
                        self.main_menu()
                    if button_previous.checkForInput(pygame.mouse.get_pos()):
                        self.lvl15()
            
            pygame.display.update()
            mainClock.tick(60)

    def maze1(self):
        self.running = True
        while self.running:
            bg = pygame.image.load("menu_bmp\win.bmp")
            screen.fill(BLACK)
            screen.blit(bg, (0, 0))

            button_home = Button(base_image=pygame.image.load("menu_bmp\homeb.bmp"),
            hovering_image=pygame.image.load("menu_bmp\homeb.bmp"),pos= (390,245))
            button_home.update(screen)

            button_exit = Button(base_image=pygame.image.load("menu_bmp\exitb.bmp"),
            hovering_image=pygame.image.load("menu_bmp\exitb.bmp"),pos= (280,245))
            button_exit.update(screen)
            
        #  draw_text('game', font, (255, 255, 255), screen, 20, 20)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.main_menu()
                        self.app.state = 'start'
                if event.type == MOUSEBUTTONDOWN:
                    if button_home.checkForInput(pygame.mouse.get_pos()):
                        self.running = False
                        self.app.state = 'start'
                    if button_exit.checkForInput(pygame.mouse.get_pos()):
                        self.running = False
                        pygame.quit()
                        sys.exit()
         
            
            pygame.display.update()
            mainClock.tick(60)

    def maze2(self):
        running = True
        while running:
            bg = pygame.image.load("menu_bmp\wyly_0.bmp")
            screen.fill((0,0,0))
            screen.blit(bg, (0, 0))
            
        #  draw_text('game', font, (255, 255, 255), screen, 20, 20)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
            
            pygame.display.update()
            mainClock.tick(60)

