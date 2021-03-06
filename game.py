import os, sys
import pygame
from pygame.locals import *
from block import *
from levels import *

screen_size = (800,640)
MAP_WIDTH  = 10
MAP_HEIGHT = 10

level_data = {"level1" : level1, "level1_total" : level1_total, "level1_x" : level1_player_x, "level1_y" : level1_player_y, "level1_teleport_ins": level1_teleport_ins, "level1_teleport_outs" : level1_teleport_outs,
			  "level2" : level2, "level2_total" : level2_total, "level2_x" : level2_player_x, "level2_y" : level2_player_y, "level2_teleport_ins": level2_teleport_ins, "level2_teleport_outs" : level2_teleport_outs,
			  "level3" : level3, "level3_total" : level3_total, "level3_x" : level3_player_x, "level3_y" : level3_player_y, "level3_teleport_ins": level3_teleport_ins, "level3_teleport_outs" : level3_teleport_outs,
			  "level4" : level4, "level4_total" : level4_total, "level4_x" : level4_player_x, "level4_y" : level4_player_y, "level4_teleport_ins": level4_teleport_ins, "level4_teleport_outs" : level4_teleport_outs,
			  "level5" : level5, "level5_total" : level5_total, "level5_x" : level5_player_x, "level5_y" : level5_player_y, "level5_teleport_ins": level5_teleport_ins, "level5_teleport_outs" : level5_teleport_outs}

class Game(object):
	def __init__(self, level_num=1):
		pygame.init()
		self.width = 640
		self.height = 480
		self.esc_pressed = 0
		self.gamestate = 1
		self.keypressed = 0
		self.level_num = level_num
		self.level = "level" + str(level_num)
		self.current_total = 0
		self.key = 0
		
		self.level_total = level_data[self.level + "_total"]
		self.level_teleport_ins = level_data[self.level + "_teleport_ins"]
		self.level_teleport_outs = level_data[self.level + "_teleport_outs"]

		self.doors_locked_sound = pygame.mixer.Sound("sounds/door-locked.wav")
		self.doors_open_sound = pygame.mixer.Sound("sounds/door-open.wav")
		self.move_sound = pygame.mixer.Sound("sounds/move.wav")
		self.teleport_sound = pygame.mixer.Sound("sounds/teleport.wav")
		self.document_sound = pygame.mixer.Sound("sounds/place-doc.wav")

		self.music = pygame.mixer.Sound("sounds/drums.wav")
		self.music.play(-1,0)

		MAP = level_data[self.level]

		# Map
		self.current_map = [[0 for x in range(MAP_WIDTH)] for x in range(MAP_HEIGHT)] 
		for x in range(MAP_WIDTH):
			for y in range(MAP_HEIGHT):
				self.current_map[x][y] = Block(MAP[x][y], x * 64, y * 64)

		self.surface = pygame.display.set_mode(screen_size, DOUBLEBUF)

		# Player
		player_init_x = level_data[self.level + "_x"]
		player_init_y = level_data[self.level + "_y"]
		self.player = Block(0, player_init_x * 64, player_init_y * 64)
		self.player_angle = 0
		self.current_map[player_init_x][player_init_y] = self.player

		self.revert_array = []

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

			self.move_sound.play()

		 	if next_step == 1:
				self.swap(x, y)
			else:
				# Purple doc
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

				# Red doc
				if next_step == 17:
					if x == 1 and self.player.x + x + 1 < MAP_WIDTH and self.current_map[self.player.x + x + 1][self.player.y + y].block_type in [1,17,18]:
						self.swap(x,y)
						self.checkIfPlacedOnCorrectTile(x, y, 18)
					elif x == -1 and self.player.x + x - 1 >= 0 and self.current_map[self.player.x + x - 1][self.player.y + y].block_type in [1,17,18]:
						self.swap(x,y)
						self.checkIfPlacedOnCorrectTile(x, y, 18)
					elif y == 1 and self.player.y + y + 1 < MAP_HEIGHT and self.current_map[self.player.x + x][self.player.y + y + 1].block_type in [1,17,18]:
						self.swap(x,y)
						self.checkIfPlacedOnCorrectTile(x, y, 18)
					elif y == -1 and self.player.y + y - 1 >= 0 and self.current_map[self.player.x + x][self.player.y + y - 1].block_type in [1,17,18]:
						self.swap(x,y)
						self.checkIfPlacedOnCorrectTile(x, y, 18)
					else:
						pass
				else:
					pass

				# Bayzat doc
				if next_step == 13:
					if x == 1 and self.player.x + x + 1 < MAP_WIDTH and self.current_map[self.player.x + x + 1][self.player.y + y].block_type in [1,13,14]:
						self.swap(x,y)
						self.checkIfPlacedOnCorrectTile(x, y, 14)
					elif x == -1 and self.player.x + x - 1 >= 0 and self.current_map[self.player.x + x - 1][self.player.y + y].block_type in [1,13,14]:
						self.swap(x,y)
						self.checkIfPlacedOnCorrectTile(x, y, 14)
					elif y == 1 and self.player.y + y + 1 < MAP_HEIGHT and self.current_map[self.player.x + x][self.player.y + y + 1].block_type in [1,13,14]:
						self.swap(x,y)
						self.checkIfPlacedOnCorrectTile(x, y, 14)
					elif y == -1 and self.player.y + y - 1 >= 0 and self.current_map[self.player.x + x][self.player.y + y - 1].block_type in [1,13,14]:
						self.swap(x,y)
						self.checkIfPlacedOnCorrectTile(x, y, 14)
					else:
						pass
				else:
					pass

				# Key
				if next_step == 9:
					self.swap(x,y)
					self.key += 1

				# Lock
				if next_step == 10:
					if self.key > 0:
						self.move_sound.stop()
						self.doors_open_sound.play()
						self.key -= 1
						self.swap(x,y)
					else:
						self.doors_locked_sound.play()

				if next_step == 11:
					pos = (self.player.x + x, self.player.y + y)
					if pos in self.level_teleport_ins:
						self.teleport_sound.play()
						idx = self.level_teleport_ins.index(pos)
						out_pos = self.level_teleport_outs[idx]
						self.current_map[self.player.x][self.player.y].block_type = 1
						self.current_map[out_pos[0]][out_pos[1]].block_type = 0
						self.player.x = out_pos[0]
						self.player.y = out_pos[1]

	def checkIfPlacedOnCorrectTile(self, x, y, correctTile):
		if self.current_map[self.player.x + x][self.player.y + y].block_type == correctTile:
			self.current_total += 1
			
			self.move_sound.stop()
			self.document_sound.play()

			self.current_map[self.player.x + x][self.player.y + y].block_type = correctTile + 1

			# All checks passed
			if self.current_total == self.level_total:
				self.finish_current()

		else:
			self.current_map[self.player.x + x][self.player.y + y].block_type = correctTile - 1

	def swap(self, x, y):
		self.current_map[self.player.x + x][self.player.y + y].block_type = 0
		self.current_map[self.player.x][self.player.y].block_type = 1
		self.player.x += x
		self.player.y += y

	def finish_current(self):
		self.gamestate = 0

	def next_level(self):
		next_lvl = int(self.level[-1])

		if next_lvl <= total_levels - 1:
			next_lvl += 1
			self.music.stop()
			Game(next_lvl)
		else:
			self.music.stop()
			self.victory()

	def victory(self):
		Victory()		

	def loop(self):
		while self.gamestate == 1:
			for event in pygame.event.get():
				if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
					self.esc_pressed = 1
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

				self.surface.fill(pygame.Color("black"), (658,128, 150, 50))
				self.surface.fill(pygame.Color("black"), (658,192, 150, 50))			
				self.surface.fill(pygame.Color("black"), (750,355, 50, 50))
				self.surface.fill(pygame.Color("black"), (655,352, 100, 100))


				font = pygame.font.Font(None, 36)
				small_font = pygame.font.Font(None, 26)

				keys_text = font.render("Keys:", 1, (255, 255, 255))
				self.surface.blit(keys_text, (655,320))

				if self.key > 0:
					orange_keys_text = small_font.render("Orange: " + str(self.key), 1, (255, 255, 255))
					self.surface.blit(orange_keys_text, (655,352))
				else :
					orange_keys_text = small_font.render("0 available.", 1, (255, 255, 255))
					self.surface.blit(orange_keys_text, (655,352))

				block_text = font.render("Docs: " + str(self.current_total) + " / " + str(self.level_total), 1, (255, 255, 255))
				self.surface.blit(block_text, (655,128))

				pygame.display.flip()

				if event.type == KEYUP:
					self.keypressed = 0

		if self.esc_pressed == 0:
			self.next_level()

class Victory(object):
	def __init__(self):
		pygame.init()
		self.surface = pygame.display.set_mode(screen_size, DOUBLEBUF)
		self.gamestate = 1

		self.screen = pygame.image.load('images/victory.png')
		self.music = pygame.mixer.Sound("sounds/victory.wav")
		self.music.stop()
		self.music.play()

		self.loop()

	def game_exit(self):
		exit()
 
	def loop(self):
		while self.gamestate==1:
			for event in pygame.event.get():
				if event.type==QUIT or (event.type==KEYDOWN and event.key==K_ESCAPE):
					self.gamestate=0

			self.surface.blit(self.screen, (0,0))
			pygame.display.flip()
			
		self.game_exit()

if __name__ == '__main__':
	Game(1)
