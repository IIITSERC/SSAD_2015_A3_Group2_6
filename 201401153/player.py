import pygame
import sys

pygame.init()


class Person(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load('final_images/player1.png')
		self.image.convert()
		self.rect = self.image.get_rect()
		self.rect.left = 40
		self.rect.top = 583
		pygame.draw.rect(self.image, (255,0,0), self.rect)
	def move_right(self):
		self.rect = self.rect.move([20,0])		
	def move_left(self):
		self.rect = self.rect.move([-20,0])
	def move_up(self):
		self.rect = self.rect.move([0,-20])
	def move_down(self):
		self.rect = self.rect.move([0,20])			
