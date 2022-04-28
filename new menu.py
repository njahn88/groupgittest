import pygame, sys
from button import *
from app_class import App
from settings import *

mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption('menu')
screen = pygame.display.set_mode((800, 600),0,32)

font = pygame.font.SysFont(None, 38)


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

#click = False

mx, my = pygame.mouse.get_pos()

def main_menu():
    while True:
        bg = pygame.image.load('menu\wyly_0.PNG')
        screen.fill((0,0,0))
        screen.blit(bg, (0, 0))

        draw_text('Press any key to start', font, (252, 3, 3), screen, 440, 210)
        draw_text('LEFT and RIGHT arrow keys', font, (252, 3, 3), screen, 440, 305)
        draw_text('to switch levels', font, (252, 3, 3), screen, 470, 335)
        draw_text('ESCAPE key to go back', font, (252, 3, 3), screen, 440, 374)
        draw_text('to start page', font, (252, 3, 3), screen, 470, 404)
        draw_text('SPACE or RETURN key to go', font, (252, 3, 3), screen, 440, 440)
        draw_text('to selected level', font, (252, 3, 3), screen, 470, 470)
        


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
                lvl1()
                click = True


        pygame.display.update()
        mainClock.tick(60)

def lvl1():
    running = True
    while running:
        bg = pygame.image.load("menu\lvl1.PNG")
        screen.fill((0,0,0))
        screen.blit(bg, (0, 0))

        button_play = Button(base_image=pygame.image.load("menu\playb.png"),
        hovering_image=pygame.image.load("menu\playb.png"),pos= (400,245))
        button_play.update(screen)

        button_goback = Button(base_image=pygame.image.load("menu\gobackb.png"),
        hovering_image=pygame.image.load("menu\gobackb.png"),pos= (280,245))
        button_goback.update(screen)

        button_next = Button(base_image=pygame.image.load("menu\extb.png"),
        hovering_image=pygame.image.load("menu\extb.png"),pos= (390,345))
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
                    main_menu()
                 #   running = False
            if event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    lvl2()
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    maze1()
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    maze1()
            if event.type == MOUSEBUTTONDOWN:
                if button_play.checkForInput(pygame.mouse.get_pos()):
                    maze1()
                if button_goback.checkForInput(pygame.mouse.get_pos()):
                    main_menu()
                if button_next.checkForInput(pygame.mouse.get_pos()):
                    lvl2()
            
                        

            pygame.display.update()
            mainClock.tick(60)

def lvl2():
    running = True
    while running:
        bg = pygame.image.load("menu\lvl2.PNG")
        screen.fill((0,0,0))
        screen.blit(bg, (0, 0))

        button_play = Button(base_image=pygame.image.load("menu\playb.png"),
        hovering_image=pygame.image.load("menu\playb.png"), pos= (400,245))
        button_play.update(screen)

        button_goback = Button(base_image=pygame.image.load("menu\gobackb.png"),
        hovering_image=pygame.image.load("menu\gobackb.png"),pos= (280,245))
        button_goback.update(screen)

        button_next = Button(base_image=pygame.image.load("menu\extb.png"),
        hovering_image=pygame.image.load("menu\extb.png"),pos= (390,345))
        button_next.update(screen)

        button_previous = Button(base_image=pygame.image.load("menu\prevb.png"),
        hovering_image=pygame.image.load("menu\prevb.png"),pos= (293,345))
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
                    main_menu()
            if event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    lvl3()
            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    lvl1()
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    maze2()
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    maze2()
            if event.type == MOUSEBUTTONDOWN:
                if button_play.checkForInput(pygame.mouse.get_pos()):
                    maze1()
                if button_goback.checkForInput(pygame.mouse.get_pos()):
                    main_menu()
                if button_next.checkForInput(pygame.mouse.get_pos()):
                    lvl3()
                if button_previous.checkForInput(pygame.mouse.get_pos()):
                    lvl1()
        #1:  ul (upper left), ur, ll, lr (308,350) (388,350) (308,430) (388,430)
        #2: ul (upper left), ur, ll, lr (398,350) (475,350) (398,430) (475,430)
        pygame.display.update()
        mainClock.tick(60)

def lvl3():
    running = True
    while running:
        bg = pygame.image.load("menu\lvl3.PNG")
        screen.fill((0,0,0))
        screen.blit(bg, (0, 0))

        button_play = Button(base_image=pygame.image.load("menu\playb.png"),
        hovering_image=pygame.image.load("menu\playb.png"), pos= (400,245))
        button_play.update(screen)

        button_goback = Button(base_image=pygame.image.load("menu\gobackb.png"),
        hovering_image=pygame.image.load("menu\gobackb.png"),pos= (280,245))
        button_goback.update(screen)

        button_next = Button(base_image=pygame.image.load("menu\extb.png"),
        hovering_image=pygame.image.load("menu\extb.png"),pos= (390,345))
        button_next.update(screen)
        
        button_previous = Button(base_image=pygame.image.load("menu\prevb.png"),
        hovering_image=pygame.image.load("menu\prevb.png"),pos= (293,345))
        button_previous.update(screen)
        
      #  draw_text('game', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    main_menu()
            if event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    lvl4()
            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    lvl2()
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    maze1()
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    maze1()
            if event.type == MOUSEBUTTONDOWN:
                if button_play.checkForInput(pygame.mouse.get_pos()):
                    maze1()
                if button_goback.checkForInput(pygame.mouse.get_pos()):
                    main_menu()
                if button_next.checkForInput(pygame.mouse.get_pos()):
                    lvl4()
                if button_previous.checkForInput(pygame.mouse.get_pos()):
                    lvl2()
        
        pygame.display.update()
        mainClock.tick(60)

def lvl4():
    running = True
    while running:
        bg = pygame.image.load("menu\lvl4.PNG")
        screen.fill((0,0,0))
        screen.blit(bg, (0, 0))

        button_play = Button(base_image=pygame.image.load("menu\playb.png"),
        hovering_image=pygame.image.load("menu\playb.png"), pos= (400,245))
        button_play.update(screen)

        button_goback = Button(base_image=pygame.image.load("menu\gobackb.png"),
        hovering_image=pygame.image.load("menu\gobackb.png"),pos= (280,245))
        button_goback.update(screen)

        button_next = Button(base_image=pygame.image.load("menu\extb.png"),
        hovering_image=pygame.image.load("menu\extb.png"),pos= (390,345))
        button_next.update(screen)
        
        button_previous = Button(base_image=pygame.image.load("menu\prevb.png"),
        hovering_image=pygame.image.load("menu\prevb.png"),pos= (293,345))
        button_previous.update(screen)
        
      #  draw_text('game', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    main_menu()
            if event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    lvl5()
            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    lvl3()
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    maze1()
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    maze1()
            if event.type == MOUSEBUTTONDOWN:
                if button_play.checkForInput(pygame.mouse.get_pos()):
                    maze1()
                if button_goback.checkForInput(pygame.mouse.get_pos()):
                    main_menu()
                if button_next.checkForInput(pygame.mouse.get_pos()):
                    lvl5()
                if button_previous.checkForInput(pygame.mouse.get_pos()):
                    lvl3()
        
        pygame.display.update()
        mainClock.tick(60)

def lvl5():
    running = True
    while running:
        bg = pygame.image.load("menu\lvl5.PNG")
        screen.fill((0,0,0))
        screen.blit(bg, (0, 0))

        button_play = Button(base_image=pygame.image.load("menu\playb.png"),
        hovering_image=pygame.image.load("menu\playb.png"), pos= (400,245))
        button_play.update(screen)

        button_goback = Button(base_image=pygame.image.load("menu\gobackb.png"),
        hovering_image=pygame.image.load("menu\gobackb.png"),pos= (280,245))
        button_goback.update(screen)

        button_next = Button(base_image=pygame.image.load("menu\extb.png"),
        hovering_image=pygame.image.load("menu\extb.png"),pos= (390,345))
        button_next.update(screen)
        
        button_previous = Button(base_image=pygame.image.load("menu\prevb.png"),
        hovering_image=pygame.image.load("menu\prevb.png"),pos= (293,345))
        button_previous.update(screen)
        
      #  draw_text('game', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    main_menu()
            if event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    lvl6()
            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    lvl4()
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    maze1()
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    maze1()
            if event.type == MOUSEBUTTONDOWN:
                if button_play.checkForInput(pygame.mouse.get_pos()):
                    maze1()
                if button_goback.checkForInput(pygame.mouse.get_pos()):
                    main_menu()
                if button_next.checkForInput(pygame.mouse.get_pos()):
                    lvl6()
                if button_previous.checkForInput(pygame.mouse.get_pos()):
                    lvl4()
        
        pygame.display.update()
        mainClock.tick(60)

def lvl6():
    running = True
    while running:
        bg = pygame.image.load("menu\lvl6.PNG")
        screen.fill((0,0,0))
        screen.blit(bg, (0, 0))

        button_play = Button(base_image=pygame.image.load("menu\playb.png"),
        hovering_image=pygame.image.load("menu\playb.png"), pos= (400,245))
        button_play.update(screen)

        button_goback = Button(base_image=pygame.image.load("menu\gobackb.png"),
        hovering_image=pygame.image.load("menu\gobackb.png"),pos= (280,245))
        button_goback.update(screen)

        button_next = Button(base_image=pygame.image.load("menu\extb.png"),
        hovering_image=pygame.image.load("menu\extb.png"),pos= (390,345))
        button_next.update(screen)
        
        button_previous = Button(base_image=pygame.image.load("menu\prevb.png"),
        hovering_image=pygame.image.load("menu\prevb.png"),pos= (293,345))
        button_previous.update(screen)
        
      #  draw_text('game', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    main_menu()
            if event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    lvl7()
            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    lvl5()
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    maze1()
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    maze1()
            if event.type == MOUSEBUTTONDOWN:
                if button_play.checkForInput(pygame.mouse.get_pos()):
                    maze1()
                if button_goback.checkForInput(pygame.mouse.get_pos()):
                    main_menu()
                if button_next.checkForInput(pygame.mouse.get_pos()):
                    lvl7()
                if button_previous.checkForInput(pygame.mouse.get_pos()):
                    lvl5()
        
        pygame.display.update()
        mainClock.tick(60)

def lvl7():
    running = True
    while running:
        bg = pygame.image.load("menu\lvl7.PNG")
        screen.fill((0,0,0))
        screen.blit(bg, (0, 0))

        button_play = Button(base_image=pygame.image.load("menu\playb.png"),
        hovering_image=pygame.image.load("menu\playb.png"), pos= (400,245))
        button_play.update(screen)

        button_goback = Button(base_image=pygame.image.load("menu\gobackb.png"),
        hovering_image=pygame.image.load("menu\gobackb.png"),pos= (280,245))
        button_goback.update(screen)

        button_next = Button(base_image=pygame.image.load("menu\extb.png"),
        hovering_image=pygame.image.load("menu\extb.png"),pos= (390,345))
        button_next.update(screen)
        
        button_previous = Button(base_image=pygame.image.load("menu\prevb.png"),
        hovering_image=pygame.image.load("menu\prevb.png"),pos= (293,345))
        button_previous.update(screen)
        
      #  draw_text('game', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    main_menu()
            if event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    lvl8()
            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    lvl6()
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    maze1()
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    maze1()
            if event.type == MOUSEBUTTONDOWN:
                if button_play.checkForInput(pygame.mouse.get_pos()):
                    maze1()
                if button_goback.checkForInput(pygame.mouse.get_pos()):
                    main_menu()
                if button_next.checkForInput(pygame.mouse.get_pos()):
                    lvl8()
                if button_previous.checkForInput(pygame.mouse.get_pos()):
                    lvl6()
        
        pygame.display.update()
        mainClock.tick(60)

def lvl8():
    running = True
    while running:
        bg = pygame.image.load("menu\lvl8.PNG")
        screen.fill((0,0,0))
        screen.blit(bg, (0, 0))

        button_play = Button(base_image=pygame.image.load("menu\playb.png"),
        hovering_image=pygame.image.load("menu\playb.png"), pos= (400,245))
        button_play.update(screen)

        button_goback = Button(base_image=pygame.image.load("menu\gobackb.png"),
        hovering_image=pygame.image.load("menu\gobackb.png"),pos= (280,245))
        button_goback.update(screen)

        button_next = Button(base_image=pygame.image.load("menu\extb.png"),
        hovering_image=pygame.image.load("menu\extb.png"),pos= (390,345))
        button_next.update(screen)
        
        button_previous = Button(base_image=pygame.image.load("menu\prevb.png"),
        hovering_image=pygame.image.load("menu\prevb.png"),pos= (293,345))
        button_previous.update(screen)
        
      #  draw_text('game', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    main_menu()
            if event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    lvl9()
            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    lvl7()
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    maze1()
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    maze1()
            if event.type == MOUSEBUTTONDOWN:
                if button_play.checkForInput(pygame.mouse.get_pos()):
                    maze1()
                if button_goback.checkForInput(pygame.mouse.get_pos()):
                    main_menu()
                if button_next.checkForInput(pygame.mouse.get_pos()):
                    lvl9()
                if button_previous.checkForInput(pygame.mouse.get_pos()):
                    lvl7()
        pygame.display.update()
        mainClock.tick(60)

def lvl9():
    running = True
    while running:
        bg = pygame.image.load("menu\lvl9.PNG")
        screen.fill((0,0,0))
        screen.blit(bg, (0, 0))

        button_play = Button(base_image=pygame.image.load("menu\playb.png"),
        hovering_image=pygame.image.load("menu\playb.png"), pos= (400,245))
        button_play.update(screen)

        button_goback = Button(base_image=pygame.image.load("menu\gobackb.png"),
        hovering_image=pygame.image.load("menu\gobackb.png"),pos= (280,245))
        button_goback.update(screen)

        button_next = Button(base_image=pygame.image.load("menu\extb.png"),
        hovering_image=pygame.image.load("menu\extb.png"),pos= (390,345))
        button_next.update(screen)
        
        button_previous = Button(base_image=pygame.image.load("menu\prevb.png"),
        hovering_image=pygame.image.load("menu\prevb.png"),pos= (293,345))
        button_previous.update(screen)
        
      #  draw_text('game', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    main_menu()
            if event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    lvl10()
            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    lvl8()
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    maze1()
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    maze1()
            if event.type == MOUSEBUTTONDOWN:
                if button_play.checkForInput(pygame.mouse.get_pos()):
                    maze1()
                if button_goback.checkForInput(pygame.mouse.get_pos()):
                    main_menu()
                if button_next.checkForInput(pygame.mouse.get_pos()):
                    lvl10()
                if button_previous.checkForInput(pygame.mouse.get_pos()):
                    lvl8()
        
        pygame.display.update()
        mainClock.tick(60)

def lvl10():
    running = True
    while running:
        bg = pygame.image.load("menu\lvl10.PNG")
        screen.fill((0,0,0))
        screen.blit(bg, (0, 0))

        button_play = Button(base_image=pygame.image.load("menu\playb.png"),
        hovering_image=pygame.image.load("menu\playb.png"), pos= (400,245))
        button_play.update(screen)

        button_goback = Button(base_image=pygame.image.load("menu\gobackb.png"),
        hovering_image=pygame.image.load("menu\gobackb.png"),pos= (280,245))
        button_goback.update(screen)

        button_next = Button(base_image=pygame.image.load("menu\extb.png"),
        hovering_image=pygame.image.load("menu\extb.png"),pos= (390,345))
        button_next.update(screen)
        
        button_previous = Button(base_image=pygame.image.load("menu\prevb.png"),
        hovering_image=pygame.image.load("menu\prevb.png"),pos= (293,345))
        button_previous.update(screen)
        
      #  draw_text('game', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    main_menu()
            if event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    lvl11()
            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    lvl9()
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    maze1()
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    maze1()
            if event.type == MOUSEBUTTONDOWN:
                if button_play.checkForInput(pygame.mouse.get_pos()):
                    maze1()
                if button_goback.checkForInput(pygame.mouse.get_pos()):
                    main_menu()
                if button_next.checkForInput(pygame.mouse.get_pos()):
                    lvl11()
                if button_previous.checkForInput(pygame.mouse.get_pos()):
                    lvl9()
            
        
        pygame.display.update()
        mainClock.tick(60)

def lvl11():
    running = True
    while running:
        bg = pygame.image.load("menu\lvl11.PNG")
        screen.fill((0,0,0))
        screen.blit(bg, (0, 0))

        button_play = Button(base_image=pygame.image.load("menu\playb.png"),
        hovering_image=pygame.image.load("menu\playb.png"), pos= (400,245))
        button_play.update(screen)

        button_goback = Button(base_image=pygame.image.load("menu\gobackb.png"),
        hovering_image=pygame.image.load("menu\gobackb.png"),pos= (280,245))
        button_goback.update(screen)

        button_next = Button(base_image=pygame.image.load("menu\extb.png"),
        hovering_image=pygame.image.load("menu\extb.png"),pos= (390,345))
        button_next.update(screen)
        
        button_previous = Button(base_image=pygame.image.load("menu\prevb.png"),
        hovering_image=pygame.image.load("menu\prevb.png"),pos= (293,345))
        button_previous.update(screen)
        
      #  draw_text('game', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                 if event.key == K_ESCAPE:
                    main_menu()
            if event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    lvl12()
            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    lvl10()
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    maze1()
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    maze1()
            if event.type == MOUSEBUTTONDOWN:
                if button_play.checkForInput(pygame.mouse.get_pos()):
                    maze1()
                if button_goback.checkForInput(pygame.mouse.get_pos()):
                    main_menu()
                if button_next.checkForInput(pygame.mouse.get_pos()):
                    lvl12()
                if button_previous.checkForInput(pygame.mouse.get_pos()):
                    lvl10()
        
        pygame.display.update()
        mainClock.tick(60)

def lvl12():
    running = True
    while running:
        bg = pygame.image.load("menu\lvl12.PNG")
        screen.fill((0,0,0))
        screen.blit(bg, (0, 0))
        
        button_play = Button(base_image=pygame.image.load("menu\playb.png"),
        hovering_image=pygame.image.load("menu\playb.png"), pos= (400,245))
        button_play.update(screen)

        button_goback = Button(base_image=pygame.image.load("menu\gobackb.png"),
        hovering_image=pygame.image.load("menu\gobackb.png"),pos= (280,245))
        button_goback.update(screen)

        button_next = Button(base_image=pygame.image.load("menu\extb.png"),
        hovering_image=pygame.image.load("menu\extb.png"),pos= (390,345))
        button_next.update(screen)
        
        button_previous = Button(base_image=pygame.image.load("menu\prevb.png"),
        hovering_image=pygame.image.load("menu\prevb.png"),pos= (293,345))
        button_previous.update(screen)
        
      #  draw_text('game', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    main_menu()
            if event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    lvl13()
            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    lvl11()
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    maze1()
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    maze1()
            if event.type == MOUSEBUTTONDOWN:
                if button_play.checkForInput(pygame.mouse.get_pos()):
                    maze1()
                if button_goback.checkForInput(pygame.mouse.get_pos()):
                    main_menu()
                if button_next.checkForInput(pygame.mouse.get_pos()):
                    lvl13()
                if button_previous.checkForInput(pygame.mouse.get_pos()):
                    lvl11()
        
        pygame.display.update()
        mainClock.tick(60)

def lvl13():
    running = True
    while running:
        bg = pygame.image.load("menu\lvl13.PNG")
        screen.fill((0,0,0))
        screen.blit(bg, (0, 0))

        button_play = Button(base_image=pygame.image.load("menu\playb.png"),
        hovering_image=pygame.image.load("menu\playb.png"), pos= (400,245))
        button_play.update(screen)

        button_goback = Button(base_image=pygame.image.load("menu\gobackb.png"),
        hovering_image=pygame.image.load("menu\gobackb.png"),pos= (280,245))
        button_goback.update(screen)

        button_next = Button(base_image=pygame.image.load("menu\extb.png"),
        hovering_image=pygame.image.load("menu\extb.png"),pos= (390,345))
        button_next.update(screen)
        
        button_previous = Button(base_image=pygame.image.load("menu\prevb.png"),
        hovering_image=pygame.image.load("menu\prevb.png"),pos= (293,345))
        button_previous.update(screen)

      #  draw_text('game', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    main_menu()
            if event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    lvl14()
            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    lvl12()
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    maze1()
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    maze1()
            if event.type == MOUSEBUTTONDOWN:
                if button_play.checkForInput(pygame.mouse.get_pos()):
                    maze1()
                if button_goback.checkForInput(pygame.mouse.get_pos()):
                    main_menu()
                if button_next.checkForInput(pygame.mouse.get_pos()):
                    lvl14()
                if button_previous.checkForInput(pygame.mouse.get_pos()):
                    lvl12()
                    
        pygame.display.update()
        mainClock.tick(60)

def lvl14():
    running = True
    while running:
        bg = pygame.image.load("menu\lvl14.PNG")
        screen.fill((0,0,0))
        screen.blit(bg, (0, 0))

        button_play = Button(base_image=pygame.image.load("menu\playb.png"),
        hovering_image=pygame.image.load("menu\playb.png"), pos= (400,245))
        button_play.update(screen)

        button_goback = Button(base_image=pygame.image.load("menu\gobackb.png"),
        hovering_image=pygame.image.load("menu\gobackb.png"),pos= (280,245))
        button_goback.update(screen)

        button_next = Button(base_image=pygame.image.load("menu\extb.png"),
        hovering_image=pygame.image.load("menu\extb.png"),pos= (390,345))
        button_next.update(screen)
        
        button_previous = Button(base_image=pygame.image.load("menu\prevb.png"),
        hovering_image=pygame.image.load("menu\prevb.png"),pos= (293,345))
        button_previous.update(screen)
        
      #  draw_text('game', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    main_menu()
            if event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    lvl15()
            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    lvl13()
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    maze1()
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    maze1()
            if event.type == MOUSEBUTTONDOWN:
                if button_play.checkForInput(pygame.mouse.get_pos()):
                    maze1()
                if button_goback.checkForInput(pygame.mouse.get_pos()):
                    main_menu()
                if button_next.checkForInput(pygame.mouse.get_pos()):
                    lvl15()
                if button_previous.checkForInput(pygame.mouse.get_pos()):
                    lvl13()
        
        pygame.display.update()
        mainClock.tick(60)

def lvl15():
    running = True
    while running:
        bg = pygame.image.load("menu\lvl15.PNG")
        screen.fill((0,0,0))
        screen.blit(bg, (0, 0))

        button_play = Button(base_image=pygame.image.load("menu\playb.png"),
        hovering_image=pygame.image.load("menu\playb.png"), pos= (400,245))
        button_play.update(screen)

        button_goback = Button(base_image=pygame.image.load("menu\gobackb.png"),
        hovering_image=pygame.image.load("menu\gobackb.png"),pos= (280,245))
        button_goback.update(screen)

        button_next = Button(base_image=pygame.image.load("menu\extb.png"),
        hovering_image=pygame.image.load("menu\extb.png"),pos= (390,345))
        button_next.update(screen)
        
        button_previous = Button(base_image=pygame.image.load("menu\prevb.png"),
        hovering_image=pygame.image.load("menu\prevb.png"),pos= (293,345))
        button_previous.update(screen)
        
      #  draw_text('game', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    main_menu()
            if event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    lvl16()
            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    lvl14()
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    maze1()
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    maze1()
            if event.type == MOUSEBUTTONDOWN:
                if button_play.checkForInput(pygame.mouse.get_pos()):
                    maze1()
                if button_goback.checkForInput(pygame.mouse.get_pos()):
                    main_menu()
                if button_next.checkForInput(pygame.mouse.get_pos()):
                    lvl16()
                if button_previous.checkForInput(pygame.mouse.get_pos()):
                    lvl14()
        
        pygame.display.update()
        mainClock.tick(60)

def lvl16():
    running = True
    while running:
        bg = pygame.image.load("menu\lvl16.PNG")
        screen.fill((0,0,0))
        screen.blit(bg, (0, 0))

        button_play = Button(base_image=pygame.image.load("menu\playb.png"),
        hovering_image=pygame.image.load("menu\playb.png"), pos= (400,245))
        button_play.update(screen)

        button_goback = Button(base_image=pygame.image.load("menu\gobackb.png"),
        hovering_image=pygame.image.load("menu\gobackb.png"),pos= (280,245))
        button_goback.update(screen)
        
        button_previous = Button(base_image=pygame.image.load("menu\prevb.png"),
        hovering_image=pygame.image.load("menu\prevb.png"),pos= (293,345))
        button_previous.update(screen)
        
      #  draw_text('game', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                 if event.key == K_ESCAPE:
                    main_menu()
            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    lvl15()
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    maze1()
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    maze1()
            if event.type == MOUSEBUTTONDOWN:
                if button_play.checkForInput(pygame.mouse.get_pos()):
                    maze1()
                if button_goback.checkForInput(pygame.mouse.get_pos()):
                    main_menu()
                if button_previous.checkForInput(pygame.mouse.get_pos()):
                    lvl15()
        
        pygame.display.update()
        mainClock.tick(60)

def maze1():
    running = True
    while running:
        bg = pygame.image.load("menu\win_model.PNG")
        screen.fill(BLACK)
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

def maze2():
    running = True
    while running:
        bg = pygame.image.load("menu\wyly_0.PNG")
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



main_menu()
