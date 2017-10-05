import random
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

def display_level(level):
        window = pg.display.set_mode((640,480), RESIZABLE)
        keep_open = 1
        
        wall = pg.image.load("wall.png").convert()
        macgyver = pg.image.load("macgyver.png").convert_alpha()
        guardian = pg.image.load("guardian.png").convert_alpha()
        #Redimensioning of the images, to adapt to the window size
        wall = pg.transform.scale(wall,(int(650/15),int(480/15)))
        macgyver = pg.transform.scale(macgyver,(int(650/15),int(480/15)))
        guardian = pg.transform.scale(guardian,(int(650/15),int(480/15)))
        #Static positioning of the labyrinth and the characters
        num_line = 0
        empty_cells = [] #List of empty cells
        for line in level :
                num_col=0
                y=num_line*480/15
                for cell in line :
                        x = num_col*640/15
                        if cell=="w":
                                window.blit(wall,(x,y))  
                        if cell=="d":
                                window.blit(macgyver,(x,y))
                        if cell=="f":
                                window.blit(guardian,(x,y))
                        elif cell=="0":
                                empty_cells.append([x,y])                                
                        num_col += 1
                num_line += 1
        #Random positioning of the obects
        position1 = random.randint(0,len(empty_cells))
        position2 = random.randint(0,len(empty_cells))
        position3 = random.randint(0,len(empty_cells))
        #print(position1,position2,position3)
        #print(empty_cells)
        #print(len(empty_cells))
        window.blit(macgyver,empty_cells[position1])
        window.blit(macgyver,empty_cells[position2])
        window.blit(macgyver,empty_cells[position3])
        
        pg.display.flip()      
        while keep_open :
                for event in pg.event.get(): 
                        if event.type == QUIT :
                                keep_open = 0
                        elif event.type == KEYDOWN:
                                if event.key == K_UP:
                                        pass
                                if event.key == K_DOWN:
                                        pass
                                if event.key == K_LEFT:
                                        pass
                                if event.key == K_RIGHT:
                                        pass
                
current_level = create_level()
display_level(current_level)

