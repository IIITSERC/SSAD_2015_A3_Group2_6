import pygame
import sys


pygame.init()

class Donkey(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load('final_images/donkey3.gif')
		self.image.convert()
		self.rect = self.image.get_rect()
		self.rect.left = 170
		self.rect.top = 30
		pygame.draw.rect(self.image, (255,0,0), self.rect)
