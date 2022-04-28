import pygame




class Button():
	def __init__(self, base_image,hovering_image, pos):
		self.x_pos = pos[0]
		self.y_pos = pos[1]
		self.base_image, self.hovering_image = base_image, hovering_image
		self.image = base_image
		self.rect = self.image.get_rect(topleft=(self.x_pos, self.y_pos))
		# self.wyly_image, self.level_image = wyly_image, level_image
		# self.wyly = wyly_image
		# self.wyly_rect = self.wyly.get_rect(topleft=(0, 148))

        


	def update(self, screen):
		# self.wyly = pygame.transform.scale(self.wyly, WYLY_SIZE)
		screen.blit(self.image, self.rect)
		# screen.blit(self.wyly, self.wyly_rect)


	def checkForInput(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			return True
		return False

	def changeColor(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.image = self.hovering_image
			# self.wyly = self.level_image

		else:
			self.image = self.base_image
			# self.wyly = self.wyly_image
    
# pygame.display.set_caption("Main Menu")

            # while (self.state == 'start'):
            #     self.screen.fill(BLACK)

            #     mouse_pos = pygame.mouse.get_pos()

            #     self.draw_text('Menu',self.screen,[WIDTH//2,10], 
            #     START_TEXT_SIZE, (255,255,255), START_FONT, centered = True)

            #     wyly_img = level.L1.w_img

            #     Level_One = Button(base_image=pygame.image.load('tech pics\levelOne_unclicked.PNG'),
            #     hovering_image=pygame.image.load('tech pics\level_one_clicked.PNG'),
            #     wyly_image=wyly_img,
            #     level_image=level.L1.wyly, pos=(350, 100))

            #     Level_Two = Button(base_image=pygame.image.load('tech pics\level_two_unclicked.PNG'),
            #     hovering_image=pygame.image.load('tech pics\level_two_clicked.PNG'),
            #     wyly_image=wyly_img,
            #     level_image=level.L2.wyly, pos=(500, 400))


            #     for button in [Level_One]:
            #         button.changeColor( mouse_pos)
            #         button.update(self.screen)

            #     for event in pygame.event.get():
            #         if event.type == pygame.QUIT:
            #             pygame.quit()
            #             sys.exit()
            #         if event.type == pygame.MOUSEBUTTONDOWN:
            #             if Level_One.checkForInput(mouse_pos):
            #                 self.maze = pygame.image.load('maze_4.jpg')
            #                 self.load('level_4.txt')
            #                 self.state = 'playing'

                # pygame.display.update()



            # pygame.draw.rect(self.screen, RED, button_1)
            # pygame.draw.rect(self.screen, RED, button_2)
        
            # for event in pygame.event.get():
            #     mx,my = pygame.mouse.get_pos()
            #     if button_1.collidepoint((mx,my)):
            #         if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

            #             self.state = 'playing'