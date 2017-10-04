import pygame as pg
from pygame.locals import *

def create_level():
	level=[]
	with open("level1.txt") as f:
		for line in f:
			lines=[]
			for cell in line:
				if cell != '\n':
					lines.append(cell)
			level.append(lines)
	print("Voici le labyrinthe sous forme de liste:",level)
	print("Voici la 4e ligne:",level[3])
	return level
	
create_level()

