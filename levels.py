import pygame

total_levels = 4

level1 = [[2,2,2,2,2,2,2,2,2,2],
      	  [2,1,1,6,1,1,7,2,2,2],
	      [2,1,1,2,2,1,2,2,2,2],
	      [2,2,2,2,2,1,3,2,2,2],
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
level1_teleport_ins = []
level1_teleport_outs = []

level2 = [[2,2,2,2,2,2,2,2,2,2],
      	  [2,2,2,2,2,16,2,2,2,2],
	      [2,2,1,1,1,10,1,1,2,2],
	      [2,2,1,2,2,2,2,1,2,2],
	      [2,2,1,2,2,2,2,6,2,2],
	      [2,2,1,2,2,2,2,1,2,2],
	      [2,2,1,2,2,2,2,7,2,2],
	      [2,2,9,2,2,2,2,2,2,2],
	      [2,2,2,2,2,2,2,2,2,2],
	      [2,2,2,2,2,2,2,2,2,2]]
level2 = [list(i) for i in zip(*level2)]
level2_total = 1
level2_player_x = 2
level2_player_y = 2
level2_teleport_ins = []
level2_teleport_outs = []

level3 = [[1,1,1,1,1,9,2,12,1,1],
      	  [1,2,2,2,2,2,2,2,2,1],
	      [1,2,2,2,2,2,2,2,2,1],
	      [11,2,2,2,2,2,11,9,10,1],
	      [2,2,2,2,2,2,2,2,2,1],
	      [2,2,2,2,2,2,2,2,2,1],
	      [2,2,2,2,2,12,2,2,2,2],
	      [2,2,2,2,2,1,6,1,7,2],
	      [2,2,2,2,2,2,2,2,2,2],
	      [2,2,2,2,2,2,2,2,2,2]]
level3 = [list(i) for i in zip(*level3)]
level3_total = 1
level3_total_moves = 30 # 28
level3_player_x = 0
level3_player_y = 0
level3_hidden_fields = 0
level3_teleport_ins = [(0,3), (6,3)]
level3_teleport_outs = [(7,0), (5,6)]

level4 = [[5,5,5,5,5,5,5,5,5,5],
      	  [5,5,5,1,1,1,1,5,5,5],
	      [5,5,5,1,1,1,1,5,5,5],
	      [5,1,1,1,1,1,1,1,1,5],
	      [5,1,1,1,13,1,1,14,1,5],
	      [5,1,1,1,1,1,1,1,1,5],
	      [5,1,1,1,1,1,1,1,1,5],
	      [5,5,5,1,1,1,1,5,5,5],
	      [5,5,5,1,1,1,1,5,5,5],
	      [5,5,5,5,5,5,5,5,5,5]]
level4 = [list(i) for i in zip(*level4)]
level4_total = 1
level4_total_moves = 1000
level4_player_x = 1
level4_player_y = 3
level4_hidden_fields = 0
level4_teleport_ins = []
level4_teleport_outs = []


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
tiles[9] = pygame.image.load('images/key.png')
tiles[10] = pygame.image.load('images/lock.png')
tiles[11] = pygame.image.load('images/teleport_in.png')
tiles[12] = pygame.image.load('images/teleport_out.png')
tiles[13] = pygame.image.load('images/document_green.png')
tiles[14] = pygame.image.load('images/green-start.png')
tiles[15] = pygame.image.load('images/green-end.png')
tiles[16] = pygame.image.load('images/building_1.png')

