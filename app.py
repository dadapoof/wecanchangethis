import sys 
import room1
import pygame
import player
from pygame.locals import *


def main():

	pygame.init()

	screen = pygame.display.set_mode([800, 600])

	player = Player(50,50)

	if event.type == pygame.KEYDOWN:
		if event.key == pygame.K_LEFT:
			player.changespeed(-5, 0)
		if event.key == pygame.K_RIGHT:
			player.changespeed(5, 0)
		if event.key == pygame.K_UP:
			player.changespeed(0, -5)
		if event.key == pygame.K_DOWN:
			player.changespeed(0, 5)

	if event.type == pygame.KEYUP:
		if event.key == pygame.K_LEFT:
			player.changespeed(5, 0)
		if event.key == pygame.K_RIGHT:
			player.changespeed(-5, 0)
		if event.key == pygame.K_UP:
			player.changespeed(0, 5)
		if event.key == pygame.K_DOWN:
			player.changespeed(0, -5)



if __name__ == "__main__":
	 main()
