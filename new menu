import pygame, sys

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
        bg = pygame.image.load("wyly_0.PNG")
        screen.fill((0,0,0))
        screen.blit(bg, (0, 0))

        draw_text('Press any key to start', font, (252, 3, 3), screen, 440, 210)
        draw_text('LEFT and RIGHT arrow keys', font, (252, 3, 3), screen, 440, 305)
        draw_text('to switch levels', font, (252, 3, 3), screen, 470, 335)
        draw_text('ESCAPE key to go back', font, (252, 3, 3), screen, 440, 374)
        draw_text('to start page', font, (252, 3, 3), screen, 470, 404)
        draw_text('SPACE or RETURN key to go', font, (252, 3, 3), screen, 440, 440)
        draw_text('to selected level', font, (252, 3, 3), screen, 470, 470)
        
##
##        button_1 = pygame.image.load("b1.PNG")
##        screen.blit(button_1, (380,115))
##        button_2 = pygame.image.load("b2.PNG")
##        screen.blit(button_2, (513,115))
##        button_3 = pygame.image.load("b3.PNG")
##        screen.blit(button_3, (650,115))
##        button_4 = pygame.image.load("b4.PNG")
##        screen.blit(button_4, (385,220))
##        button_5 = pygame.image.load("b5.PNG")
##        screen.blit(button_5, (515,220))
##        button_6 = pygame.image.load("b6.PNG")
##        screen.blit(button_6, (659,300))
##        button_7 = pygame.image.load("b7.PNG")
##        screen.blit(button_7, (380,325))
##        button_8 = pygame.image.load("b8.PNG")
##        screen.blit(button_8, (515,325))
##        button_9 = pygame.image.load("b9.PNG")
##        screen.blit(button_9, (660,355))
##        button_10 = pygame.image.load("b10.PNG")
##        screen.blit(button_10, (380,442))
##        button_11 = pygame.image.load("b11.PNG")
##        screen.blit(button_11, (515,436))
##        button_12 = pygame.image.load("b12.PNG")
##        screen.blit(button_12, (658,400))
##        button_13 = pygame.image.load("b13.PNG")
##        screen.blit(button_13, (380,490))
##        button_14 = pygame.image.load("b14.PNG")
##        screen.blit(button_14, (520,490))
##        button_15 = pygame.image.load("b15.PNG")
##        screen.blit(button_15, (660,490))
##        button_16 = pygame.image.load("b16.PNG")
##        screen.blit(button_16, (520,535))

##        myMask = pygame.mask(button_1)
##        mySurface = myMask.to_surface()

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
        bg = pygame.image.load("lvl1.PNG")
        screen.fill((0,0,0))
        screen.blit(bg, (0, 0))

        button_play = pygame.image.load("playb.PNG")
        screen.blit(button_play, (400,245))

        button_goback = pygame.image.load("gobackb.PNG")
        screen.blit(button_goback, (280,245))

        button_next = pygame.image.load("nextb.PNG")
        screen.blit(button_next, (340,345))
##
##        playbutton = pygame.Rect(50,100,200,50)
##        if playbutton.collidepoint((mx,my)):
##            if pygame.mouse.get_pressed():
##                maze1()
##
##        pygame.draw.rect(screen, (255,0,0), playbutton)
##        click = pygame.mouse.get_pressed()
##
##        if click == (406, 285):
##            maze1()
##        x= 444
##        y = 285

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
                if button_play.get_rect().collidepoint((mx, my)):
                    maze1()
               
##            if event.type == MOUSEBUTTONDOWN:
##                if collidepoint((mx, my)):
##                    maze1()
                    # lr (406, 285) (485, 285)
                    #du (441, 329) (441, 250)
##            if event.type == MOUSEBUTTONDOWN:
##                if button_goback.get_rect().collidepoint((mx, my)):
##                    main_menu()
                    #  lr (298, 285) (377, 285)
                    #du (335, 329) (335, 250)
##            if event.type == pygame.MOUSEBUTTONDOWN:
##                if button_next.get_rect().collidepoint((mx, my)):
##                    lvl2()
                    # ul (upper left), ur, ll, lr (356,350) (436,350) (356,430) (436,430)

        pygame.display.update()
        mainClock.tick(60)

def lvl2():
    running = True
    while running:
        bg = pygame.image.load("lvl2.PNG")
        screen.fill((0,0,0))
        screen.blit(bg, (0, 0))

        button_play = pygame.image.load("playb.PNG")
        screen.blit(button_play, (400,245))

        button_goback = pygame.image.load("gobackb.PNG")
        screen.blit(button_goback, (280,245))

        button_next = pygame.image.load("nextb.PNG")
        screen.blit(button_next, (377,345))
        
        button_previous = pygame.image.load("prevb.png")
        screen.blit(button_previous, (293,345))

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
        #1:  ul (upper left), ur, ll, lr (308,350) (388,350) (308,430) (388,430)
        #2: ul (upper left), ur, ll, lr (398,350) (475,350) (398,430) (475,430)
        pygame.display.update()
        mainClock.tick(60)

def lvl3():
    running = True
    while running:
        bg = pygame.image.load("lvl3.PNG")
        screen.fill((0,0,0))
        screen.blit(bg, (0, 0))

        button_play = pygame.image.load("playb.PNG")
        screen.blit(button_play, (400,245))

        button_goback = pygame.image.load("gobackb.PNG")
        screen.blit(button_goback, (280,245))

        button_next = pygame.image.load("nextb.PNG")
        screen.blit(button_next, (377,345))
        
        button_previous = pygame.image.load("prevb.png")
        screen.blit(button_previous, (293,345))
        
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
        
        pygame.display.update()
        mainClock.tick(60)

def lvl4():
    running = True
    while running:
        bg = pygame.image.load("lvl4.PNG")
        screen.fill((0,0,0))
        screen.blit(bg, (0, 0))

        button_play = pygame.image.load("playb.PNG")
        screen.blit(button_play, (400,245))

        button_goback = pygame.image.load("gobackb.PNG")
        screen.blit(button_goback, (280,245))

        button_next = pygame.image.load("nextb.PNG")
        screen.blit(button_next, (377,345))
        
        button_previous = pygame.image.load("prevb.png")
        screen.blit(button_previous, (293,345))
        
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
        
        pygame.display.update()
        mainClock.tick(60)

def lvl5():
    running = True
    while running:
        bg = pygame.image.load("lvl5.PNG")
        screen.fill((0,0,0))
        screen.blit(bg, (0, 0))

        button_play = pygame.image.load("playb.PNG")
        screen.blit(button_play, (400,245))

        button_goback = pygame.image.load("gobackb.PNG")
        screen.blit(button_goback, (280,245))

        button_next = pygame.image.load("nextb.PNG")
        screen.blit(button_next, (377,345))
        
        button_previous = pygame.image.load("prevb.png")
        screen.blit(button_previous, (293,345))
        
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
        
        pygame.display.update()
        mainClock.tick(60)

def lvl6():
    running = True
    while running:
        bg = pygame.image.load("lvl6.PNG")
        screen.fill((0,0,0))
        screen.blit(bg, (0, 0))

        button_play = pygame.image.load("playb.PNG")
        screen.blit(button_play, (400,245))

        button_goback = pygame.image.load("gobackb.PNG")
        screen.blit(button_goback, (280,245))

        button_next = pygame.image.load("nextb.PNG")
        screen.blit(button_next, (377,345))
        
        button_previous = pygame.image.load("prevb.png")
        screen.blit(button_previous, (293,345))
        
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
        
        pygame.display.update()
        mainClock.tick(60)

def lvl7():
    running = True
    while running:
        bg = pygame.image.load("lvl7.PNG")
        screen.fill((0,0,0))
        screen.blit(bg, (0, 0))

        button_play = pygame.image.load("playb.PNG")
        screen.blit(button_play, (400,245))

        button_goback = pygame.image.load("gobackb.PNG")
        screen.blit(button_goback, (280,245))

        button_next = pygame.image.load("nextb.PNG")
        screen.blit(button_next, (377,345))
        
        button_previous = pygame.image.load("prevb.png")
        screen.blit(button_previous, (293,345))
        
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
        
        pygame.display.update()
        mainClock.tick(60)

def lvl8():
    running = True
    while running:
        bg = pygame.image.load("lvl8.PNG")
        screen.fill((0,0,0))
        screen.blit(bg, (0, 0))

        button_play = pygame.image.load("playb.PNG")
        screen.blit(button_play, (400,245))

        button_goback = pygame.image.load("gobackb.PNG")
        screen.blit(button_goback, (280,245))

        button_next = pygame.image.load("nextb.PNG")
        screen.blit(button_next, (377,345))
        
        button_previous = pygame.image.load("prevb.png")
        screen.blit(button_previous, (293,345))
        
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
        pygame.display.update()
        mainClock.tick(60)

def lvl9():
    running = True
    while running:
        bg = pygame.image.load("lvl9.PNG")
        screen.fill((0,0,0))
        screen.blit(bg, (0, 0))

        button_play = pygame.image.load("playb.PNG")
        screen.blit(button_play, (400,245))

        button_goback = pygame.image.load("gobackb.PNG")
        screen.blit(button_goback, (280,245))

        button_next = pygame.image.load("nextb.PNG")
        screen.blit(button_next, (377,345))
        
        button_previous = pygame.image.load("prevb.png")
        screen.blit(button_previous, (293,345))
        
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
        
        pygame.display.update()
        mainClock.tick(60)

def lvl10():
    running = True
    while running:
        bg = pygame.image.load("lvl10.PNG")
        screen.fill((0,0,0))
        screen.blit(bg, (0, 0))

        button_play = pygame.image.load("playb.PNG")
        screen.blit(button_play, (400,245))

        button_goback = pygame.image.load("gobackb.PNG")
        screen.blit(button_goback, (280,245))

        button_next = pygame.image.load("nextb.PNG")
        screen.blit(button_next, (377,345))
        
        button_previous = pygame.image.load("prevb.png")
        screen.blit(button_previous, (293,345))
        
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
        
        pygame.display.update()
        mainClock.tick(60)

def lvl11():
    running = True
    while running:
        bg = pygame.image.load("lvl11.PNG")
        screen.fill((0,0,0))
        screen.blit(bg, (0, 0))

        button_play = pygame.image.load("playb.PNG")
        screen.blit(button_play, (400,245))

        button_goback = pygame.image.load("gobackb.PNG")
        screen.blit(button_goback, (280,245))

        button_next = pygame.image.load("nextb.PNG")
        screen.blit(button_next, (377,345))
        
        button_previous = pygame.image.load("prevb.png")
        screen.blit(button_previous, (293,345))
        
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
        
        pygame.display.update()
        mainClock.tick(60)

def lvl12():
    running = True
    while running:
        bg = pygame.image.load("lvl12.PNG")
        screen.fill((0,0,0))
        screen.blit(bg, (0, 0))
        
        button_play = pygame.image.load("playb.PNG")
        screen.blit(button_play, (400,245))

        button_goback = pygame.image.load("gobackb.PNG")
        screen.blit(button_goback, (280,245))

        button_next = pygame.image.load("nextb.PNG")
        screen.blit(button_next, (377,345))
        
        button_previous = pygame.image.load("prevb.png")
        screen.blit(button_previous, (293,345))
        
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
        
        pygame.display.update()
        mainClock.tick(60)

def lvl13():
    running = True
    while running:
        bg = pygame.image.load("lvl13.PNG")
        screen.fill((0,0,0))
        screen.blit(bg, (0, 0))

        button_play = pygame.image.load("playb.PNG")
        screen.blit(button_play, (400,245))

        button_goback = pygame.image.load("gobackb.PNG")
        screen.blit(button_goback, (280,245))

        button_next = pygame.image.load("nextb.PNG")
        screen.blit(button_next, (377,345))
        
        button_previous = pygame.image.load("prevb.png")
        screen.blit(button_previous, (293,345))

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
                    
        pygame.display.update()
        mainClock.tick(60)

def lvl14():
    running = True
    while running:
        bg = pygame.image.load("lvl14.PNG")
        screen.fill((0,0,0))
        screen.blit(bg, (0, 0))

        button_play = pygame.image.load("playb.PNG")
        screen.blit(button_play, (400,245))

        button_goback = pygame.image.load("gobackb.PNG")
        screen.blit(button_goback, (280,245))

        button_next = pygame.image.load("nextb.PNG")
        screen.blit(button_next, (377,345))
        
        button_previous = pygame.image.load("prevb.png")
        screen.blit(button_previous, (293,345))
        
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
        
        pygame.display.update()
        mainClock.tick(60)

def lvl15():
    running = True
    while running:
        bg = pygame.image.load("lvl15.PNG")
        screen.fill((0,0,0))
        screen.blit(bg, (0, 0))

        button_play = pygame.image.load("playb.PNG")
        screen.blit(button_play, (400,245))

        button_goback = pygame.image.load("gobackb.PNG")
        screen.blit(button_goback, (280,245))

        button_next = pygame.image.load("nextb.PNG")
        screen.blit(button_next, (377,345))
        
        button_previous = pygame.image.load("prevb.png")
        screen.blit(button_previous, (293,345))
        
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
        
        pygame.display.update()
        mainClock.tick(60)

def lvl16():
    running = True
    while running:
        bg = pygame.image.load("lvl16.PNG")
        screen.fill((0,0,0))
        screen.blit(bg, (0, 0))

        button_play = pygame.image.load("playb.PNG")
        screen.blit(button_play, (400,245))

        button_goback = pygame.image.load("gobackb.PNG")
        screen.blit(button_goback, (280,245))
        
        button_previous = pygame.image.load("prevb.png")
        screen.blit(button_previous, (340,345))
        
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
        
        pygame.display.update()
        mainClock.tick(60)

def maze1():
    running = True
    while running:
        bg = pygame.image.load("win_model.PNG")
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

def maze2():
    running = True
    while running:
        bg = pygame.image.load("wyly_0.PNG")
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
