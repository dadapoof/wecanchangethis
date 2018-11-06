import pygame

WHITE = {255, 255, 255}

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

		walls = [[0, 0, 20, 200, WHITE],
				 [0, 200, -200, 20, WHITE],
				 [200, 0, 20, 200, WHITE],
				 [200, 200, -200, 20, WHITE],
				]

		for item in walls:
			wall = Wall(item[0], item[1], item[2], item[3], item[4])
			self.wall_list.add(wall)