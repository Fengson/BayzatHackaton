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
		self.player_angle = 0
		#self.level = level1

		MAP = level_data["level1"]

		self.current_map = [[0 for x in range(MAP_WIDTH)] for x in range(MAP_HEIGHT)] 
		for x in range(MAP_WIDTH):
			for y in range(MAP_HEIGHT):
				self.current_map[x][y] = Block(MAP[x][y], x * 64, y * 64)

		self.surface = pygame.display.set_mode(screen_size, DOUBLEBUF)
		self.loop()

	def drawMap(self):
		for x in range(MAP_WIDTH):
			for y in range(MAP_HEIGHT):
				tile = self.current_map[x][y].block_type
				self.surface.blit(pygame.transform.rotate(tiles[tile], self.player_angle), (x*64,y*64))

	def loop(self):
		while self.gamestate == 1:
			for event in pygame.event.get():
				if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
					self.gamestate = 0

				self.drawMap()
				pygame.display.flip()

if __name__ == '__main__':
	Game()