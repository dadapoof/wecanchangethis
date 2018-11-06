import sys 
import pygame
import time
from pygame.locals import *

WHITE = [255, 255, 255]
BLACK = [0,0,0]
RED = [255, 0, 0]

class Wall(pygame.sprite.Sprite):

	def __init__(self, x, y, width, height, color):
		super().__init__()

		self.image = pygame.Surface([width, height])
		self.image.fill(color)

		self.rect = self.image.get_rect()
		self.rect.y = y
		self.rect.x = x


class Room(object):
	wall_list = None
	rock_sprites = None

	def __init__(self):
		self.wall_list = pygame.sprite.Group()
		self.rock_sprites = pygame.sprite.Group()


class Room1(Room):
	def __init__(self):
		super().__init__()

		walls = [[0, 0, 20, 600, WHITE],
				   [0, 0, 800, 20, WHITE],
				   [0, 580, 800, 20, WHITE],
				   [780, 0, 20, 800, WHITE]
				  ]

		for item in walls:
			wall = Wall(item[0], item[1], item[2], item[3], item[4])
			self.wall_list.add(wall)

class Enemy(pygame.sprite.Sprite):

	change_x = 0
	change_y = 0

	def __init__(self, x, y):
		super().__init__()

		self.image = pygame.Surface([30, 30])
		self.image.fill(RED)

		self.rect = self.image.get_rect()
		self.rect.y = y
		self.rect.x = x

	def getrect(self):
		return self.rect

	def changespeed(self, x, y, player):

		if self.rect.x > player.rect.x:
			self.change_x = -2
		elif self.rect.x < player.rect.x:
			self.change_x = 2
		elif self.rect.x == player.rect.x:
			self.change_x = 0
		if self.rect.y > player.rect.y:
			self.change_y = -2
		elif self.rect.y < player.rect.y:
			self.change_y = 2
		elif self.rect.y == player.rect.y:
			self.change_y = 0



	def move(self, walls, player):

		self.rect.x += self.change_x

		block_hit_list = pygame.sprite.spritecollide(self, walls, False)
		for block in block_hit_list:
			# If we are moving right, set our right side to the left side of
			# the item we hit
			if self.change_x > 0:
				self.rect.right = block.rect.left
			else:
				# Otherwise if we are moving left, do the opposite.
				self.rect.left = block.rect.right

		self.rect.y += self.change_y
		
		block_hit_list = pygame.sprite.spritecollide(self, walls, False)
		for block in block_hit_list:

			# Reset our position based on the top/bottom of the object.
			if self.change_y > 0:
				self.rect.bottom = block.rect.top
			else:
				self.rect.top = block.rect.bottom



class Player(pygame.sprite.Sprite):

	change_x = 0
	change_y = 0
 

	def __init__(self, x, y):
		# Constructor function
 
		# Call the parent's constructor
		super().__init__()
 
		# Set height, width
		self.image = pygame.Surface([15, 15])
		self.image.fill(WHITE)
 
		# Make our top-left corner the passed-in location.
		self.rect = self.image.get_rect()
		self.rect.y = y
		self.rect.x = x

	def getrect(self):
		return self.rect

	def changespeed(self, x, y):
		""" Change the speed of the player. Called with a keypress. """
		self.change_x += x
		self.change_y += y

	def move(self, walls):
		""" Find a new position for the player """
 
		# Move left/right
		self.rect.x += self.change_x

		# Did this update cause us to hit a wall?
		block_hit_list = pygame.sprite.spritecollide(self, walls, False)
		for block in block_hit_list:
			# If we are moving right, set our right side to the left side of
			# the item we hit
			if self.change_x > 0:
				self.rect.right = block.rect.left
			else:
				# Otherwise if we are moving left, do the opposite.
				self.rect.left = block.rect.right

		# Move up/down
		self.rect.y += self.change_y

		# Check and see if we hit anything
		block_hit_list = pygame.sprite.spritecollide(self, walls, False)
		for block in block_hit_list:

			# Reset our position based on the top/bottom of the object.
			if self.change_y > 0:
				self.rect.bottom = block.rect.top
			else:
				self.rect.top = block.rect.bottom

def main():

	pygame.init()

	screen = pygame.display.set_mode([800, 600])
	# screen.fill(BLACK)
	pygame.display.set_caption("YEET OR GET YEETED")
	pygame.display.update()

	room = Room()

	player = Player(50,50)
	enemy = Enemy(400, 350)
	enemy2 = Enemy(300, 600)

	moving_sprites = pygame.sprite.Group()
	moving_sprites.add(player)
	moving_sprites.add(enemy)
	moving_sprites.add(enemy2)

	room = Room1()

	pygame.display.update()
	done = False

	while not done:

		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					done = True

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
			enemy.changespeed(0, 0, player)
			enemy2.changespeed(0,0,player)

		enemy.changespeed(0, 0, player)
		enemy2.changespeed(0,0,player)
		player.move(room.wall_list)
		enemy.move(room.wall_list, player)
		enemy2.move(room.wall_list, player)

		player_hit = pygame.sprite.collide_rect(enemy, player)
		player_hit2 = pygame.sprite.collide_rect(enemy2, player)
		if player_hit or player_hit2:
			screen.fill(RED)
			pygame.display.flip()
			game_over()


		screen.fill(BLACK)
		moving_sprites.draw(screen)
		room.wall_list.draw(screen)
		pygame.display.flip()

	pygame.quit()

def game_over():
	time.sleep(1)
	pygame.quit()

if __name__ == "__main__":
	main()
