#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame

class Block(object):
	def __init__(self, block_type, x, y):
		self.x = x / 64
		self.y = y / 64
		self.block_type = block_type