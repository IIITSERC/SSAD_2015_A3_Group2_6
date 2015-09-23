import pygame
import sys
import random

pygame.init()

class Coin(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		coins = pygame.sprite.OrderedUpdates()
		for i in range(20):
		   	self.image = pygame.image.load('final_images/coin62.png')
			self.image.convert()
			self.rect = self.image.get_rect()
			self.rect.left = random.randint(1,22)*40
			self.rect.top = random.randint(0,8)*90
			coins.add(self)
			pygame.draw.rect(self.image, (255,0,0), self.rect)
			pygame.display.update()