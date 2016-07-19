import os, sys
import pygame
from pygame.locals import *
from block import *
from levels import *

screen_size = (800,640)
MAP_WIDTH  = 10
MAP_HEIGHT = 10

level_data = {"level1" : level1}

class Game(object):
	def __init__(self):
		pygame.init()
		self.width = 640
		self.height = 480
		self.gamestate = 1
		self.keypressed = 0
		self.level = "level1"
		self.current_total = 0
		self.level_total = 3 # change this later

		MAP = level_data["level1"]

		# Map
		self.current_map = [[0 for x in range(MAP_WIDTH)] for x in range(MAP_HEIGHT)] 
		for x in range(MAP_WIDTH):
			for y in range(MAP_HEIGHT):
				self.current_map[x][y] = Block(MAP[x][y], x * 64, y * 64)

		self.surface = pygame.display.set_mode(screen_size, DOUBLEBUF)

		# Player
		player_init_x = 1
		player_init_y = 1
		self.player = Block(0, player_init_x * 64, player_init_y * 64)
		self.player_angle = 0
		self.current_map[player_init_x][player_init_y] = self.player


		self.loop()

	def drawMap(self):
		for x in range(MAP_WIDTH):
			for y in range(MAP_HEIGHT):
				tile = self.current_map[x][y].block_type
				if tile == 0:
					self.surface.blit(pygame.transform.rotate(tiles[tile], self.player_angle), (x*64,y*64))
				else:
					self.surface.blit(tiles[tile], (x*64,y*64))

	def move(self, x, y, angle):
		self.player_angle = angle

		if self.player.x + x >= 0 and self.player.x + x < MAP_WIDTH and self.player.y + y >= 0 and self.player.y + y < MAP_HEIGHT:

			next_step = self.current_map[self.player.x + x][self.player.y + y].block_type
			next_pos =  (self.current_map[self.player.x + x][self.player.y + y].x, self.current_map[self.player.x + x][self.player.y + y].y)

		 	if next_step == 1:
				self.swap(x, y)
			else:
				# Purple block
				if next_step == 6:
					if x == 1 and self.player.x + x + 1 < MAP_WIDTH and self.current_map[self.player.x + x + 1][self.player.y + y].block_type in [1,6,7]:
						self.swap(x,y)
						self.checkIfPlacedOnCorrectTile(x, y, 7)
					elif x == -1 and self.player.x + x - 1 >= 0 and self.current_map[self.player.x + x - 1][self.player.y + y].block_type in [1,6,7]:
						self.swap(x,y)
						self.checkIfPlacedOnCorrectTile(x, y, 7)
					elif y == 1 and self.player.y + y + 1 < MAP_HEIGHT and self.current_map[self.player.x + x][self.player.y + y + 1].block_type in [1,6,7]:
						self.swap(x,y)
						self.checkIfPlacedOnCorrectTile(x, y, 7)
					elif y == -1 and self.player.y + y - 1 >= 0 and self.current_map[self.player.x + x][self.player.y + y - 1].block_type in [1,6,7]:
						self.swap(x,y)
						self.checkIfPlacedOnCorrectTile(x, y, 7)
					else:
						pass
				else:
					pass

	def checkIfPlacedOnCorrectTile(self, x, y, correctTile):
		if self.current_map[self.player.x + x][self.player.y + y].block_type == correctTile:
			self.current_total += 1

			self.current_map[self.player.x + x][self.player.y + y].block_type = correctTile + 1

			# All checks passed
			if self.current_total == self.level_total:
				print "End of Level"

		else:
			self.current_map[self.player.x + x][self.player.y + y].block_type = correctTile - 1

	def swap(self, x, y):
		self.current_map[self.player.x + x][self.player.y + y].block_type = 0
		self.current_map[self.player.x][self.player.y].block_type = 1
		self.player.x += x
		self.player.y += y

	def loop(self):
		while self.gamestate == 1:
			for event in pygame.event.get():
				if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
					self.gamestate = 0

				if event.type == KEYDOWN and event.key == pygame.K_s and self.keypressed == 0:
					self.move(0, 1, 0)
					self.keypressed = 1
				if event.type == KEYDOWN and event.key == pygame.K_w and self.keypressed == 0:
					self.move(0, -1, 180)
					self.keypressed = 1
				if event.type == KEYDOWN and event.key == pygame.K_a and self.keypressed == 0:
					self.move(-1,0, 270)
					self.keypressed = 1
				if event.type == KEYDOWN and event.key == pygame.K_d and self.keypressed == 0:
					self.move(1,0, 90)
					self.keypressed = 1

				self.drawMap()
				pygame.display.flip()

				if event.type == KEYUP:
					self.keypressed = 0

if __name__ == '__main__':
	Game()
