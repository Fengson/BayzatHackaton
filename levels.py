import pygame

level1 = [[2,2,2,2,1,1,1,1,1,1],
      	  [1,1,1,1,1,1,1,1,1,1],
	      [1,1,1,1,1,1,1,1,1,1],
	      [1,1,1,1,1,1,1,1,1,1],
	      [1,1,1,1,1,1,1,1,1,1],
	      [1,1,1,1,1,1,1,1,1,1],
	      [1,1,1,1,1,1,1,1,1,1],
	      [1,1,1,1,1,1,1,1,1,1],
	      [1,1,1,1,1,1,1,1,1,1],
	      [1,1,1,1,1,1,1,1,1,1]]
level1 = [list(i) for i in zip(*level1)]
level1_x = 1
level1_y = 1


tiles = [None] * 25
tiles[0] = pygame.image.load('images/player.png')
tiles[1] = pygame.image.load('images/tile1.png')
tiles[2] = pygame.image.load('images/water.png')