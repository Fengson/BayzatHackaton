import pygame

total_levels = 2

level1 = [[2,2,2,2,2,2,2,2,2,2],
      	  [2,1,1,6,1,1,7,2,2,2],
	      [2,1,1,2,2,1,2,2,2,2],
	      [2,2,2,2,2,1,2,2,2,2],
	      [2,2,2,2,2,6,2,2,2,2],
	      [2,7,1,6,1,1,2,2,2,2],
	      [2,2,2,2,2,7,2,2,2,2],
	      [2,2,2,2,2,2,2,2,2,2],
	      [2,2,2,2,2,2,2,2,2,2],
	      [2,2,2,2,2,2,2,2,2,2]]
level1 = [list(i) for i in zip(*level1)]
level1_player_x = 1
level1_player_y = 1
level1_total = 3

level2 = [[2,2,2,2,2,2,2,2,2,2],
      	  [2,2,2,2,2,2,2,2,2,2],
	      [2,2,1,1,1,5,1,1,2,2],
	      [2,2,1,2,2,2,2,1,2,2],
	      [2,2,1,2,2,2,2,6,2,2],
	      [2,2,1,2,2,2,2,1,2,2],
	      [2,2,1,2,2,2,2,7,2,2],
	      [2,2,5,2,2,2,2,2,2,2],
	      [2,2,2,2,2,2,2,2,2,2],
	      [2,2,2,2,2,2,2,2,2,2]]
level2 = [list(i) for i in zip(*level2)]
level2_total = 1
level2_player_x = 2
level2_player_y = 2


tiles = [None] * 25
# 0 - Jenny (Player)
# 1 - Default sidewalk / road
# 2 - Water (barrier)
# 3 - Pyramid (barrier)

tiles[0] = pygame.image.load('images/player.png')
tiles[1] = pygame.image.load('images/tile1.png')
tiles[2] = pygame.image.load('images/building_4.png')
tiles[3] = pygame.image.load('images/building_2.png')
tiles[4] = pygame.image.load('images/building_3.png')
tiles[5] = pygame.image.load('images/water.png')
tiles[6] = pygame.image.load('images/document_purple.png')
tiles[7] = pygame.image.load('images/purple-start.png')
tiles[8] = pygame.image.load('images/purple_end.png')