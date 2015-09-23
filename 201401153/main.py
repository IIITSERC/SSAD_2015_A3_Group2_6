import pygame
import os
import sys
import time
import random
from pygame.locals import *
from player import *
from donkey import *
from coins import *
#from fireball import *


pygame.init()

black= 0, 0, 0
red = 255,0,0

screen =pygame.display.set_mode((930,675))
pygame.display.set_caption('Dokey Kong Game')
#clock = pygame.time.Clock()

surface = pygame.image.load('final_images/wallnew.jpg')
surface.convert()

#donkey = pygame.image.load('final_images/donkey3.gif')
#donkey.convert()

fireball = pygame.image.load('final_images/fireballn.png')
fireball.convert()

ladder = pygame.image.load('final_images/ladder21.png')
ladder.convert()

ladder2 = pygame.image.load('final_images/ladder22.png')
ladder2.convert()

princess = pygame.image.load('final_images/princess61.png')
princess.convert()

#player1=pygame.image.load('final_images/player1.png')
#player1.convert()

player2=pygame.image.load('final_images/player2.png')
player2.convert()

player= Person()
donkey= Donkey()

coin = Coin()
coin1 = Coin()
coin2 = Coin()
coin3 = Coin()
coin4 = Coin()
coin5 = Coin()
coin6 = Coin()

#	coins.add(coin)


#def player(x,y):
 #   screen.blit(player1,(x,y))


def game_loop():

	x=40
	y=583
	while 1:
	    for event in pygame.event.get():
	        if event.type == pygame.QUIT:
	            sys.exit()
	        elif event.type == pygame.KEYDOWN:
	            if event.key == pygame.K_ESCAPE:
	               sys.exit()
	        elif event.type == pygame.KEYUP:
	           	if event.key == pygame.K_d:
	         		player.move_right()
	      	 	elif event.key == pygame.K_a:
	     	  		player.move_left()
	    	   	elif event.key == pygame.K_w:
	     	  		player.move_up()
	    	   	elif event.key == pygame.K_s:
	    	   		player.move_down()



	    screen.fill((0, 0, 200))
	    screen.blit(surface,(0,655))
	    screen.blit(surface,(280,655))
	    screen.blit(surface,(560,655))
	    screen.blit(surface,(660,655))
	    screen.blit(surface,(0,495))
	    screen.blit(surface,(390,495))
	    screen.blit(surface,(500,495))
	    screen.blit(surface,(700,495))
	    screen.blit(surface,(0,335))
	    screen.blit(surface,(248,335))
	    screen.blit(surface,(640,335))
	    screen.blit(surface,(0,165))
	    screen.blit(surface,(280,165))
	    screen.blit(surface,(560,165))
	    screen.blit(surface,(720,165))


	    screen.blit(fireball,(600,138))


	    screen.blit(ladder,(560,495))
	    screen.blit(ladder,(130,335))
	    screen.blit(ladder2,(740,165))

	    screen.blit(princess,(300,0))

	    #screen.blit(donkey,(200,30))
		
		#coins.draw(screen)


	    

	    mlist=pygame.sprite.Group()
	    mlist.add(player)
	    mlist.add(donkey)
	    mlist.add(coin)
	    mlist.add(coin1)
	    mlist.add(coin2)
	    mlist.add(coin3)
	    mlist.add(coin4)
	    mlist.add(coin5)
	    mlist.add(coin6)

	    mlist.draw(screen)

	    pygame.display.update()

game_loop()
pygame.quit()
quit()
